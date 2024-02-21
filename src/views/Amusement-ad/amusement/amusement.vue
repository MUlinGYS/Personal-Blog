<template>
	<div style="width: 10%; margin-top: 40px">
		<!-- 抽屉按钮 -->
		<el-button
			type="info"
			round
			style="margin-left: 16px"
			@click="drawer = true"
		>
			摸鱼人日历
		</el-button>
		<!-- 抽屉 -->
		<el-drawer
			v-model="drawer"
			:with-header="false"
		>
			<img src="https://api.vvhan.com/api/moyu" />
		</el-drawer>
		<el-empty description="娱乐位" />
	</div>
</template>
<script setup lang="ts">
	import { ref } from 'vue';
	const drawer = ref(false);
</script>

<style>
	.el-drawer {
		width: auto !important;
	}
	.el-drawer__body {
		overflow: hidden !important;
		padding: 0 !important;
	}
</style>
