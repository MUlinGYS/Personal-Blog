<template>
	<el-card>
		<el-space
			direction="vertical"
			style="width: 100%"
		>
			<!-- 这个div里写入一个富文本编辑器 -->
			<el-card style="width: 97vw">
				<div>
					<el-input
						v-model="input0"
						placeholder="标题"
					>
						<template #prepend>标题</template>
					</el-input>
				</div>
			</el-card>
			<el-card
				class="ueditor"
				style="width: 97vw"
			>
				<vue-ueditor-wrap
					v-model="msg"
					:config="editorConfig"
					editor-id="editor-demo-01"
				></vue-ueditor-wrap>
			</el-card>
			<!-- <el-empty description="富文本编辑器正在开发中，敬请期待！" /> -->
			<el-card style="width: 97vw; display: flex; justify-content: center">
				<el-rate
					v-model="value"
					show-score
					allow-half
					size="large"
					score-template="为这篇文章定级"
			/></el-card>
			<el-card style="width: 97vw">
				<div>
					<el-input
						v-model="input1"
						placeholder="网站地址或本机文件地址"
					>
						<template #prepend>
							<el-select
								v-model="select"
								placeholder="协议"
								style="width: 115px"
							>
								<el-option
									label="Http://"
									value="1"
								/>
								<el-option
									label="https://"
									value="2"
								/>
								<el-option
									label="file://"
									value="3"
								/>
								<el-option
									label="其他（自行输入）"
									value="4"
								/>
							</el-select>
						</template>
					</el-input>
				</div>
				<div class="mt-4">
					<el-input
						v-model="input3"
						class="input-with-select"
					>
						<template #prepend>标签</template>
					</el-input>
				</div>
				<div class="mt-4">
					<el-input
						v-model="input2"
						placeholder="输入备注信息"
					>
						<template #prepend>备注</template>
					</el-input>
				</div>
			</el-card>
			<el-button
				style="width: 97vw"
				type="primary"
				round
			>
				发布<el-icon class="el-icon--right"><Upload /></el-icon>
			</el-button>
		</el-space>
	</el-card>
</template>

<script setup lang="ts">
	import { ref } from 'vue';

	const input0 = ref('');
	const input1 = ref('');
	const input2 = ref('');
	const input3 = ref('');
	const select = ref('');

	const value = ref();

	//富文本编辑器
	const msg = ref('<h2>推文内容</h2>');
	const editorConfig = ref({
		UEDITOR_HOME_URL: '/UEditor/',
		serverUrl: '//ueditor.zhenghaochuan.com/cos',
	});
</script>

<style lang="less">
	.input-with-select .el-input-group__prepend {
		background-color: var(--el-fill-color-blank);
	}
	.edui-editor-iframeholder {
		height: 50vh !important;
		width: 100% !important;
	}
	.edui-editor {
		width: 100% !important;
	}
</style>
