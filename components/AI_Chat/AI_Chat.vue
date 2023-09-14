<template>
	<view class="frame">
		<block v-for="(item,index) in chat_content_list">
			<AdaptiveReplyBox :content="item.question" v-if="item.question"></AdaptiveReplyBox>
			<view class="answer_group" v-if="item.answer">
				<image src="/static/logo.jpg"></image>
				<AdaptiveReplyBox :content="item.answer"></AdaptiveReplyBox>
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
		width: 334px;
		display: inline-flex;
		flex-direction: column;
		align-items: flex-end;
		gap: 25px;
	}
.answer_group{
	display: flex;
	align-items: flex-start;
	gap: 14px;
}
.answer_group image{
	width: 40px;
	height: 40px;
	border-radius: 20px;
}
</style>