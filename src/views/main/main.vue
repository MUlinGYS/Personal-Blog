<template>
	<el-tabs
		v-model="activeName"
		type="card"
		class="demo-tabs"
		style="width: 80%; padding: 0 1vw"
		@tab-click="handleClick"
	>
		<el-tab-pane
			label="首页"
			name="first"
			><Tweets></Tweets
		></el-tab-pane>
		<el-tab-pane
			label="资源链接"
			name="second"
			><Resource></Resource
		></el-tab-pane>
		<el-tab-pane
			label="技术锦囊"
			name="third"
			><Tips></Tips
		></el-tab-pane>
		<el-tab-pane
			label="归档"
			name="fourth"
			><Pigeonhole></Pigeonhole
		></el-tab-pane>
	</el-tabs>
</template>
<script lang="ts" setup name="main">
	import Tweets from './branch/AllTweets/tweets.vue';
	import Pigeonhole from './branch/pigeonhole/pigeonhole.vue';
	import Resource from './branch/resource/resource.vue';
	import Tips from './branch/Tips/Tips.vue';
	import { ref } from 'vue';
	import type { TabsPaneContext } from 'element-plus';

	const activeName = ref('first');

	const handleClick = (tab: TabsPaneContext, event: Event) => {
		console.log(tab, event);
	};
</script>
<style scoped>
	.demo-tabs > .el-tabs__content {
		padding: 32px;
		color: #6b778c;
		font-size: 32px;
		font-weight: 600;
	}

	.demo-tabs > .el-tabs__content {
		padding: 0 !important;
	}
</style>
