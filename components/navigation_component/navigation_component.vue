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
	gap: 17px;
}
.item image{
	width: 10px;
	height: 10px;
	stroke-width: 2px;
	stroke: #000;
}
.item_text{
	color: #000;
	text-align: center;
	font-feature-settings: 'clig' off, 'liga' off;
	font-family: ABeeZee;
	font-size: 15px;
	font-style: normal;
	font-weight: 400;
	line-height: normal;
}
</style>