<template>
	<div class="common-layout">
		<el-container>
			<el-header><Header></Header></el-header>
			<el-main> <router-view></router-view></el-main>
			<el-footer><Footer></Footer></el-footer>
		</el-container>
	</div>
</template>

<script lang="ts" setup name="index">
	import Header from '@/components/Header.vue';
	import Footer from '../Footer/footer.vue';
</script>

<style scoped>
	.el-header {
		padding: 0 !important;
		height: auto;
	}
	.el-footer {
		padding: 0 !important;
		height: auto;
	}
</style>
