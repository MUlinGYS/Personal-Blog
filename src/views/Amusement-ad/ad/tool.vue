<template>
	<div style="width: 10%; margin-top: 40px">
		<el-card
			style="
				width: auto;
				display: flex;
				justify-content: center;
				alignitems: center;
			"
		>
			<p style="text-align: center">ico站标获取</p>
			<el-input
				v-model="inputValue"
				@keyup.enter="fetchIco"
				style="width: 100%"
				placeholder="请输入网站地址"
			/>
			<el-button
				type="primary"
				@click="fetchIco"
				style="margin-top: 20px"
			>
				获取
			</el-button>
			<el-image
				:src="icoUrl"
				style="width: 100%; height: auto; padding-top: 10px"
				v-if="wds"
			/>
			<p v-if="checkInput && inputValue != '' && !validUrl">参数似乎不正确</p>
		</el-card>
		<el-empty description="工具位" />
	</div>
</template>

<script setup lang="ts">
	import { ref } from 'vue';

	const inputValue = ref(''); // 输入框的值
	const validUrl = ref(false); // 用于指示URL是否有效
	const wds = ref(false); // 控制展示的标识
	const icoUrl = ref(''); // 存储获取到的图片的url
	const checkInput = ref(false); // 用于判断是否调用fetchIco方法

	const fetchIco = () => {
		checkInput.value = true;
		let tempUrl = `https://api.vvhan.com/api/ico?url=${inputValue.value}`;
		let tempImg = new Image();
		tempImg.src = tempUrl;

		tempImg.onload = () => {
			icoUrl.value = tempUrl;
			validUrl.value = true;
			wds.value = true;
		};

		tempImg.onerror = () => {
			validUrl.value = false;
			wds.value = false;
		};
	};
</script>

<style lang="less" scoped>
	:deep(.el-card__body) {
		display: flex !important;
		flex-direction: column !important;
	}
</style>
