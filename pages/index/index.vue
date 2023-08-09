<template>
	<view class="frame">
		<view class="content">
			<!-- 标题框架:Chat Test -->
			<view class="title_frame">
				<text class="title_1">Math Test</text>
				<text class="title_2">上传题目图片</text>
			</view>
			
			<!-- 使用示例按钮 -->
			<button class="button_example">UpLoad Math Image</button>
			
			<!-- 提问框 -->
			<view class="response_result" :style="gpt_answer?'width: 500rpx;':''">
				<image v-if="!gpt_answer" src="https://s3-alpha-sig.figma.com/img/46b9/ef5f/b5b166af39d5cf7d66c8cda918d6278c?Expires=1690156800&Signature=S8SSJ3JtrxTTwwlF-YFDyacPqAIdvJaOz-b-l4mjgT~~p~Fqhfsqcls~0t~0tiC2hLjTb3HTlJsJo2BcUjmtEfEm-1W0h4dB8dXPDhM5CnqqLl5arNPFYWihsBUvqlboUDI2m~VbkfGit7rS95uRByXHxKL53i9BM1hgRJt~TshEpQBhZJqKf8PzC37Y5EPXpt3VD858dKmhD3U5tHYjzJR0~GwFcwHnACzqDW1V6B-MnrHUZz1eYgeD1A3YvbxyhpZ~~G0CM71hZVOa8WHk39UgvS9v3C9I8Fp-2Xs~RVQlACtsSlIq6MRMgE-t~3iFXkg9qxm~qOcfevrAjXAj9A__&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4"></image>
				<text v-if="gpt_answer">{{gpt_answer}}</text>
			</view>
			
			<!-- 标题框架:Chat Test -->
			<view class="title_frame">
				<text class="title_2">解析题目数据</text>
				<text class="title_2">Hello! It seems like you provided the......</text>
			</view>
				
			<!-- 标题框架:Chat Test -->
			<view class="title_frame">
				<text class="title_1">Chat Test</text>
				<text class="title_2">调用Chat API</text>
			</view>
			
			<!-- 提问框 -->
			<custom_input></custom_input>
			<view class="title_frame">
				<text class="title_2">你好呀！很高兴见到你。我是ChatGPT，有什么我可以帮助你的吗？</text>
			</view>

		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				title: 'Hello'
			}
		},
		onLoad() {

		},
		methods: {

		}
	}
</script>

<style>
	.frame {
		display: flex;
		justify-content: center;
	}
	.content {
		display: inline-flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		gap: 20px;
		margin-top: 25px;
		margin-bottom: 25px;
	}
	.title_frame{
		display: flex;
		width: 343px;
		flex-direction: column;
		align-items: flex-start;
		gap: 12px;
	}
	.title_1{
		color: var(--gray-900, #18181B);
		font-feature-settings: 'clig' off, 'liga' off;
		font-family: Manrope;
		font-size: 22px;
		font-style: normal;
		font-weight: 800;
		line-height: 30px; /* 136.364% */
		letter-spacing: -0.4px;
	}
	.title_2{
		color: var(--gray-600, #52525B);
		font-feature-settings: 'clig' off, 'liga' off;
		font-family: Manrope;
		font-size: 16px;
		font-style: normal;
		font-weight: 500;
		line-height: 24px; /* 150% */
		letter-spacing: -0.4px;
	}
	.button_example{
		/* 布局样式 */
		display: flex;
		width: 343px;
		padding: 10px 24px;
		justify-content: center;
		align-items: center;
		gap: 8px;
		border-radius: 12px;
		background: var(--teal-900, #134E4A);
		/* 字体 */
		color: var(--base-white, #FFF);
		font-feature-settings: 'clig' off, 'liga' off;
		font-family: Manrope;
		font-size: 16px;
		font-style: normal;
		font-weight: 700;
		line-height: 24px; /* 150% */
		letter-spacing: -0.4px;
	}
	.response_result{
			padding: 10px;
			border: 1px solid #ccc;
			border-radius: 10px;
			background-color: #f8f8f8;
	}
	
	.response_result image{
		border-radius: 10px;
	}
</style>
