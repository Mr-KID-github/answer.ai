<template>
	<view class="background">
		<view class="title">Answer AI China</view>
		

		<view style="margin-top:10px; width: 100%; padding-left: 40px; background: transparent; margin-bottom: 30px;">
			<u-tabs :list="list1"></u-tabs>
		</view>

		
		<view class="conten_frame">
			<!-- 拍照搜题 -->
			<view class="button_item" @click="chooseAndUploadImage">
				<view class="text_frame">
					<text class="text1">拍照搜题</text>
					<text class="text2">扫描并获取作业答案 By AI</text>
				</view>
				<image src="/static/camera.svg"></image>
			</view>
			
			<!-- 提问框 -->
			<view class="response_result">
				<image :src="work_image"></image>
			</view>
			
			<!-- 提问框 -->
			<!-- <view class="response_result" :style="gpt_answer?'width: 500rpx;':''">
				<image v-if="!gpt_answer" src="https://s3-alpha-sig.figma.com/img/46b9/ef5f/b5b166af39d5cf7d66c8cda918d6278c?Expires=1690156800&Signature=S8SSJ3JtrxTTwwlF-YFDyacPqAIdvJaOz-b-l4mjgT~~p~Fqhfsqcls~0t~0tiC2hLjTb3HTlJsJo2BcUjmtEfEm-1W0h4dB8dXPDhM5CnqqLl5arNPFYWihsBUvqlboUDI2m~VbkfGit7rS95uRByXHxKL53i9BM1hgRJt~TshEpQBhZJqKf8PzC37Y5EPXpt3VD858dKmhD3U5tHYjzJR0~GwFcwHnACzqDW1V6B-MnrHUZz1eYgeD1A3YvbxyhpZ~~G0CM71hZVOa8WHk39UgvS9v3C9I8Fp-2Xs~RVQlACtsSlIq6MRMgE-t~3iFXkg9qxm~qOcfevrAjXAj9A__&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4"></image>
				<text v-if="gpt_answer">{{gpt_answer}}</text>
			</view> -->
			
			<!-- 标题框架:Chat Test -->
			<view class="title_frame">
				<text class="title_2">解析题目数据</text>
				<text class="title_2">{{ analyze_math_data }}</text>
			</view>
				
			<!-- 标题框架:Chat Test -->
			<view class="title_frame">
				<text class="title_1">深入交流</text>
				<text class="title_2">如果有不懂的地方继续提问吧~</text>
			</view>
			
			<!-- 提问框 -->
			<custom_input></custom_input>
			<view class="title_frame">
				<text class="title_2">你好呀！很高兴见到你。我是ChatGPT，有什么我可以帮助你的吗？</text>
			</view>
		</view>
					
		<!-- 底部 -->			
		<view class="bottom-section">
			<!-- 滚动通知 -->
			<!-- <u-notice-bar bgColor="#ECF5FF" color="#3C9CFF" :text="text1" mode="closable" speed="0" customStyle=""></u-notice-bar> -->
			
			<!-- 底部导航栏 -->
			<u-tabbar
				:value="value6"
				@change="name => value6 = name"
				:fixed="true"
				:placeholder="true"
				:safeAreaInsetBottom="true"
			>
				<u-tabbar-item text="首页" icon="home" ></u-tabbar-item>
				<u-tabbar-item text="我的" icon="account" ></u-tabbar-item>
			</u-tabbar>
		</view>
	</view>
</template>

<script>
	 export default {
	        data() {
	            return {
	                list1: [{
	                    name: 'AI搜题',
	                }],
					value6: 0,
					text1: '快加入学习群',
					
					
					gpt_answer: 'Hello',
					work_image:"",
					originalText: "",
					analyze_math_data: "",
					currentCharIndex: 0
	            }
	        },
			onLoad() {
				// const MathJax = require('mathjax');
			},
			methods: {
				// 逐字显示
				displayTextByChar() {
					if (this.currentCharIndex < this.originalText.length) {
						this.analyze_math_data += this.originalText[this.currentCharIndex];
						this.currentCharIndex++;
						setTimeout(this.displayTextByChar, 100);  // 每 100 毫秒显示一个字符
					}
				},
				startDisplay() {
					this.analyze_math_data = "";  // 清空文本
					this.currentCharIndex = 0;  // 重置索引
					this.displayTextByChar();  // 开始逐字符显示
				},
				chooseAndUploadImage() {
					var that = this
					uni.chooseImage({
					        count: 1, // 可选择的图片数量，这里设置为1表示每次只能选择一张图片
					        sourceType: ['album', 'camera'], // 图片的来源，可以是相册或相机
					        success: (res) => {
					          const tempFilePaths = res.tempFilePaths; // 选择的图片临时文件路径
							  that.work_image = tempFilePaths
					          // 处理选择的图片逻辑，比如上传到服务器等
							  console.log(tempFilePaths)
							  that.upload_img_to_server(tempFilePaths[0])
					        },
					        fail: (err) => {
					          console.log(err)
					        }
					});
				},
			
				upload_img_to_server(filePath) {
					console.log("调用upload_img_to_server")
				    uni.uploadFile({
				        url: 'http://127.0.0.1:5000/upload', // 替换为您的服务器地址
				        filePath: filePath,
				        name: "image",
				        success: (res) => {
							console.log(res)
				            let data = res.data
				            if (data) {
								console.log("图片上传成功")
				                uni.showToast({
				                    title: 'Upload successful',
				                    icon: 'success'
				                });
								console.log("开始图片解析")
								this.analyze_img(data)
				            } else {
				                uni.showToast({
				                    title: 'Upload failed',
				                    icon: 'none'
				                });
				            }
				        },
				        fail: () => {
				            uni.showToast({
				                title: 'Server error',
				                icon: 'none'
				            });
				        }
				    });
				},
				async analyze_img(tempFilePaths){
					// 使用uni.uploadFile上传图片至云服务器
					console.log(tempFilePaths)
					const apiUrl = "https://math.rockeyops.com/api/v1/math/solve";
					const header = {
						"x-app-id": "math-app",
						"x-app-key": "7a6c508f25324c3d36c46c409c4f7f2b",
						"Content-Type": "application/json" // Assuming the API expects JSON content type
					};
					const data = {
						stream: false,
						url: tempFilePaths
					};
			
					try {
						uni.showLoading({
							title: "解析中..."
						})
						console.log("开始调用数学题扫描解答")
						const response = await uni.request({
							url: apiUrl,
							method: "POST",
							header: header,
							data: data
						});
			
						if (response.statusCode === 200) {
							console.log("API response:", response.data);
							// Process the response data as needed
							this.originalText = response.data.data.content
							this.startDisplay()
						} else {
							console.error("Error calling API:", response);
						}
					} catch (error) {
						console.error("API call failed:", error);
					} finally {
						uni.hideLoading()
					}
					
				},
			}
	    }
</script>

	
<style>
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
	.conten_frame{
		width: 343px;
		align-items: flex-start;
		gap: 20px;
		
		display: flex;
		flex-direction: column;
		align-items: center;
		padding-top: 50px;
		flex-shrink: 0;
		border-radius: 20px 20px 0px 0px;
		background: #FFF;
		
		margin-top: auto;
		width: 100%;
		flex: 1;  /* 这使得它能够自动扩展并占据所有剩余空间 */
		padding-bottom: 40px;
	}
.background{
	
	display: flex;
	align-items: center;
	flex-direction: column;
	padding-top: 20px;
	
	width: 100vw;
	height: 100vh;
	flex-shrink: 0;
	background: radial-gradient(circle, #8055FC, rgba(128, 85, 252, 0.00));
}
.title{
	color: #000;
	font-family: Inter;
	font-size: 12px;
	font-style: normal;
	font-weight: 700;
	line-height: normal;
}

	.title_frame{
		display: flex;
		width: 343px;
		flex-direction: column;
		align-items: flex-start;
		gap: 12px;
	}
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
	.button_example{
		/* 布局样式 */
		display: flex;
		width: 343px;
		padding: 10px 24px;
		justify-content: center;
		align-items: center;
		gap: 8px;
		border-radius: 12px;
		background: var(--teal-900, #134E4A);
		/* 字体 */
		color: var(--base-white, #FFF);
		font-feature-settings: 'clig' off, 'liga' off;
		font-family: Manrope;
		font-size: 16px;
		font-style: normal;
		font-weight: 700;
		line-height: 24px; /* 150% */
		letter-spacing: -0.4px;
	}
	.response_result{
			padding: 10px;
			border: 1px solid #ccc;
			border-radius: 10px;
			background-color: #f8f8f8;
	}
	
	.response_result image{
		border-radius: 10px;
	}
</style>
