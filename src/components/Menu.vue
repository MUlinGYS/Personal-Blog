<template>
	<el-menu
		:default-active="activeIndex"
		class="el-menu-demo"
		mode="horizontal"
		:ellipsis="false"
		@select="handleSelect"
	>
		<el-menu-item index="0"
			><h2 style="color: white">个人博客</h2></el-menu-item
		>
		<div class="flex-grow" />
		<el-menu-item index="1">Processing Center</el-menu-item>
		<el-sub-menu index="2">
			<template #title>Workspace</template>
			<el-menu-item
				index="2-1"
				style="background-color: transparent !important"
				>item one</el-menu-item
			>
			<el-sub-menu index="2-2">
				<template #title>item four</template>
				<el-menu-item index="2-4-1">item one</el-menu-item>
			</el-sub-menu>
		</el-sub-menu>
	</el-menu>
</template>

<script lang="ts" setup>
	import { ref } from 'vue';

	const activeIndex = ref('1');
	const handleSelect = (key: string, keyPath: string[]) => {
		console.log(key, keyPath);
	};
</script>

<style>
	.flex-grow {
		flex-grow: 1;
	}

	.el-menu {
		background-color: transparent;
		border-bottom: 0px !important;
	}

	.el-menu--horizontal .el-menu-item:not(.is-disabled):hover,
	.el-menu-item.is-active,
	.el-sub-menu:hover .el-sub-menu__title {
		background-color: transparent !important;
		color: inherit !important;
	}
	.el-menu-item:focus,
	.el-menu-item:active {
		outline: none;
	}
</style>
