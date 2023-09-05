<template>
    <view class="content">
		<joMarkdown :nodes="markdownData"></joMarkdown>
		<view @click="click">点击我</view>
	</view>
</template>

<script>
import markdownFunc from '@/uni_modules/jo-markdown/components/jo-markdown/index.js';
import joMarkdown from '@/uni_modules/jo-markdown/components/jo-markdown/decode.vue';
export default {
	components: {
		joMarkdown  // 这里使用了上面导入的名称
	},
	data() {
		return {
			markdownData: {},
			markdown: ``
		};
	},
	onLoad() {
		// 如果 markdownFunc 是一个函数，您需要确保它是正确的，并且 markdown 这个变量在当前作用域中是已定义的。
		// 替换字符串中的单一反斜线为双反斜线
		    this.markdown = this.markdown.replace(/\\/g, '\\\\');
		    
		    console.log(this.markdown);
		this.markdownData = markdownFunc(this.markdown,"markdown");
	},
	methods: {
	click(){
		console.log(this.markdown)
	}
	}
};
</script>

<style>
.test{
		
}
</style>
