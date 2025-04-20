<template>
	<div v-bind:style="{ backgroundImage: 'url(' + bgImage + ')' }" class="common-layout"></div>
	<el-container class="content-container">
		<el-affix :offset="1">
			<div style="width: 65px; display: flex; justify-content: space-around">
				<div class="vertical-line"></div>
			</div>
			<router-link to="/publishpage">
				<el-button type="success" circle><svg t="1709092972785" class="icon" viewBox="0 0 1024 1024"
						version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="1476" width="16" height="16">
						<path
							d="M799.288889 641.28a32.455111 32.455111 0 0 0-45.511111 0L658.631111 728.177778a32.455111 32.455111 0 0 0 0 45.511111 32.455111 32.455111 0 0 0 45.511111 0l33.080889-33.109333V955.733333c0 20.679111 12.430222 33.109333 33.109333 33.109334 20.679111 0 33.080889-12.430222 33.080889-33.109334v-211.000889l33.109334 33.080889a32.455111 32.455111 0 0 0 45.511111 0 32.455111 32.455111 0 0 0 0-45.511111l-82.744889-91.022222z"
							fill="#000000" p-id="1477"></path>
						<path
							d="M935.822222 260.664889L687.587556 12.401778C679.310222 4.152889 675.157333 0 662.755556 0H191.089778C129.024 0 83.512889 45.511111 83.512889 107.576889v781.937778c0 62.094222 45.511111 107.605333 107.576889 107.605333h376.519111v-70.343111H191.089778c-20.679111 0-37.233778-12.430222-37.233778-37.262222V107.605333c0-20.679111 12.401778-37.262222 37.262222-37.262222h401.294222v211.029333c0 37.233778 33.109333 70.343111 70.343112 70.343112h211.000888v182.044444h70.343112V281.315556c4.124444-8.277333 0-16.554667-8.277334-20.679112z m-273.066666 24.803555V86.897778l198.599111 198.570666H662.755556z"
							fill="#000000" p-id="1478"></path>
						<path
							d="M493.112889 376.490667c20.707556 0 33.109333-12.401778 33.109333-37.233778 0-20.679111-12.401778-37.233778-33.109333-37.233778h-235.804445c-20.707556 0-33.109333 12.430222-33.109333 37.262222 0 20.679111 12.401778 37.205333 33.080889 37.205334h235.832889zM261.404444 542.008889h508.928c20.679111 0 37.233778-12.430222 37.233778-37.262222 0-20.679111-12.401778-37.233778-37.262222-37.233778H261.461333c-20.679111 0-37.262222 12.430222-37.262222 37.262222 4.152889 24.803556 16.583111 37.233778 37.262222 37.233778z"
							fill="#000000" p-id="1479"></path>
					</svg></el-button></router-link>
		</el-affix>
		<el-header>
			<Header></Header>
		</el-header>
		<el-main style="padding: 20px 1vw 0; overflow: visible" v-bind:style="{ display: elMainAndFooterDisplay }">
			<div style="display: flex">
				<Tool></Tool>
				<router-view></router-view>
				<Amusement></Amusement>
			</div>
		</el-main>
		<el-footer v-bind:style="{ display: elMainAndFooterDisplay }">
			<Footer></Footer>
		</el-footer>
	</el-container>
	<el-backtop :right="100" :bottom="100" />
</template>

<script>
import { computed, ref, onMounted, defineComponent } from 'vue';
import { useStore } from 'vuex';
import axios from 'axios';
import Header from '@/components/Header.vue';
import Footer from '../Footer/footer.vue';
import Tool from '../Amusement-ad/ad/tool.vue';
import Amusement from '../Amusement-ad/amusement/amusement.vue';

export default defineComponent({
	name: 'Index',
	components: {
		Header,
		Footer,
		Tool,
		Amusement
	},
	setup() {
		let bgImage = ref('');

		onMounted(async () => {
			try {
				const res = await axios.get(
					'https://api.vvhan.com/api/wallpaper/pcGirl?type=json'
				);
				bgImage.value = res.data.url;
			} catch (error) {
				console.error(error);
			}
		});

		const store = useStore();

		let elMainAndFooterDisplay = computed(() => {
			if (!store.state.showContent) {
				return 'none';
			} else {
				return '';
			}
		});

		return {
			bgImage,
			elMainAndFooterDisplay
		};
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

.content-container:deep(.el-affix) {
	display: flex !important;
	flex-direction: row-reverse !important;
}

.content-container:deep(.el-affix--fixed) {
	width: 370px !important;
	display: flex;
	flex-direction: column;
	align-items: center;
}

.vertical-line {
	width: 1px;
	height: 80px;
	/* 设置垂直线的长度 */
	border-left: 1px dashed rgb(255, 255, 255);
	/* 设置垂直线的颜色和边框样式 */
}
</style>
