<template>
	<div class="common-layout">
		<el-container>
			<el-header><Header></Header></el-header>
			<el-main> <router-view>Main</router-view></el-main>
			<el-footer>Footer</el-footer>
		</el-container>
	</div>
</template>

<script lang="ts" setup name="index">
	import Header from '@/components/Header.vue';
</script>

<style scoped>
	.el-header {
		padding: 0 !important;
	}
</style>
