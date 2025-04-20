<template>
	<!-- 推荐位 -->
	<p style="text-align: center; margin: 0">{{ text }}</p>
	<div style="padding: 16px 2vw">
		<el-carousel height="400px" direction="vertical" type="card" :autoplay="true">
			<el-carousel-item v-for="image in imageInfo" :key="image.id">
				<div style="position: relative; height: auto">
					<p style="
							position: absolute;
							top: 10px;
							left: 10px;
							background-color: transparent;
							font-size: 10px;
							color: white;
							margin: 0;
						">
						{{ image.title }}
					</p>
					<img :src="image.url" style="height: auto" />
				</div>
			</el-carousel-item>
		</el-carousel>
	</div>

	<ul v-infinite-scroll="load" class="infinite-list" style="overflow: auto" infinite-scroll-distance="10px">
		<li v-for="i in count" :key="i" class="infinite-list-item">
			<el-card shadow="hover" style="width: 100%">
				<template #header>
					<span>推文name+时间</span>
				</template>
				<div v-for="o in 4" :key="o" class="text item">
					{{ '内容 ' + o }}
				</div>
				<template #footer>备注:无</template>
			</el-card>
		</li>
	</ul>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';


// 初始化为可以存放图片信息的数组
const imageInfo = ref([]);

//获取图片信息
const fetchImage = async () => {
	const response = await axios.get(
		'https://api.vvhan.com/api/bing?size=1078x480&rand=sj&type=json'
	);
	if (response.data.success) {
		return {
			id: response.data.data.date,
			url: response.data.data.url,
			title: response.data.data.title,
		};
	} else {
		console.error('Failed to fetch image:', response.data);
		return {
			id: '',
			url: '',
			title: '',
		};
	}
};

onMounted(async () => {
	// 并发五次请求
	const fetches = Array.from({ length: 5 }, () => fetchImage());
	const images = await Promise.all(fetches);
	// 将返回的图片信息赋值给imageInfo
	imageInfo.value = images;
});

const text = ref('');

onMounted(async () => {
	const response = await axios.get(
		'https://api.vvhan.com/api/ian/rand?type=json'
	);
	text.value = response.data.data.content + '——  ' + response.data.data.form;
});

//无限滚动count.value += 10;添加一个+号
const count = ref(0);
const load = () => {
	count.value = 4;
};
</script>
<style scoped>
.el-carousel__item h3 {
	color: #475669;
	opacity: 0.75;
	line-height: 200px;
	margin: 0;
	text-align: center;
}

.el-carousel__item:nth-child(2n) {
	background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n + 1) {
	background-color: #d3dce6;
}

/* 滚动 */
.infinite-list {
	height: 650px;
	padding: 0;
	margin: 0;
	overflow-x: hidden !important;
	overflow-y: auto !important;
	list-style: none;
}

.infinite-list::-webkit-scrollbar {
	display: none;
}

.infinite-list .infinite-list-item {
	display: flex;
	align-items: center;
	justify-content: center;
	height: auto;
	background: var(--el-color-primary-light-9);
	margin: 10px;
	color: var(--el-color-primary);
}

.infinite-list .infinite-list-item+.list-item {
	margin-top: 10px;
}
</style>
