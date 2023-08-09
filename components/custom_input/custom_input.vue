<template>
	<view>
		<u-input
				type="text"
			    placeholder="询问孩子情况"
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
		props:["content"],
		methods:{
			change(res){
				// console.log(res)
			},
			 send_message() {
				// 在这里执行你的方法
				console.log('发送给chatgpt......');
				// console.log(this.content)
				// console.log(this.ask_value)
				var ask_message = `小孩子的话语:${this.content}\n我的问题:${this.ask_value}`
				// console.log(ask_message)
				this.ask_chatGPT(ask_message)
			},
			ask_chatGPT(ask_message){
				uni.showLoading({
					title:"稍等片刻..."
				})
				uni.request({
				    url: 'https://www.withtime.site/chat', // 你的Flask API接口地址
				    method: 'POST',
				    data: {
				        message: ask_message
				    },
				    header: {
				        'content-type': 'application/json'
				    },
				    success: (res) => {
				        console.log(res.data);
						this.$emit('get_gpt_answer',res.data)
						uni.hideLoading()
				    },
				    fail: (err) => {
				        console.error(err);
				    }
				});
			}
		}
	}
</script>

<style>

</style>