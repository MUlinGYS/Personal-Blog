<template>
	<div class="headerimg">
		<Menu></Menu>
		<div
			style="
				width: 100vw;
				height: calc(100% - 60px);
				display: flex;
				justify-content: center;
				align-items: center;
			"
		>
			<img
				class="rotate"
				src="../assets/img/avatar.jpeg"
			/>
		</div>
	</div>
</template>

<script setup lang="ts" name="Header">
	import Menu from '@/components/Menu.vue';
</script>

<style scoped>
	.headerimg {
		position: relative;
		width: 100%;
		height: 500px;
		overflow: hidden;
		background-size: 100% 100%;
		background-color: #a7a8bd;
		background-image: url('../assets/gif/header.gif');
	}

	.rotate {
		animation: rotation 5s infinite linear;
		width: 23%;
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
