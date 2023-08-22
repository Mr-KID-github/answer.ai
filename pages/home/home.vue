<template>
	<view class="background">
		<view class="title">Answer AI China</view>
		
		 <u-sticky bgColor="" custom-style="margin-top:10px; width: 100%; padding-left: 40px; background: transparent; margin-bottom: 30px;">
		    <u-tabs :list="list1"></u-tabs>
		</u-sticky>
		
		<view class="conten_frame">
			<view class="button_item">
				<view class="text_frame">
					<text class="text1">拍照搜题</text>
					<text class="text2">扫描并获取作业答案 By AI</text>
				</view>
				<image src="/static/camera.svg"></image>
			</view>
		</view>
		
		<view class="bottom-section">
			<!-- 滚动通知 -->
			<u-notice-bar :text="text1" mode="closable" speed="250" url="/pages/componentsB/tag/tag"></u-notice-bar>
			
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
					text1: '快加入学习群'
	            }
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
