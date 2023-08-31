<template>
	<view class="background">
		<view class="title">Answer AI China</view>
		
		<view style="margin-top:10px; width: 100%; padding-left: 40px; background: transparent; margin-bottom: 30px;">
			<u-tabs :list="list1"></u-tabs>
		</view>
		<conten_frame></conten_frame>
		<view class="conten_frame">
			<view v-if="tar_value==0">
				<home_component></home_component>
			</view>
			
			<view v-else-if="tar_value==1">
				<mine></mine>
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
	                    name: 'AI搜题',
	                }],
					tar_value: 0
	            }
	        },
			onLoad() {
				
			},
			methods: {
				click_tabbar(res) {
					// console.log(res)
				}
			}
	    }
</script>

	
<style>
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

</style>
