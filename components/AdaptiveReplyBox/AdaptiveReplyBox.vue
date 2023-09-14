<template>
	<view class="frame">
		<text>{{content}}</text>
	</view>
</template>

<script>
	export default {
		name:"AdaptiveReplyBox",
		props:['content'],
		data() {
			return {
				
			};
		}
	}
</script>

<style>
.frame{
	display: inline-flex;
	padding: 10px;
	justify-content: center;
	align-items: center;
	gap: 10px;
	
	border-radius: 10px;
	background: #D9D9D9;
}
.frame text{
	color: #000;
	font-family: ABeeZee;
	font-size: 17px;
	font-style: normal;
	font-weight: 400;
	line-height: 16px; /* 94.118% */
	max-width: 250px;
}
</style>