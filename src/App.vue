<template>
	<router-view v-slot="{ Component }">
		<keep-alive>
			<component :is="Component" />
		</keep-alive>
	</router-view>
</template>

<script>
export default {
	name: 'App',
	components: {},
};
</script>

<style>
/* 隐藏整个页面的滚动条 */
html,
body {
	scrollbar-width: none;
	/* Firefox */
	-ms-overflow-style: none;
	/* IE and Edge */
}

/* 隐藏WebKit浏览器(Chrome, Safari)的滚动条 */
html::-webkit-scrollbar,
body::-webkit-scrollbar {
	display: none;
}
</style>
