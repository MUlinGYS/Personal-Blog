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
		<el-menu-item
			index="1"
			style="color: white"
			>首页</el-menu-item
		>
		<el-menu-item
			index="2"
			style="color: white"
			>隐藏</el-menu-item
		>
	</el-menu>
</template>

<script lang="ts" setup>
	import { ref } from 'vue';
	import { useStore } from 'vuex';

	const store = useStore();

	const activeIndex = ref('1');
	const handleSelect = (key: string) => {
		if (key === '2') {
			store.commit('setShowContent', false);
			store.commit('setHide', false);
		} else if (key === '1') {
			store.commit('setShowContent', true);
			store.commit('setHide', true);
		}
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

	.el-menu--horizontal > .el-menu-item.is-active {
		border-bottom: 2px solid white !important;
		color: white !important;
	}

	.el-menu--horizontal > .el-menu-item.is-active {
		border-bottom: 2px solid white !important;
		color: white !important;
	}

	html:root {
		--el-menu-text-color: white !important;
	}
</style>
