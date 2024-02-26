<template>
	<ul
		v-infinite-scroll="load"
		class="infinite-list"
		style="overflow: auto"
		infinite-scroll-distance="10px"
	>
		<li
			v-for="i in count"
			:key="i"
			class="infinite-list-item"
		>
			<el-card
				shadow="hover"
				style="width: 100%"
			>
				<template #header>
					<span>推文name+时间</span>
				</template>
				<div
					v-for="o in 4"
					:key="o"
					class="text item"
				>
					{{ '内容 ' + o }}
				</div>
				<template #footer>备注:无</template>
			</el-card>
		</li>
	</ul>
</template>

<script lang="ts" setup>
	import { ref } from 'vue';
	const count = ref(0);
	const load = () => {
		count.value += 2;
	};
</script>

<style>
	.infinite-list {
		height: 650px;
		padding: 0;
		margin: 0;
		list-style: none;
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
	.infinite-list .infinite-list-item + .list-item {
		margin-top: 10px;
	}
</style>
