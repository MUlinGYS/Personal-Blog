<template>
	<el-row style="margin-top: 25px">
		<el-col :span="6">
			<el-statistic
				title="Daily active users"
				:value="268500"
			/>
		</el-col>
		<el-col :span="6">
			<el-statistic :value="138">
				<template #title>
					<div style="display: inline-flex; align-items: center">
						Ratio of men to women
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
				title="Total Transactions"
				:value="outputValue"
			/>
		</el-col>
		<el-col :span="6">
			<el-statistic
				title="Feedback number"
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
				<h4>Update Github template</h4>
				<p>Tom committed {{ activity.content }}</p>
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
			content: 'Custom icon',
			timestamp: '2018-04-12 20:46',
			size: 'large',
			type: 'primary',
			icon: MoreFilled,
		},
		{
			content: 'Custom color',
			timestamp: '2018-04-03 20:46',
			color: '#0bbd87',
		},
		{
			content: 'Custom size',
			timestamp: '2018-04-03 20:46',
			size: 'large',
		},
		{
			content: 'Custom hollow',
			timestamp: '2018-04-03 20:46',
			type: 'primary',
			hollow: true,
		},
		{
			content: 'Default node',
			timestamp: '2018-04-03 20:46',
		},
	];
</script>

<style scoped>
	.el-col {
		text-align: center;
	}
</style>
