<template>
	<div
		v-bind:style="{ backgroundImage: 'url(' + bgImage + ')' }"
		class="common-layout"
	></div>
	<el-container class="content-container">
		<el-header><Header></Header></el-header>
		<el-main
			style="padding: 20px 1vw 0; overflow: visible"
			v-bind:style="{ display: elMainAndFooterDisplay }"
		>
			<div style="display: flex">
				<Tool></Tool>
				<router-view></router-view>
				<Amusement></Amusement>
			</div>
		</el-main>
		<el-footer v-bind:style="{ display: elMainAndFooterDisplay }"
			><Footer></Footer
		></el-footer>
	</el-container>
</template>

<script lang="ts" setup>
	import Header from '@/components/Header.vue';
	import Footer from '../Footer/footer.vue';
	import Tool from '../Amusement-ad/ad/tool.vue';
	import Amusement from '../Amusement-ad/amusement/amusement.vue';
	import { computed, ref, onMounted } from 'vue';
	import { useStore } from 'vuex';
	import type { State } from '../../store/index.ts'; // 使用 import type 导入 State 类型
	import axios from 'axios';

	let bgImage = ref('');

	onMounted(async () => {
		try {
			const res = await axios.get('https://api.vvhan.com/api/girl?type=json');
			bgImage.value = res.data.imgurl;
		} catch (error) {
			console.error(error);
		}
	});

	const store = useStore() as { state: State }; // 强制类型转换 store

	// 创建一个计算样式的计算属性
	let elMainAndFooterDisplay = computed(() => {
		if (!store.state.showContent) {
			// 如果 showContent 为 false，则设为 'none'
			return 'none';
		} else {
			// 否则不设置 display
			return '';
		}
	});
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
	.common-layout {
		position: fixed;
		top: 0;
		left: 0;
		width: 100%;
		height: 100vh;
		z-index: -1;
		background-repeat: no-repeat;
		background-size: cover;
		background-position: top;
	}
	.content-container {
		position: relative;
		z-index: 1;
		height: 100vh;
		overflow: auto;
	}

	.el-container {
		overflow: visible !important;
	}
</style>
