<template>
	<div id="app">
		<router-view v-slot="{ Component }">
			<keep-alive>
				<component :is="Component" />
			</keep-alive>
		</router-view>
	</div>
</template>

<script lang="ts">
	export default {
		name: 'App',
		components: {},
	};
</script>

<style>
	body {
		margin: 0;
		/* overflow: hidden;页面上下留白滚动 */
	}
</style>
