<template>
	<div class="pigeonhole-container">
		<!-- 统计卡片 -->
		<el-row style="margin-top: 25px">
			<el-col :span="6">
				<el-statistic title="推文总数统计" :value="statistics.tweet_count || 0">
					<template #suffix>
						<el-icon style="vertical-align: -0.125em">
							<Document />
						</el-icon>
					</template>
				</el-statistic>
			</el-col>
			<el-col :span="6">
				<el-statistic :value="statistics.resource_count || 0">
					<template #title>
						<div style="display: inline-flex; align-items: center">
							资源链接统计
							<el-icon style="margin-left: 4px" :size="12">
								<Link />
							</el-icon>
						</div>
					</template>
				</el-statistic>
			</el-col>
			<el-col :span="6">
				<el-statistic title="技术锦囊统计" :value="statistics.tech_tip_count || 0">
					<template #suffix>
						<el-icon style="vertical-align: -0.125em">
							<Collection />
						</el-icon>
					</template>
				</el-statistic>
			</el-col>
			<el-col :span="6">
				<el-statistic title="阅读量统计" :value="statistics.read_count || 0">
					<template #suffix>
						<el-icon style="vertical-align: -0.125em">
							<ChatLineRound />
						</el-icon>
					</template>
				</el-statistic>
			</el-col>
		</el-row>

		<!-- 提交记录时间线 -->
		<div class="timeline-container">
			<h2 class="section-title">最近提交记录</h2>
			<el-timeline>
				<el-timeline-item v-for="(submission, index) in submissions" :key="index"
					:type="getTimelineItemType(submission.type)" :color="getTimelineItemColor(submission.type)"
					:timestamp="formatDate(submission.created_at)" placement="top">
					<el-card shadow="hover" class="submission-card">
						<div class="submission-header">
							<span class="submission-type">{{ getSubmissionTypeName(submission.type) }}</span>
							<span class="submission-title">{{ getSubmissionTitle(submission) }}</span>
						</div>
						<div class="demo-collapse">
							<el-collapse v-model="activeNames[index]" accordion>
								<el-collapse-item name="1">
									<template #title>
										详情
										<el-icon class="header-icon">
											<InfoFilled />
										</el-icon>
									</template>
									<div class="submission-content">
										{{ getSubmissionContent(submission) }}
									</div>
								</el-collapse-item>
								<el-collapse-item title="备注" name="2">
									<div>{{ submission.note || '无' }}</div>
								</el-collapse-item>
							</el-collapse>
						</div>
					</el-card>
				</el-timeline-item>
			</el-timeline>
		</div>
	</div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { Document, Link, Collection, ChatLineRound, InfoFilled } from '@element-plus/icons-vue';
import axios from 'axios';
import { ElMessage } from 'element-plus';
import { useRouter } from 'vue-router';

const router = useRouter();

// 统计数据
const statistics = ref({
	tweet_count: 0,
	resource_count: 0,
	tech_tip_count: 0,
	read_count: 0
});

// 提交记录
const submissions = ref([]);
// 折叠面板激活项
const activeNames = ref([]);

// 获取统计数据
const fetchStatistics = async () => {
	try {
		const response = await axios.get('http://localhost:5000/api/statistics');
		statistics.value = response.data;
	} catch (error) {
		ElMessage.error('获取统计数据失败');
		console.error(error);
	}
};

// 获取提交记录
const fetchSubmissions = async () => {
	try {
		const response = await axios.get('http://localhost:5000/api/submissions', {
			params: { limit: 20 }
		});
		submissions.value = response.data;
		// 初始化折叠面板激活项
		activeNames.value = new Array(submissions.value.length).fill('');
	} catch (error) {
		ElMessage.error('获取提交记录失败');
		console.error(error);
	}
};

// 格式化日期
const formatDate = (dateString) => {
	if (!dateString) return '';
	const date = new Date(dateString);
	return date.toLocaleString();
};

// 获取时间线项目类型
const getTimelineItemType = (type) => {
	switch (type) {
		case 'tweet':
			return 'primary';
		case 'resource':
			return 'success';
		case 'tech_tip':
			return 'warning';
		default:
			return 'info';
	}
};

// 获取时间线项目颜色
const getTimelineItemColor = (type) => {
	switch (type) {
		case 'tweet':
			return '#409EFF';
		case 'resource':
			return '#67C23A';
		case 'tech_tip':
			return '#E6A23C';
		default:
			return '#909399';
	}
};

// 获取提交类型名称
const getSubmissionTypeName = (type) => {
	switch (type) {
		case 'tweet':
			return '推文';
		case 'resource':
			return '资源链接';
		case 'tech_tip':
			return '技术锦囊';
		default:
			return '未知';
	}
};

// 获取提交标题
const getSubmissionTitle = (submission) => {
	switch (submission.type) {
		case 'tweet':
			return submission.title;
		case 'resource':
			return submission.name;
		case 'tech_tip':
			return submission.name;
		default:
			return '未知标题';
	}
};

// 获取提交内容
const getSubmissionContent = (submission) => {
	switch (submission.type) {
		case 'tweet':
			return submission.content;
		case 'resource':
			return submission.url;
		case 'tech_tip':
			return submission.content;
		default:
			return '无内容';
	}
};

// 处理卡片点击
const handleCardClick = (type) => {
	switch (type) {
		case 'tweets':
			router.push('/tweets');
			break;
		case 'resources':
			router.push('/resources');
			break;
		case 'tech-tips':
			router.push('/tech-tips');
			break;
	}
};

// 在 script setup 部分添加
const incrementViewCount = async (contentType, contentId) => {
	try {
		await axios.post(`/api/view-count/${contentType}/${contentId}`);
	} catch (error) {
		console.error('Error incrementing view count:', error);
	}
};

// 组件挂载时获取数据
onMounted(() => {
	fetchStatistics();
	fetchSubmissions();
});
</script>

<style scoped>
.pigeonhole-container {
	padding: 24px;
}

/* 移除统计卡片相关样式 */
.timeline-container {
	margin-top: 40px;
}

.section-title {
	font-size: 20px;
	font-weight: 600;
	margin-bottom: 20px;
	color: #303133;
}

.submission-card {
	margin-bottom: 10px;
}

.submission-header {
	display: flex;
	align-items: center;
	margin-bottom: 10px;
}

.submission-type {
	display: inline-block;
	padding: 2px 8px;
	border-radius: 4px;
	font-size: 12px;
	margin-right: 10px;
	background-color: #f0f0f0;
	color: #606266;
}

.submission-title {
	font-weight: 600;
	font-size: 16px;
	color: #303133;
}

.submission-content {
	white-space: pre-line;
	line-height: 1.6;
	color: #606266;
}

.header-icon {
	margin-left: 5px;
}

.el-col {
	text-align: center;
	margin-bottom: 20px;
}

.submission-item {
	cursor: pointer;
	transition: background-color 0.3s;
}

.submission-item:hover {
	background-color: rgba(0, 0, 0, 0.05);
}

/* 移除新的统计卡片样式 */
.statistics-cards {
	display: none;
}

.stat-card {
	display: none;
}

.stat-icon {
	display: none;
}

.stat-info {
	display: none;
}

.stat-value {
	display: none;
}

.stat-label {
	display: none;
}
</style>
