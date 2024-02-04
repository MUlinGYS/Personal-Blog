<template>
	<div id="app">
		<Header></Header>
		<router-view v-slot="{ Component }">
			<keep-alive>
				<component :is="Component" />
			</keep-alive>
		</router-view>
	</div>
</template>

<script lang="ts">
	import Header from '../src/components/Header.vue';
	export default {
		name: 'App',
		components: {
			Header,
		},
	};
</script>

<style>
	body,
	.app {
		margin: 20px 20px 0 20px;
	}
</style>
