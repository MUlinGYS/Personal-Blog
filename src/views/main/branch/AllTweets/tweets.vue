<template>
	<!-- 推荐位 -->
	<div style="padding: 2vw">
		<el-carousel
			height="400px"
			direction="vertical"
			type="card"
			:autoplay="true"
		>
			<el-carousel-item
				v-for="image in imageInfo"
				:key="image.id"
			>
				<div style="position: relative; height: auto">
					<p
						style="
							position: absolute;
							top: 10px;
							left: 10px;
							background-color: transparent;
							font-size: 10px;
							color: white;
							margin: 0;
						"
					>
						{{ image.title }}
					</p>
					<img
						:src="image.url"
						style="height: auto"
					/>
				</div>
			</el-carousel-item>
		</el-carousel>
	</div>

	<el-card shadow="hover">
		<template #header>
			<span>推文name</span>
		</template>
		<div
			v-for="o in 4"
			:key="o"
			class="text item"
		>
			{{ '内容 ' + o }}
		</div>
		<template #footer>其他内容</template>
	</el-card>
</template>

<script setup lang="ts">
	import { ref, onMounted } from 'vue';
	import axios from 'axios';

	interface ImageInfo {
		id: string;
		url: string;
		title: string;
	}

	// 初始化为可以存放图片信息的数组
	const imageInfo = ref<ImageInfo[]>([]);

	//获取图片信息
	const fetchImage = async (): Promise<ImageInfo> => {
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
</style>
