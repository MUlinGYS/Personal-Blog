<template>
	<el-tabs v-model="activeName" type="card" class="demo-tabs" :stretch="true" style="width: 80%; padding: 0 1vw">
		<el-tab-pane label="首页" name="first" :lazy="true">
			<Tweets></Tweets>
		</el-tab-pane>
		<el-tab-pane label="资源链接" name="second" :lazy="true">
			<Resource></Resource>
		</el-tab-pane>
		<el-tab-pane label="技术锦囊" name="third" :lazy="true">
			<Tips></Tips>
		</el-tab-pane>
		<el-tab-pane label="归档" name="fourth" :lazy="true">
			<Pigeonhole></Pigeonhole>
		</el-tab-pane>
	</el-tabs>
</template>
<script setup name="main">
import Tweets from './components/branch/AllTweets/tweets.vue';
import Pigeonhole from './components/branch/pigeonhole/pigeonhole.vue';
import Resource from './components/branch/resource/resource.vue';
import Tips from './components/branch/Tips/Tips.vue';
import { ref } from 'vue';
// import type { TabsPaneContext } from 'element-plus';

const activeName = ref('first');

// const handleClick = (tab: TabsPaneContext, event: Event) => {
// 	console.log(tab, event);
// };
</script>
<style scoped>
.demo-tabs>.el-tabs__content {
	padding: 32px;
	color: #6b778c;
	font-size: 32px;
	font-weight: 600;
}

.demo-tabs>.el-tabs__content {
	padding: 0 !important;
}

:deep(.el-tabs__header) {
	border-radius: 7px;
	box-shadow: inset 0 0 50px rgb(255, 255, 255);
}

:deep(.el-tabs__item) {
	border-bottom: 10px !important;
}

:deep(.el-tabs__nav) {
	border-radius: 7px !important;
}

:deep(.el-tabs__item.is-active) {
	color: rgb(0, 57, 163) !important;
}

:deep(.el-tabs__item:hover) {
	color: rgb(135, 132, 132);
}
</style>
