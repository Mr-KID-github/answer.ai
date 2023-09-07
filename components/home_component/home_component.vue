<template>
	<view class="frame">
		<!-- 拍照搜题 -->
		<view class="button_item" @click="chooseAndUploadImage">
			<view class="text_frame">
				<text class="text1">拍照搜题</text>
				<text class="text2">扫描并获取作业答案 By AI</text>
			</view>
			<image src="/static/camera.svg"></image>
		</view>
		
		<!-- 提问框 -->
		<view class="response_result" v-if="work_image">
			<image mode="widthFix" :src="work_image" @error="handleImageError"></image>
		</view>
		
		<!-- 标题框架:Chat Test -->
		<view class="title_frame" v-if="markdownData">
			<text class="title_2">解析题目数据</text>
			<joMarkdown :nodes="markdownData"></joMarkdown>
		</view>
		
		<!-- 标题框架:Chat Test -->
		<view class="title_frame" v-if="markdownData">
			<text class="title_1">深入交流</text>
			<text class="title_2">如果有不懂的地方继续提问吧~</text>
		</view>
		
		<!-- 提问框 -->
		<view v-if="markdownData" class="frame">
			<custom_input @click_ask="handleAskData"></custom_input>
			<view class="title_frame">
				<text class="title_2">你好呀！很高兴见到你。有什么我可以帮助你的吗？</text>
				<text class="title_2">{{deep_answer_data[-1].content}}</text>
			</view>
		</view>
	</view>
</template>

<script>
	import markdownFunc from '@/uni_modules/jo-markdown/components/jo-markdown/index.js';
	import joMarkdown from '@/uni_modules/jo-markdown/components/jo-markdown/decode.vue';
	
	export default {
		name:"home_component",
		components: {
			joMarkdown  // 这里使用了上面导入的名称
		},
		data() {
			return {
				work_image:"",
				// parts: []
				markdownData: {},
				deep_answer_data: []
			};
		},
		methods: {
			latexBackground(svgData) {
			    return `background-image: url(${svgData}); background-size: cover;`;
			},
			handleImageError(e) {
				console.log('Image loading error:', e);
			},
			isLatex(part) {
			    console.log("isLatex:",part);
			    if (typeof part === 'string') {
			        // 检查是否是 SVG 图像的 Base64 编码数据
			        if (part.startsWith("data:image/svg+xml;base64")) {
						console.log("part是svg")
						return true;
			        }
			    }
			    return false;
			},
			chooseAndUploadImage() {
				var that = this
				uni.chooseImage({
				        count: 1, // 可选择的图片数量，这里设置为1表示每次只能选择一张图片
				        sourceType: ['album', 'camera'], // 图片的来源，可以是相册或相机
				        success: (res) => {
						  const tempFilePath = res.tempFilePaths[0];	// 选择的图片临时文件路径
						  uni.getFileSystemManager().readFile({
							  filePath: tempFilePath,
							  encoding: 'base64',
							  success: (readFileRes) => {
								  const base64Data = 'data:image/jpeg;base64,' + readFileRes.data;
								  that.work_image = base64Data;
								  // console.log("that.work_image:",that.work_image)
							  }
						  });
				          // 处理选择的图片逻辑，比如上传到服务器等
						  that.upload_img_to_server(res.tempFilePaths[0])
				        },
				        fail: (err) => {
				          console.log(err)
				        }
				});
			},
			// 处理提问框提出问题
			handleAskData(data){
				console.log("处理提问框提出问题：",data)
				// 将其添加到深入提问数组
				this.deep_answer_data.push({
					"content": "",
					"question": data
				})
				console.log(this.deep_answer_data)
				this.deep_ask_answer()
			},
			// 深入提问数学题目
			deep_ask_answer() {
				uni.showLoading({
					title:"提问中..."
				})
				uni.request({
					url: getApp().globalData.server + '/deep_ask_answer',
					method: 'POST',
					data: JSON.stringify(this.deep_answer_data),
					header: {
						'content-type': 'application/json' // 设置请求的 header
					},
					success: (res) => {
						console.log(res);
						const content = res.data.data.content
						
						try{
							console.log(this.deep_answer_data)
							if (this.deep_answer_data[-1].question && this.deep_answer_data[-1].content) {
								this.deep_answer_data[-1].content = content
							}
						}catch(e){
							// 删除this.deep_answer_data最后一个对象
							this.deep_answer_data.pop();
							console.log("清楚刚才提出的问题：",this.deep_answer_data)
							console.log(e)
						}
					},
					fail: (err) => {
						console.error("请求失败: ", err);
					},
					complete() {
						uni.hideLoading()
					}
				})
			},
			// 数学题目解析
			upload_img_to_server(filePath) {
				console.log("调用upload_img_to_server,现在已经改为调用use_mathAPI")
			    uni.showLoading({
					title: "解析中..."
				})
				uni.uploadFile({
			        url: getApp().globalData.server + '/use_mathAPI',
			        filePath: filePath,
			        name: "image",
			        success: (res) => {
						console.log(res)
						if (res.statusCode == 200) {
							console.log("解析出来的数据如下：\n",JSON.parse(res.data))
							const content = JSON.parse(res.data).content
							const question = JSON.parse(res.data).question
							// 赋值问题和答案方便传递给chatgpt深入回答
							this.deep_answer_data = []		// 初始化数组
							this.deep_answer_data.push({
								"content": content,
								"question": question
							})
							try{
								this.markdownData = markdownFunc(content,"markdown");
							}catch(e){
								this.markdownData = content
							}
						}
			            else {
							uni.showModal({
								title:"太火爆了",
								content:"请稍后再试",
								showCancel: false
							})
						}
						
			        },
			        fail: () => {
			            uni.showToast({
			                title: 'Server error',
			                icon: 'none'
			            });
			        },
					complete() {
						uni.hideLoading()
					}
			    });
			},
						
		}
	}
</script>

<style>
	.title_1{
		color: var(--gray-900, #18181B);
		font-feature-settings: 'clig' off, 'liga' off;
		font-family: Manrope;
		font-size: 22px;
		font-style: normal;
		font-weight: 800;
		line-height: 30px; /* 136.364% */
		letter-spacing: -0.4px;
	}
	.frame{
		display: flex;
		width: 343px;
		flex-direction: column;
		align-items: flex-start;
		gap: 20px;
	}
	.combined-text{
		display: inline-flex;
		align-items: center;
		justify-content: center;
	}
	.answer_text{
		color: #000;
		font-family: Inter;
		font-size: 14px;
		font-style: normal;
		font-weight: 400;
		line-height: normal;
		 display: inline-block;
		letter-spacing: 0.28px;
	}
	.title_2{
		color: var(--gray-600, #52525B);
		font-feature-settings: 'clig' off, 'liga' off;
		font-family: Manrope;
		font-size: 16px;
		font-style: normal;
		font-weight: 500;
		line-height: 24px; /* 150% */
		letter-spacing: -0.4px;
	}
	.title_frame{
		display: flex;
		width: 343px;
		flex-direction: column;
		align-items: flex-start;
		gap: 12px;
	}
	.response_result{
		width: 303px;
		padding: 10px;
		border: 1px solid #ccc;
		border-radius: 10px;
		background-color: #f8f8f8;
	}
	
	.response_result image{
		border-radius: 10px;
		width: 100%;
	}
.bottom-section {
	        position: absolute;
	        bottom: 0;
	        left: 0;
	        right: 0;
	    }
	.button_item{
		width: 304px;
		height: 107px;
		flex-shrink: 0;
		display: flex;
		 align-items: center; /* 垂直居中 */
		border-radius: 20px;
		background: #F5F6FA;
		padding-left: 40px;
		
		position: relative;
	}
	.text_frame{
		display: inline-flex;
		flex-direction: column;
		align-items: flex-start;
		gap: 11px;
	}
	.text1{
		color: #000;
		font-family: ABeeZee;
		font-size: 18px;
		font-style: normal;
		font-weight: 600;
		line-height: 16px; /* 88.889% */
	}
	.text2{
		color: #8B8F92;
		font-family: ABeeZee;
		font-size: 12px;
		font-style: normal;
		font-weight: 400;
		line-height: 16px; /* 133.333% */
	}
	.button_item image{
		position: absolute;
		bottom: 0;  /* 贴在上边 */
		    right: 0;  /* 贴在右边 */
		width: 150px;
		height: 150px;
		flex-shrink: 0;
	}
</style>