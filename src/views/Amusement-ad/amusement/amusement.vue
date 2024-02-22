<template>
	<div
		style="width: 10%; margin-top: 40px; display: flex; flex-direction: column"
	>
		<!-- 抽屉按钮 -->
		<el-button
			round
			style="margin: 16px 0; background-color: rgba(230, 193, 199, 0.774)"
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

		<el-card
			class="box-card"
			v-if="music.picUrl"
		>
			<img
				:src="music.picUrl"
				class="music-cover"
			/>
			<div class="music-info">
				<h1 class="music-title">{{ music.name }}</h1>
				<h2 class="music-auther">{{ music.auther }}</h2>
			</div>
			<el-button
				circle
				@click="togglePlay"
				><el-icon><SwitchButton /></el-icon
			></el-button>
		</el-card>
		<el-empty description="娱乐位" />
	</div>
</template>
<script setup lang="ts">
	import { ref, onMounted } from 'vue';
	import axios from 'axios';

	const drawer = ref(false);
	const music = ref({
		picUrl: '',
		name: '',
		auther: '',
		mp3url: '',
	});
	let audio = new Audio();

	// 抽取成单独的函数方便复用
	const fetchMusic: () => Promise<void> = async () => {
		const response = await axios.get(
			'https://api.vvhan.com/api/rand.music?type=json&sort=%E6%96%B0%E6%AD%8C%E6%A6%9C'
		);
		const fetchedMusic = response.data.info;

		// 检查歌曲信息长度
		if (fetchedMusic.name.length > 7 || fetchedMusic.auther.length > 7) {
			// 如果长度超出，重新调用本函数
			await fetchMusic();
			return;
		}

		// 格式合适则将歌曲信息赋值到 music
		music.value = fetchedMusic;
		audio.src = music.value.mp3url;
	};

	onMounted(fetchMusic);

	const togglePlay = () => {
		if (audio.paused) {
			audio.play();
		} else {
			audio.pause();
		}
	};
</script>

<style lang="less" scoped>
	.el-drawer {
		width: auto !important;
	}
	.el-drawer__body {
		overflow: hidden !important;
		padding: 0 !important;
	}
	.el-card {
		width: auto;
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
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
	.el-card {
		padding: 10px !important;
	}
</style>
