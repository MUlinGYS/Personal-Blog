<template>
	<el-row style="margin-top: 25px">
		<el-col :span="6">
			<el-statistic
				title="推文总数统计"
				:value="268500"
			/>
		</el-col>
		<el-col :span="6">
			<el-statistic :value="138">
				<template #title>
					<div style="display: inline-flex; align-items: center">
						资源链接统计
						<el-icon
							style="margin-left: 4px"
							:size="12"
						>
							<Male />
						</el-icon>
					</div>
				</template>
				<template #suffix>/100</template>
			</el-statistic>
		</el-col>
		<el-col :span="6">
			<el-statistic
				title="技术锦囊统计"
				:value="outputValue"
			/>
		</el-col>
		<el-col :span="6">
			<el-statistic
				title="阅读量统计"
				:value="562"
			>
				<template #suffix>
					<el-icon style="vertical-align: -0.125em">
						<ChatLineRound />
					</el-icon>
				</template>
			</el-statistic>
		</el-col>
	</el-row>
	<el-timeline style="margin-top: 25px">
		<el-timeline-item
			v-for="(activity, index) in activities"
			:key="index"
			:icon="activity.icon"
			:type="activity.type"
			:color="activity.color"
			:size="activity.size"
			:hollow="activity.hollow"
			:timestamp="activity.timestamp"
			center
			placement="top"
		>
			<el-card>
				<div class="demo-collapse">
					<el-collapse
						v-model="activeNames[index]"
						accordion
					>
						<el-collapse-item name="1"
							><template #title>
								标题<el-icon class="header-icon">
									<info-filled />
								</el-icon>
							</template>
							<div>
								Consistent with real life: in line with the process and logic of
								real life, and comply with languages and habits that the users
								are used to;
							</div>
						</el-collapse-item>
						<el-collapse-item
							title="内容"
							name="2"
						>
							<div>推文内容</div>
						</el-collapse-item>
						<el-collapse-item
							title="链接"
							name="3"
						>
							<div>www.xxxxxxxxxxxx.com</div>
						</el-collapse-item>
						<el-collapse-item
							title="备注"
							name="4"
						>
							<div>无</div>
						</el-collapse-item>
					</el-collapse>
				</div>
			</el-card>
		</el-timeline-item>
	</el-timeline>
</template>

<script lang="ts" setup>
	import { ref } from 'vue';
	import { useTransition } from '@vueuse/core';
	import { ChatLineRound, Male } from '@element-plus/icons-vue';

	const source = ref(0);
	const outputValue = useTransition(source, {
		duration: 1500,
	});
	source.value = 172000;

	import { MoreFilled } from '@element-plus/icons-vue';

	const activities = [
		{
			timestamp: '2018-04-12 20:46',
			size: 'large',
			type: 'primary',
			icon: MoreFilled,
		},
		{
			timestamp: '2018-04-03 20:46',
			color: '#0bbd87',
		},
		{
			timestamp: '2018-04-03 20:46',
			size: 'large',
		},
		{
			timestamp: '2018-04-03 20:46',
			type: 'primary',
			hollow: true,
		},
		{
			timestamp: '2018-04-03 20:46',
		},
	];
	const activeNames = activities.map(() => '');
</script>

<style scoped>
	.el-col {
		text-align: center;
	}
</style>
