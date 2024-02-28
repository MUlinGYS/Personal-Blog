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
				<div class="demo-collapse">
					<el-collapse
						v-model="activeName"
						accordion
					>
						<el-collapse-item name="1"
							><template #title>
								标题{{ activity.content
								}}<el-icon class="header-icon">
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
							title="Feedback"
							name="2"
						>
							<div>
								Operation feedback: enable the users to clearly perceive their
								operations by style updates and interactive effects;
							</div>
						</el-collapse-item>
						<el-collapse-item
							title="Efficiency"
							name="3"
						>
							<div>
								Simplify the process: keep operating process simple and
								intuitive;
							</div>
						</el-collapse-item>
						<el-collapse-item
							title="Controllability"
							name="4"
						>
							<div>
								Decision making: giving advices about operations is acceptable,
								but do not make decisions for the users;
							</div>
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

	const activeName = ref('1');
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
