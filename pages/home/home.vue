<template>
	<view class="background">
		<view class="title">Answer AI China</view>
		
		<view style="margin-top:20rpx; width: 100%; padding-left: 80rpx; background: transparent; margin-bottom: 60rpx;">
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
			<view v-if="tar_value==0 && cur_tabs=='AI对话'"  style="position: fixed; bottom: 180rpx; background-color: white; border-radius: 200rpx;">
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
	import * as TextEncoding from 'text-encoding-shim';
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
					cur_tabs: 'AI搜题',
					chat_content_list: [
						{
							'content': "大家好，我是你的人工智能助手，我可以帮助你完成不同的任务。",
							"role": "system",
						}
					],
					Receive_data: 0
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
					// this.chat_content_list.push({
					// 	"role": "user",
					// 	"content": data
					// })
					// 将新对象添加到数组中并确保响应性
					 let newItem = {
					       role: "user",
					       content: data
					     };
					 this.chat_content_list.push(newItem);

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
					// console.log("添加后",this.chat_content_list.length)
					const requestTask = uni.request({
						enableChunked:true,  // 开启分片模式
						url: getApp().globalData.server + '/ask_chat',
						method: 'POST',
						data: JSON.stringify(this.chat_content_list),
						header: {
							'content-type': 'application/json' // 设置请求的 header
						},
						success: (res) => {
							this.Receive_data = 0			// 接收数据完毕
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
						if (!this.Receive_data) {
							// 是否正在接收数据
							this.chat_content_list.push({
								"role": "assistant",
								"content": ""
							})
						}
						this.Receive_data = 1			// 正在接收数据
					    // 接收分片的数据
						// 使用TextDecoder将Uint8Array转换为字符串
						// const textChunk = new TextDecoder().decode(chunk.data);
						// console.log(`接收分片的数据 (大小：${textChunk.length} 字符):\n${textChunk}`);
						// 这里处理和渲染你的数据
						// this.handleChunk(chunk);
						 const uint8Array = new Uint8Array(chunk.data);
						const str = new TextEncoding.TextDecoder('utf-8').decode(uint8Array);
						// 看一下 打印出来的结果
						console.log(str)
						// 调用 handleChunk 处理每个分片
					    this.handleChunk(str);
						
					})
				},
				handleChunk(chunk) {
					// 添加新数据到累积数据
					accumulatedData += chunk;
				
					// 正则表达式用来找到 'data: {' 开始的JSON对象
					const jsonStartRegex = /data: \{/;
				
					let tryParseJson = (data) => {
						try {
							return JSON.parse(data);
						} catch (e) {
							return null;
						}
					};
				
					// 用来累积可能的 JSON 片段
					let jsonBuffer = '';
					let bracketCount = 0;
				
					for (let i = 0; i < accumulatedData.length; i++) {
						const char = accumulatedData[i];
						jsonBuffer += char;
				
						if (char === '{') {
							bracketCount++; // 找到一个未匹配的左花括号
						} else if (char === '}') {
							bracketCount--; // 找到一个匹配的右花括号
						}
				
						// 检查是否有完整的 JSON 对象
						if (bracketCount === 0 && jsonBuffer.trim().match(jsonStartRegex)) {
							// console.log("jsonBuffer",jsonBuffer)
							// 去除 'data: ' 前缀，并尝试解析JSON
							const jsonData = tryParseJson(jsonBuffer.trim().substring(6));
							
							if (jsonData) {
								// 如果解析成功，处理数据
								this.processData(jsonData);
								// 清空 JSON 缓冲区，准备接收新的 JSON 对象
								jsonBuffer = '';
							} else {
								// 如果解析失败，保留数据直到下一个完整的JSON对象
								continue;
							}
						}
					}
				
					// 如果花括号计数不为 0（即 JSON 数据不完整），保留累积的数据
					if (bracketCount !== 0) {
						// 保存不完整的JSON对象到累积数据
						accumulatedData = jsonBuffer;
					} else {
						// 如果所有 JSON 对象都已处理完毕，重置累积数据
						accumulatedData = '';
					}
				},


				processData(parsedData) {
				    console.log(this.chat_content_list);
					console.log("length",this.chat_content_list.length)
				    if (parsedData.type === 0 && parsedData.text && parsedData.text.content) {
				        // 获取数组的最后一个元素的索引
				        let lastIndex = this.chat_content_list.length - 1;
				        console.log("lastIndex",lastIndex)
				        // 检查确保最后一个元素存在
				        if (lastIndex >= 0) {
							// console.log(this.chat_content_list[lastIndex].content)
				            
							setTimeout(() => {
								// 修改数组中对象的属性并确保响应性
								this.$set(this.chat_content_list[lastIndex], 'content', this.chat_content_list[lastIndex].content + parsedData.text.content);
							}, 500);  // 200毫秒延迟逐字显示
				        }
				    } else if (parsedData.type === 1 && parsedData.ext) {
				        console.log("Received status message:", parsedData.ext);
				    }
				},
				// appendCharacterToDisplay(content) {
				//     // 你的逐字符渲染逻辑，例如更新文本框或其他UI元素
				// 	console.log("逐字符渲染",content)
				// }

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
		padding-bottom: 300rpx;
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
