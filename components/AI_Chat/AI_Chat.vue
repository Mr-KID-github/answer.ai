<template>
	<view class="frame">
		<block v-for="(item,index) in chat_content_list">
			<AdaptiveReplyBox :content="item.content" v-if="item.role == 'user'"></AdaptiveReplyBox>
			<view class="answer_group" v-if="item.role == 'system' || item.role == 'assistant'">
				<image src="/static/logo.jpg"></image>
				<AdaptiveReplyBox :content="item.content"></AdaptiveReplyBox>
			</view>
		</block>
	</view>
</template>

<script>
	export default {
		name:"AI_Chat",
		props: ['chat_content_list'],
		data() {
			return {
				
			};
		}
	}
</script>

<style>
	.frame{
		width: 668rpx;
		display: inline-flex;
		flex-direction: column;
		align-items: flex-end;
		gap: 50rpx;
	}
.answer_group{
	display: flex;
	align-items: flex-start;
	gap: 28rpx;
	width: 100%;
}
.answer_group image{
	width: 80rpx;
	height: 80rpx;
	border-radius: 40rpx;
}
</style>