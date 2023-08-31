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
			<view class="response_result" v-if="work_image">
				<image mode="widthFix" :src="work_image" @error="handleImageError"></image>
			</view>
			
			<!-- 标题框架:Chat Test -->
			<view class="title_frame" v-if="parts.length != 0">
				<text class="title_2">解析题目数据</text>
				<view v-for="(part, index) in parts">
				    <view v-if="!isLatex(part)">{{ parts[index] }}</view>
					<view v-else style="width: 303px; height: 202px;" :style="isLatex(part) ? latexBackground(part) : ''"></view>
				</view>
				<!-- <text class="title_2">{{ analyze_math_data }}</text> -->
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
					// originalText: "",
					analyze_math_data: "",
					currentCharIndex: 0,
					parts: []
	            }
	        },
			onLoad() {
				// const MathJax = require('mathjax');
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
				        // // 检查是否是 LaTeX 公式的文本表示
				        // if (part.startsWith('$') && part.endsWith('$')) {
				        //     return true;
				        // }
				        // // 检查是否是 PNG 图像的 Base64 编码数据
				        // if (part.startsWith("data:image/png;base64")) {
				        //     return true;
				        // }
				        // 检查是否是 SVG 图像的 Base64 编码数据
				        if (part.startsWith("data:image/svg+xml;base64")) {
							console.log("part是svg")
							return true;
				        }
				    }
				    return false;
				},
				// async getLatexImageUrl(formula,index) {
				// 	// console.log("之前的this.parts[index]：",this.parts[index])
				// 	// console.log(formula)
				//     let response = await uni.request({
				//         url: getApp().globalData.server + '/latex',
				//         method: 'POST',
				//         data: {
				//             formula: formula
				//         },
				//         responseType: 'arraybuffer'  // 这确保你获取的是一个字节流
				//     });
					
				//     // 将字节流转换为 data URL 以在前端显示
				//     console.log(response);
				//     const base64Data = uni.arrayBufferToBase64(response.data);
				//     const dataUrl = "data:image/png;base64," + base64Data;
				// 	// console.log(dataUrl)
				// 	// Vue 在处理数组更新时，可能不会检测到数组内部的变化，尤其是直接通过索引修改数组元素的情况。当你直接使用 this.parts[index] = dataUrl 进行更新时，Vue 可能不会认为 parts 发生了变化，因此不会重新渲染 DOM。
				// 	// 为了解决这个问题，你应该使用 Vue 的 this.$set 方法来更新数组元素。这会确保 Vue 知道数组发生了变化并触发重新渲染。
				// 	// this.parts[index] = dataUrl
				// 	this.$set(this.parts, index, dataUrl);
				// 	// console.log("之后的this.parts[index]：",this.parts[index])
				// },
				// async processText() {
				// 	// 使用正则表达式拆分文本
				// 	this.parts = this.originalText.split(/(\$\$?.+?\$\$?)/);
				// 	for (let i = 0; i < this.parts.length; i++) {
				// 		if (this.isLatex(this.parts[i])) {
				// 			this.getLatexImageUrl(this.parts[i],i);
				// 		}
				// 	}
				// },
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
				
			// 	async analyze_img(tempFilePaths){
			// 		// 使用uni.uploadFile上传图片至云服务器
			// 		console.log(tempFilePaths)
			// 		const apiUrl = "https://math.rockeyops.com/api/v1/math/solve";
			// 		const header = {
			// 			"x-app-id": "math-app",
			// 			"x-app-key": "7a6c508f25324c3d36c46c409c4f7f2b",
			// 			"Content-Type": "application/json" // Assuming the API expects JSON content type
			// 		};
			// 		const data = {
			// 			stream: false,
			// 			url: tempFilePaths
			// 		};
					
			// 		var that = this
			// 		try {
			// 			uni.showLoading({
			// 				title: "解析中..."
			// 			})
			// 			console.log("开始调用数学题扫描解答")
			// 			const response = await uni.request({
			// 				url: apiUrl,
			// 				method: "POST",
			// 				header: header,
			// 				data: data
			// 			});
			
			// 			if (response.statusCode === 200) {
			// 				console.log("API response:", response.data);
			// 				if (response.data.msg == 'invalid image') {
			// 					uni.showModal({
			// 						title:"太火爆了！",
			// 						content:"请重试一遍",
			// 						showCancel:false,
			// 						success(res) {
			// 							// if (res.confirm) {
			// 							// 	that.analyze_img(tempFilePaths)
			// 							// }
			// 						}
			// 					})
			// 					console.error("Error calling API:", response);
			// 				} else {
			// 					// Process the response data as needed
			// 					this.originalText = response.data.data.content
			// 					// this.startDisplay()
			// 					this.processText();
			// 				}
			// 			}
			// 		} catch (error) {
			// 			console.error("API call failed:", error);
			// 		} finally {
			// 			uni.hideLoading()
			// 		}
					
			// 	},
			
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
</style>
