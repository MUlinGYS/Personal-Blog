<template>
	<div
		class="headerimg"
		:style="headerImageClass"
	>
		<Menu></Menu>
		<div
			:style="{
				width: '100vw',
				height: isHidden ? 'calc(100% - 60px)' : '0',
				display: 'flex',
				justifyContent: 'center',
				alignItems: 'center',
			}"
		>
			<!-- 如果 isHidden 为 true, 就隐藏 <img> -->
			<img
				v-if="isHidden"
				class="rotate"
				src="../assets/img/avatar.jpeg"
			/>
		</div>
	</div>
</template>

<script setup lang="ts" name="Header">
	import Menu from '@/components/Menu.vue';
	import { computed, ref } from 'vue';
	import { useStore } from 'vuex';

	const store = useStore();
	let isHidden = ref(computed(() => store.state.isHidden));

	let headerImageClass = computed(() => ({
		'background-color': isHidden.value ? '#a7a8bd' : 'transparent',
		'background-image': isHidden.value ? '' : 'url(../assets/gif/header.gif)',
		height: isHidden.value ? '500px' : 'auto',
		// 这里添加其余的样式更改
	}));
</script>

<style scoped>
	.headerimg {
		position: relative;
		width: 100%;
		height: 300px !important;
		overflow: hidden;
		background-size: 100% 100%;
		background-color: transparent !important;
	}

	.rotate {
		animation: rotation 5s infinite linear;
		width: 13%;
		border-radius: 50%;
	}
	@keyframes rotation {
		from {
			transform: rotate(0deg);
		}
		to {
			transform: rotate(360deg);
		}
	}
</style>
