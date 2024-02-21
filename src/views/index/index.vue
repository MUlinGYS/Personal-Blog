<template>
	<div class="common-layout">
		<el-container>
			<el-header><Header></Header></el-header>
			<el-main style="padding: 20px 1vw 0"
				><div style="display: flex">
					<Tool></Tool>
					<router-view></router-view>
					<Amusement></Amusement>
				</div>
			</el-main>
			<el-divider border-style="dashed" />
			<el-footer><Footer></Footer></el-footer>
		</el-container>
	</div>
</template>

<script lang="ts" setup name="index">
	import Header from '@/components/Header.vue';
	import Footer from '../Footer/footer.vue';
	import Tool from '../Amusement-ad/ad/tool.vue';
	import Amusement from '../Amusement-ad/amusement/amusement.vue';
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
