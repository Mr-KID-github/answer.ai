<template>
	<view class="background">
		<view class="title">Answer AI China</view>
		
		<view style="margin-top:10px; width: 100%; padding-left: 40px; background: transparent; margin-bottom: 30px;">
			<u-tabs :list="list1"  @click="click_tabs"></u-tabs>
		</view>
		<conten_frame></conten_frame>
		<view class="conten_frame">
			<view v-if="tar_value==0">
				<view v-if="cur_tabs=='AI搜题'">
					<home_component></home_component>
				</view>
				<view v-if="cur_tabs=='AI对话'">
					<AI_Chat :chat_content_list="chat_content_list"></AI_Chat>
				</view>
			</view>
			
			<view v-else-if="tar_value==1">
				<mine></mine>
			</view>
			<view v-if="tar_value==0 && cur_tabs=='AI对话'"  style="position: fixed; bottom: 100px;">
				<custom_input @click_ask="handleAskData"></custom_input>
			</view>
		</view>
		
		<view>{{answer}}</view>
					
		<!-- 底部 -->			
		<view class="bottom-section">
			<!-- 底部导航栏 -->
			<u-tabbar
				:value="tar_value"
				@change="name => tar_value = name"
				:fixed="true"
				:placeholder="true"
				:safeAreaInsetBottom="true"
			>
				<u-tabbar-item text="首页" icon="home" @click="click_tabbar"></u-tabbar-item>
				<u-tabbar-item text="我的" icon="account" @click="click_tabbar"></u-tabbar-item>
			</u-tabbar>
		</view>
	</view>
</template>

<script>
	let accumulatedData = "";  // 用于累积从chunk接收到的数据
	 export default {
	        data() {
	            return {
	                list1: [{
						name: 'AI搜题'
					},
					{
						name: 'AI对话'
					}],
					tar_value: 0,
					cur_tabs: 'AI对话',
					chat_content_list: [
						{
							'content': "大家好，我是你的人工智能助手，我可以帮助你完成不同的任务。",
							"role": "system",
						},
						{
							'content': "帮我写一篇小作文",
							'role': "user"
						},
						{
							'role': "assistant",
							'content': "当然可以！请告诉我你想要什么类型？"
						}
					],
			
	            }
	        },
			onLoad() {
				
			},
			methods: {
				click_tabbar(res) {
					// console.log(res)
				},
				click_tabs(res){
					// console.log(res.name)
					this.cur_tabs = res.name
				},
				// 处理提问框提出问题
				handleAskData(data){
					console.log("处理提问框提出问题：",data)
					// 将其添加到深入提问数组
					this.chat_content_list.push({
						"role": "user",
						"content": data
					})
					console.log("将提问框提出问题放入数组中",this.chat_content_list)
					
					uni.showLoading({
						title:"提问中..."
					})
					
					this.callGPTApi((response) => {
						console.log(response);
					});
				},
				// AI对话接口
				callGPTApi(payload,callback) {
				    console.log("调用GPT接口")
					
					const requestTask = uni.request({
						enableChunked:true,  // 开启分片模式
						url: getApp().globalData.server + '/ask_chat',
						method: 'POST',
						data: JSON.stringify(this.chat_content_list),
						header: {
							'content-type': 'application/json' // 设置请求的 header
						},
						success: (res) => {
							this.chat_content_list.push({
								"role": "assistant",
								"content": ""
							})
							 console.log('Request completed', res);
						},
						fail: (err) => {
							console.error('Request failed:', err);
						},
						complete() {
							uni.hideLoading()
						}
					})
					requestTask.onChunkReceived((chunk)=>{
					    // 接收分片的数据
						// 使用TextDecoder将Uint8Array转换为字符串
						const textChunk = new TextDecoder().decode(chunk.data);
						console.log(`接收分片的数据 (大小：${textChunk.length} 字符):\n${textChunk}`);
						// 这里处理和渲染你的数据
						// this.handleChunk(chunk);
					})
				},
				handleChunk(response) {
					let chunk = response.data;
					let decoder = new TextDecoder('utf-8');
					let decodedString;

					try {
						decodedString = decoder.decode(chunk);
					} catch (error) {
						console.error("Error while decoding chunk:", error);
						return;
					}

					accumulatedData += decodedString;

					// 循环处理完整的消息
					while (true) {
						let startPos = accumulatedData.indexOf("data: ");
						let endPos = accumulatedData.indexOf("\n\n", startPos);

						if (startPos !== -1 && endPos !== -1) {
							let jsonString = accumulatedData.substring(startPos + 6, endPos).trim();
							let parsedData;

							try {
								parsedData = JSON.parse(jsonString);
								let content = parsedData.text.content;

								// 显示解析后的内容
								this.chat_content_list[-1].content += content
								console.log("显示解析后的内容",this.chat_content_list[-1].content)
								console.log(this.chat_content_list)
								// 清除已处理的数据
								accumulatedData = accumulatedData.substring(endPos + 2);
							} catch (e) {
								console.error("Failed to parse JSON:", e);
								break;
							}
						} else {
							break;
						}
					}
				},
				appendCharacterToDisplay(content) {
				    // 你的逐字符渲染逻辑，例如更新文本框或其他UI元素
					console.log("逐字符渲染",content)
					
				}

			}
	    }
</script>

	
<style>
	.conten_frame{
		width: 644rpx;
		align-items: flex-start;
		gap: 40rpx;
		
		display: flex;
		flex-direction: column;
		align-items: center;
		padding-top: 100rpx;
		flex-shrink: 0;
		border-radius: 40rpx 40rpx 0rpx 0rpx;
		background: #FFF;
		
		margin-top: auto;
		width: 100%;
		flex: 1;  /* 这使得它能够自动扩展并占据所有剩余空间 */
		padding-bottom: 80rpx;
		position: relative; /* 添加此行 */
	}
.background{
	display: flex;
	align-items: center;
	flex-direction: column;
	padding-top: 40rpx;
	
	width: 100vw;
	height: 100vh;
	flex-shrink: 0;
	background: radial-gradient(circle, #8055FC, rgba(128, 85, 252, 0.00));
}
.title{
	color: #000;
	font-family: Inter;
	font-size: 24rpx;
	font-style: normal;
	font-weight: 700;
	line-height: normal;
}

</style>
