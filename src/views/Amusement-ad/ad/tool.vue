<template>
	<div style="width: 10%; margin-top: 40px">
		<el-button
			round
			style="
				background-color: transparent;
				margin-top: 11px;
				width: 100%;
				box-shadow: inset 0 0 50px rgb(255, 167, 167);
			"
			@click="dialogFormVisible = true">
			字符串加密
		</el-button>
		<el-dialog
			v-model="dialogFormVisible"
			title="字符串加密"
			width="500">
			<el-form :model="form">
				<el-form-item
					label="需加密/解密的内容"
					:label-width="formLabelWidth">
					<el-input
						v-model="form.content"
						autocomplete="off" />
				</el-form-item>
				<el-form-item
					label="自定义的密码"
					:label-width="formLabelWidth">
					<el-input
						v-model="form.password"
						autocomplete="off"
						placeholder="Key必须为1-8位纯数字" />
				</el-form-item>
			</el-form>
			<el-dialog
				v-model="innerVisible"
				width="500"
				title="密文信息"
				append-to-body>
				<el-input
					type="textarea"
					:rows="1"
					v-model="enmissString"
					readonly></el-input>
			</el-dialog>
			<el-dialog
				v-model="innerVisibletwo"
				width="500"
				title="明文信息"
				append-to-body>
				<el-input
					type="textarea"
					:rows="1"
					v-model="demissString"
					readonly></el-input>
			</el-dialog>
			<template #footer>
				<div class="dialog-footer">
					<el-button
						type="danger"
						@click="decrypt"
						>解密</el-button
					>
					<el-button
						type="success"
						@click="encrypt">
						加密
					</el-button>
				</div>
			</template>
		</el-dialog>
		<el-card
			style="
				width: auto;
				display: flex;
				margin-top: 16px;
				justify-content: center;
				align-items: center;
			">
			<p style="text-align: center">ico站标获取</p>
			<el-input
				v-model="inputValue"
				@keyup.enter="fetchIco"
				style="width: 100%"
				placeholder="请输入网站地址" />
			<el-button
				type="primary"
				@click="fetchIco"
				style="margin-top: 20px">
				获取
			</el-button>
			<el-image
				:src="icoUrl"
				style="width: 100%; height: auto; padding-top: 10px"
				v-if="wds" />
			<p v-if="checkInput && inputValue != '' && !validUrl">
				参数似乎不正确
			</p>
		</el-card>

		<el-empty description="工具位待添加" />
	</div>
</template>

<script setup lang="ts">
	import { ref, reactive } from 'vue';
	import axios from 'axios';
	import { ElNotification } from 'element-plus';

	const inputValue = ref('');
	const validUrl = ref(false);
	const wds = ref(false);
	const icoUrl = ref('');
	const checkInput = ref(false);
	const innerVisible = ref(false);
	const innerVisibletwo = ref(false);
	const enmissString = ref(''); //密文
	const demissString = ref(''); //明文

	const fetchIco = () => {
		checkInput.value = true;
		const tempUrl = `https://api.vvhan.com/api/ico?url=${inputValue.value}`;
		const tempImg = new Image();
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

	const dialogFormVisible = ref(false);
	const formLabelWidth = '140px';

	const form = reactive({
		content: '',
		password: '',
	});

	//表单判断
	const validateForm = () => {
		if (!form.content.trim()) {
			ElNotification({
				title: '提示',
				message: '没有输入需要解密/加密的内容',
				type: 'error',
			});
			return false;
		}
		if (!form.password.trim()) {
			ElNotification({
				title: '提示',
				message: '没有输入密码',
				type: 'error',
			});
			return false;
		}

		if (!/^[0-9]{1,8}$/.test(form.password)) {
			ElNotification({
				title: '提示',
				message: '密码不是1-8位纯数字',
				type: 'error',
			});
			return false;
		}

		return true;
	};

	//加密
	const encrypt = async () => {
		if (!validateForm()) return;
		innerVisible.value = true;
		try {
			const encryptUrl = await axios.get('https://api.vvhan.com/api/jm', {
				params: {
					key: form.password,
					string: form.content,
					type: 'en',
				},
			});
			if (encryptUrl.data.success) {
				enmissString.value = encryptUrl.data.enmissString; // Assign the value here
			}
		} catch (error) {
			console.error('Failed to fetch image:', error);
		}
	};
	//解密
	const decrypt = async () => {
		if (!validateForm()) return;
		innerVisibletwo.value = true;
		try {
			const encryptwotUrl = await axios.get(
				'https://api.vvhan.com/api/jm',
				{
					params: {
						key: form.password,
						string: form.content,
						type: 'de',
					},
				}
			);
			if (encryptwotUrl.data.success) {
				demissString.value = encryptwotUrl.data.demissString; // Assign the value here
			}
		} catch (error) {
			console.error('Failed to fetch image:', error);
		}
	};
</script>

<style lang="less" scoped>
	:deep(.el-card__body) {
		display: flex !important;
		flex-direction: column !important;
	}
</style>
