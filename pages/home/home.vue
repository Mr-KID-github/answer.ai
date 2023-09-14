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
				<custom_input></custom_input>
			</view>
		</view>
					
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
							'question': "",
							'answer': "大家好，我是你的人工智能助手，我可以帮助你完成不同的任务。你可以叫我去写一篇文章，解决数学问题，历史测验的问题和答案等。"
						},
						{
							'question': "帮我写一篇小作文",
							'answer': "当然可以！请问您希望这篇小作文是关于什么主题或内容的呢？如果没有特定的要求，我可以直接为您创作一篇。"
						}
					]
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
				}
			}
	    }
</script>

	
<style>
	.conten_frame{
		width: 322px;
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
		position: relative; /* 添加此行 */
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

</style>
