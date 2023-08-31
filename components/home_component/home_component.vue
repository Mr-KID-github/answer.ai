<template>
	<view>
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
		<view class="title_frame" v-if="parts.length != 0">
			<text class="title_2">解析题目数据</text>
			<view v-for="(part, index) in parts" class="combined-text">
			    <view v-if="!isLatex(part)" class="answer_text">{{ parts[index] }}</view>
				<image v-else style="width: 200px;height: 200px;" :style="isLatex(part) ? latexBackground(part) : ''"></image>
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		name:"home_component",
		data() {
			return {
				work_image:"",
				parts: []
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
							const dataArray = JSON.parse(res.data);
							this.parts = dataArray
							console.log(this.parts);
						}
			            else {
							uni.showModal({
								title:"测试弹窗",
								content:"statusCode:" + res.statusCode,
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