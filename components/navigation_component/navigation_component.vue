<template>
	<view>
		<view class="item" @click="this.$emit('NavigationClicked', title)">
			<view style="display: flex;align-items: center;gap: 203px;">
				<view class="item_text">{{title}}</view>
				<image src="/static/Rectangle_2.svg"></image>
			</view>
			<u-line></u-line>
		</view>
	</view>
</template>

<script>
	export default {
		name:"navigation_component",
		props:['title'],
		data() {
			return {
				
			};
		}
	}
</script>

<style>
.item{
	display: flex;
	flex-direction: column;
	align-items: center;
	gap: 34rpx;
}
.item image{
	width: 20rpx;
	height: 20rpx;
	stroke-width: 4rpx;
	stroke: #000;
}
.item_text{
	color: #000;
	text-align: center;
	font-feature-settings: 'clig' off, 'liga' off;
	font-family: ABeeZee;
	font-size: 30rpx;
	font-style: normal;
	font-weight: 400;
	line-height: normal;
}
</style>