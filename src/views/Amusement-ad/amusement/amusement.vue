<template>
	<div style="
			width: 10%;
			margin-top: 40px;
			display: flex;
			flex-direction: column;
		">
		<!-- 抽屉按钮 -->
		<el-button round style="
				background-color: transparent;
				margin-top: 11px;
				box-shadow: inset 0 0 50px rgb(255, 167, 167);
			" @click="drawer = true">
			摸鱼人日历
		</el-button>

		<!-- 抽屉 -->
		<el-drawer v-model="drawer" :with-header="false" class="moyu" @click="drawer = false"
			style="background: transparent">
			<div style="display: flex; justify-content: center; align-items: center; height: 100%">
				<img src="https://api.vvhan.com/api/moyu" style="max-width: 100%; max-height: 100%" />
			</div>
		</el-drawer>


	</div>
</template>
<script setup>
import { ref } from 'vue';

const drawer = ref(false);
</script>

<style lang="less" scoped>
:deep(.moyu .el-drawer__body) {
	padding: 0 !important;
	overflow: hidden !important;
}

:deep(.el-card) {
	width: auto;
	display: flex;
	flex-direction: column;
	align-items: center;
	justify-content: center;
	padding: 10px !important;
}

.el-card {
	margin-top: 16px !important;
}

:deep(.el-drawer.rtl) {
	width: auto !important;
}

.music-cover {
	width: 100px;
	height: 100px;
}

.music-info {
	text-align: center;
	margin-bottom: 10px;
}

.music-title {
	margin: 10px 0;
	font-size: 18px;
	white-space: nowrap;
	overflow: hidden;
	text-overflow: ellipsis;
}

.music-auther {
	margin: 5px 0;
	font-size: 14px;
	color: gray;
	white-space: nowrap;
	overflow: hidden;
	text-overflow: ellipsis;
}

.box-card {
	width: auto;
}

.box-card:deep(.el-card__body) {
	display: flex !important;
	flex-direction: column !important;
	align-items: center !important;
	justify-content: center !important;
}

.chouti:deep(.el-card__body) {
	padding: 0 !important;
	height: auto !important;
}
</style>
