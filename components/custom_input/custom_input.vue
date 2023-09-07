<template>
	<view>
		<u-input
				type="text"
			    placeholder="输入提问"
			    prefixIconStyle="font-size: 22px;color: #909399"
				shape="circle"
				customStyle="width: 550rpx; padding:10rpx; padding-left:50rpx; padding-right:50rpx;height:60rpx"
				confirmType="send"
				v-model="ask_value"
				@change="change"
		>
			<template slot="suffix">
				<image src="/static/submit.png" style="width:50rpx; height:50rpx;" @click="send_message"></image>
			</template>
		</u-input>
	</view>
</template>

<script>
	export default {
		name:"custom_input",
		data() {
			return {
				ask_value: ""
			};
		},
		methods:{
			change(res){
				// console.log(res)
			},
			 send_message() {
				// 在这里执行你的方法
				console.log('发送给前端......');
				this.$emit('click_ask',this.ask_value)
			},
		
		}
	}
</script>

<style>

</style>