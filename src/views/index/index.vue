<template>
	<div v-bind:style="{ backgroundImage: 'url(' + bgImage + ')' }" class="common-layout"></div>
	<el-container class="content-container">
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
import request from '@/utils/request';
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
				// 获取背景图片
				const res = await request.get('https://api.vvhan.com/api/wallpaper/pcGirl?type=json');
				bgImage.value = res.data.url;

				// 添加樱花特效
				const script = document.createElement('script');
				// 使用相对路径，从当前文件所在目录开始计算
				script.src = 'yinghua.js';
				document.body.appendChild(script);

				// 10秒后移除特效
				setTimeout(() => {
					// 移除脚本
					if (script.parentNode) {
						script.parentNode.removeChild(script);
					}

					// 清除所有樱花元素
					const sakuraElements = document.querySelectorAll('.sakura');
					sakuraElements.forEach(el => {
						if (el.parentNode) {
							el.parentNode.removeChild(el);
						}
					});

					// 清除所有canvas元素
					const canvasElements = document.querySelectorAll('canvas');
					canvasElements.forEach(canvas => {
						if (canvas.parentNode && canvas.id !== 'defaultCanvas0') {
							canvas.parentNode.removeChild(canvas);
						}
					});
				}, 10000);
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
