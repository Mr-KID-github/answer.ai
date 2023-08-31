<template>
	<view class="frame">
		<view class="title">设置</view>
		<navigation_component title='历史记录' @NavigationClicked="HandleHistoryClick"></navigation_component>
<!-- 		<navigation_component title='加入社群' @NavigationClicked="HandleJoinCommunityClick"></navigation_component>
	 -->
		<u-popup :show="ShowPopup" mode="center" :round="10" zoom @close="ClosePopup" @open="OpenPopup">
			<view>
				<text>人生若只如初见，何事秋风悲画扇</text>
			</view>
		</u-popup>
	</view>
</template>

<script>
	export default {
		name:"mine",
		data() {
			return {
				ShowPopup: false
			};
		},
		methods:{
			OpenPopup() {
				// console.log('open');
			  },
			  ClosePopup() {
				this.ShowPopup = false
				// console.log('close');
			  },
			HandleHistoryClick(e){
				console.log("点击",e)
				uni.showModal({
					title:"还在开发中...",
					content:"你想要这个功能吗？",
					cancelText:"并不想",
					confirmText:"超级想",
					success: (res) => {
						console.log(res)
					}
				})
			},
			HandleJoinCommunityClick(e){
				console.log("点击",e)
				this.ShowPopup = true
			}
		}
	}
</script>

<style>
.frame{
	display: inline-flex;
	flex-direction: column;
	align-items: flex-start;
	gap: 20px;
}
.title{
	color: #8C8B8B;
	text-align: center;
	font-feature-settings: 'clig' off, 'liga' off;
	font-family: ABeeZee;
	font-size: 15px;
	font-style: normal;
	font-weight: 400;
	line-height: normal;
}

</style>