<template>
	<div class="tweets-wrapper">
		<!-- 搜索和添加区域 -->
		<div class="action-bar">
			<el-input v-model="searchQuery" placeholder="搜索推文标题" class="search-input" clearable @input="handleSearch">
				<template #prefix>
					<el-icon>
						<Search />
					</el-icon>
				</template>
			</el-input>
			<div class="action-buttons">
				<el-button type="primary" @click="handleRefresh" :loading="loading">
					<el-icon>
						<Refresh />
					</el-icon>
					刷新
				</el-button>
				<el-button type="primary" @click="openTweetDialog()">添加推文</el-button>
			</div>
		</div>

		<!-- 推文列表容器 -->
		<div class="tweets-container">
			<ul v-infinite-scroll="load" class="infinite-list" style="overflow: auto" infinite-scroll-distance="10px">
				<li v-for="tweet in tweets" :key="tweet.id" class="infinite-list-item">
					<el-card shadow="hover" style="width: 100%">
						<template #header>
							<div class="card-header">
								<span>{{ formatDate(tweet.created_at) }} ------- {{ tweet.title }}</span>
								<div class="card-actions">
									<el-button type="primary" link @click="showTweetDetail(tweet)">查看详情</el-button>
									<el-button type="primary" link @click="openTweetDialog(tweet)">编辑</el-button>
									<el-button type="danger" link @click="handleDelete(tweet)">删除</el-button>
								</div>
							</div>
						</template>
						<div class="text item">
							{{ truncateContent(tweet.content) }}
						</div>
						<template #footer>备注: {{ tweet.note || '无' }}</template>
					</el-card>
				</li>
			</ul>
		</div>

		<!-- 推文详情对话框 -->
		<el-dialog v-model="detailDialogVisible" :title="currentTweet?.title" width="60%">
			<div class="tweet-detail">
				<div class="tweet-meta">
					<span class="time">发布时间：{{ formatDate(currentTweet?.created_at) }}</span>
				</div>
				<div class="tweet-content" v-if="currentTweet">
					<div v-html="formatContent(currentTweet.content)"></div>
				</div>
				<div class="tweet-note" v-if="currentTweet?.note">
					<el-divider content-position="left">备注</el-divider>
					{{ currentTweet.note }}
				</div>
			</div>
		</el-dialog>

		<!-- 添加/编辑推文对话框 -->
		<el-dialog v-model="tweetDialogVisible" :title="isEdit ? '编辑推文' : '添加推文'" width="70%" class="edit-dialog">
			<div class="dialog-header">
				<p class="edit-time" v-if="isEdit">最后编辑时间：{{ formatDate(tweetData.updated_at) }}</p>
			</div>
			<el-form :model="tweetData" label-width="80px" class="edit-form">
				<el-form-item label="标题" required>
					<el-input v-model="tweetData.title" placeholder="请输入推文标题" class="title-input" :maxlength="100"
						show-word-limit></el-input>
				</el-form-item>

				<el-tabs v-model="activeTab" class="content-tabs">
					<el-tab-pane label="编辑内容" name="edit">
						<el-form-item label="内容" required>
							<el-input v-model="tweetData.content" type="textarea" rows="10" placeholder="请输入推文内容"
								class="content-input" :maxlength="100000" show-word-limit></el-input>
							<div class="coding-guide">
								<el-popover placement="bottom" :width="300" trigger="hover">
									<template #reference>
										<el-link type="primary" :underline="false" class="guide-link">
											<el-icon>
												<InfoFilled />
											</el-icon>
											代码块编写指南
										</el-link>
									</template>
									<template #default>
										<div class="guide-content">
											<h4>如何添加代码块</h4>
											<p>使用三个反引号(```)包裹代码</p>
										</div>
									</template>
								</el-popover>
							</div>
						</el-form-item>
					</el-tab-pane>
					<el-tab-pane label="预览" name="preview">
						<div class="preview-container">
							<div class="preview-content" v-html="formatContent(tweetData.content)"></div>
						</div>
					</el-tab-pane>
				</el-tabs>

				<el-form-item label="备注">
					<el-input v-model="tweetData.note" type="textarea" rows="2" placeholder="请输入备注（可选）"
						class="note-input" :maxlength="1000" show-word-limit></el-input>
				</el-form-item>
			</el-form>
			<template #footer>
				<span class="dialog-footer">
					<el-button @click="tweetDialogVisible = false" class="cancel-btn">取消</el-button>
					<el-button type="primary" @click="handleSubmit" class="confirm-btn">{{ isEdit ? '保存修改' : '确定'
					}}</el-button>
				</span>
			</template>
		</el-dialog>
	</div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { ElMessage, ElMessageBox } from 'element-plus';
import { Search, Refresh, InfoFilled } from '@element-plus/icons-vue';
import axios from 'axios';
import request from '@/utils/request'; // 导入request实例
import hljs from 'highlight.js';
import 'highlight.js/styles/atom-one-dark.css'; // 导入一个喜欢的主题样式

// 搜索查询
const searchQuery = ref('');
// 防抖定时器
let searchTimer = null;

// 当前页码
const currentPage = ref(1);
// 每页数量
const perPage = 10;

// 推文列表数据
const tweets = ref([]);
// 对话框显示状态
const tweetDialogVisible = ref(false);
// 详情对话框显示状态
const detailDialogVisible = ref(false);
// 当前查看的推文
const currentTweet = ref(null);
// 是否为编辑模式
const isEdit = ref(false);
// 推文表单数据
const tweetData = ref({
	id: null,
	title: '',
	content: '',
	note: ''
});

// 编辑页面当前激活的标签页
const activeTab = ref('edit');

// 加载状态
const loading = ref(false);
// 是否还有更多数据
const hasMore = ref(true);

// 处理内容格式化，检测并高亮代码块
const formatContent = (content) => {
	if (!content) return '';

	// 检测是否使用```包裹的代码块
	const codeBlockRegex = /```([a-z]*)\n([\s\S]*?)```/g;

	// 替换代码块为高亮版本
	const formattedContent = content.replace(codeBlockRegex, (match, language, code) => {
		// 简单高亮，不检测语言
		try {
			const highlighted = hljs.highlightAuto(code);
			return `<pre class="code-block"><code class="hljs">${highlighted.value}</code></pre>`;
		} catch (error) {
			console.error('代码高亮出错:', error);
			return `<pre class="code-block"><code>${code}</code></pre>`;
		}
	});

	// 处理普通文本（非代码块部分）
	// 将换行符转换为<br>并保持段落格式
	return formattedContent.replace(/\n\n/g, '</p><p>').replace(/\n/g, '<br>');
};

// 加载推文列表
const loadTweets = async () => {
	try {
		const params = {
			page: currentPage.value,
			per_page: perPage
		};
		if (searchQuery.value) {
			params.search = searchQuery.value;
			// 搜索时重置页码
			currentPage.value = 1;
		}

		const response = await request.get('/tweets', { params });
		const { items, total, pages } = response.data;

		// 如果搜索模式下，直接替换数据
		if (searchQuery.value || currentPage.value === 1) {
			tweets.value = items;
		} else {
			// 非搜索模式下，追加数据
			tweets.value = [...tweets.value, ...items];
		}

		// 更新是否有更多数据
		hasMore.value = currentPage.value < pages;
		// 如果还有更多数据，增加页码
		if (hasMore.value) {
			currentPage.value++;
		}
	} catch (error) {
		ElMessage.error('加载推文失败');
		console.error(error);
	} finally {
		loading.value = false;
	}
};

// 处理搜索
const handleSearch = () => {
	// 清除之前的定时器
	if (searchTimer) {
		clearTimeout(searchTimer);
	}
	// 设置新的定时器，延迟300ms执行搜索
	searchTimer = setTimeout(() => {
		currentPage.value = 1; // 重置页码
		loadTweets();
	}, 300);
};

// 打开推文对话框
const openTweetDialog = (tweet = null) => {
	isEdit.value = !!tweet;
	if (tweet) {
		tweetData.value = {
			id: tweet.id,
			title: tweet.title,
			content: tweet.content,
			note: tweet.note,
			updated_at: tweet.updated_at
		};
	} else {
		tweetData.value = {
			id: null,
			title: '',
			content: '',
			note: ''
		};
	}
	tweetDialogVisible.value = true;
};

// 提交表单
const handleSubmit = async () => {
	try {
		if (isEdit.value) {
			await request.put(`/tweets/${tweetData.value.id}`, {
				title: tweetData.value.title,
				content: tweetData.value.content,
				note: tweetData.value.note
			});
			ElMessage.success('修改推文成功');
		} else {
			await request.post('/tweets', {
				title: tweetData.value.title,
				content: tweetData.value.content,
				note: tweetData.value.note
			});
			ElMessage.success('添加推文成功');
		}
		tweetDialogVisible.value = false;
		loadTweets();
	} catch (error) {
		ElMessage.error(isEdit.value ? '修改推文失败' : '添加推文失败');
		console.error(error);
	}
};

// 格式化日期
const formatDate = (dateString) => {
	if (!dateString) return '';
	const date = new Date(dateString);
	return date.toLocaleString();
};

// 截断内容，最多显示5行
const truncateContent = (content) => {
	if (!content) return '';
	const lines = content.split('\n');
	if (lines.length <= 5) return content;
	return lines.slice(0, 5).join('\n') + '...';
};

// 显示推文详情
const showTweetDetail = async (tweet) => {
	try {
		// 增加阅读量
		await request.post(`/view-count/tweet/${tweet.id}`);
		currentTweet.value = tweet;
		detailDialogVisible.value = true;
	} catch (error) {
		console.error('增加阅读量失败:', error);
	}
};

// 删除推文
const handleDelete = (tweet) => {
	ElMessageBox.confirm(
		'确定要删除这条推文吗？',
		'删除确认',
		{
			confirmButtonText: '确定',
			cancelButtonText: '取消',
			type: 'warning',
		}
	).then(async () => {
		try {
			await request.delete(`/tweets/${tweet.id}`);
			ElMessage.success('删除推文成功');
			// 重新加载推文列表
			currentPage.value = 1;
			loadTweets();
		} catch (error) {
			ElMessage.error('删除推文失败');
			console.error(error);
		}
	}).catch(() => {
		// 用户取消删除
	});
};

// 无限滚动加载
const load = () => {
	if (loading.value || !hasMore.value) return;
	loading.value = true;
	loadTweets();
};

// 刷新推文列表
const handleRefresh = () => {
	currentPage.value = 1;
	searchQuery.value = '';
	tweets.value = []; // 清空现有数据
	hasMore.value = true; // 重置加载更多状态
	loadTweets();
};

// 组件挂载时加载推文
onMounted(() => {
	loadTweets();
});
</script>

<style scoped>
/* 父容器样式 */
.tweets-wrapper {
	padding: 24px;
	min-height: 100vh;
}

/* 全局滚动条美化 - 添加:deep使其生效于子组件 */
:deep(::-webkit-scrollbar) {
	width: 4px;
	height: 6px;
}

:deep(::-webkit-scrollbar-thumb) {
	background-color: rgba(255, 255, 255, 0.3);
	border-radius: 2px;
}

:deep(::-webkit-scrollbar-track) {
	background-color: rgba(250, 5, 5, 0.05);
}

:deep(::-webkit-scrollbar-button) {
	display: none;
}

/* 为代码块特别定制的滚动条样式 */
.code-block code::-webkit-scrollbar-thumb {
	background-color: rgba(255, 255, 255, 0.3);
}

.code-block code::-webkit-scrollbar-track {
	background-color: rgba(0, 0, 0, 0.1);
}

/* 操作栏样式 */
.action-bar {
	display: flex;
	justify-content: space-between;
	align-items: center;
	margin-bottom: 24px;
	padding: 16px 24px;
	background-color: rgba(255, 255, 255, 0.15);
	border-radius: 12px;
	box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.15);
	backdrop-filter: blur(8px);
	-webkit-backdrop-filter: blur(8px);
	border: 1px solid rgba(255, 255, 255, 0.15);
}

.search-input {
	width: 300px;
}

.search-input :deep(.el-input__wrapper) {
	background-color: rgba(255, 255, 255, 0.15);
	border: 1px solid rgba(255, 255, 255, 0.15);
	color: rgba(44, 62, 80, 0.8);
	border-radius: 20px;
	padding: 0 15px;
	transition: all 0.3s;
}

.search-input :deep(.el-input__wrapper:hover) {
	background-color: rgba(255, 255, 255, 0.2);
}

.search-input :deep(.el-input__wrapper.is-focus) {
	background-color: rgba(255, 255, 255, 0.2);
	box-shadow: 0 0 0 1px rgba(52, 152, 219, 0.2) inset;
}

.action-buttons {
	display: flex;
	gap: 12px;
}

.action-buttons .el-button {
	display: flex;
	align-items: center;
	gap: 6px;
}

.action-buttons .el-icon {
	font-size: 16px;
}

/* 推文列表容器 */
.tweets-container {
	background-color: rgba(255, 255, 255, 0.15);
	border-radius: 12px;
	padding: 24px;
	box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.1);
	backdrop-filter: blur(8px);
	-webkit-backdrop-filter: blur(8px);
	border: 1px solid rgba(255, 255, 255, 0.15);
}

/* 推文列表样式 */
.infinite-list {
	height: calc(100vh - 200px);
	border-radius: 12px;
	padding: 0;
	margin: 0;
	overflow-x: hidden !important;
	overflow-y: auto !important;
	list-style: none;
}

.infinite-list .infinite-list-item {
	margin-bottom: 16px;
	border-radius: 12px;
	transition: all 0.3s;
}

.infinite-list .infinite-list-item:hover {
	transform: translateY(-2px);
}

/* 卡片样式 */
.el-card {
	border: none;
	border-radius: 8px;
	transition: all 0.3s;
	background-color: rgba(255, 255, 255, 0.15);
	backdrop-filter: blur(4px);
	-webkit-backdrop-filter: blur(4px);
	border: 1px solid rgba(255, 255, 255, 0.15);
}

.el-card:hover {
	box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.1);
	background-color: rgba(255, 255, 255, 0.2);
	border: 1px solid rgba(255, 255, 255, 0.25);
}

.card-header {
	display: flex;
	justify-content: space-between;
	align-items: center;
	padding: 12px 20px;
	border-bottom: 1px solid rgba(255, 255, 255, 0.15);
	background-color: transparent;
	border-radius: 8px 8px 0 0;
	backdrop-filter: blur(4px);
	-webkit-backdrop-filter: blur(4px);
}

.card-header span {
	font-size: 16px;
	font-weight: 500;
	color: rgba(44, 62, 80, 0.8);
}

.card-actions {
	display: flex;
	gap: 12px;
}

.card-actions .el-button {
	color: rgba(52, 152, 219, 0.8);
	background-color: transparent;
	border: none;
	padding: 6px 12px;
	font-size: 14px;
	transition: all 0.3s;
}

.card-actions .el-button:hover {
	color: rgba(41, 128, 185, 0.9);
	background-color: rgba(255, 255, 255, 0.1);
}

.card-actions .el-button--danger {
	color: rgba(231, 76, 60, 0.8);
}

.card-actions .el-button--danger:hover {
	color: rgba(192, 57, 43, 0.9);
	background-color: rgba(255, 255, 255, 0.1);
}

/* 推文内容样式 */
.text.item {
	padding: 16px 20px;
	white-space: pre-line;
	line-height: 1.8;
	font-size: 15px;
	color: rgba(44, 62, 80, 0.7);
	max-height: 7.5em;
	overflow: hidden;
	text-overflow: ellipsis;
	display: -webkit-box;
	-webkit-line-clamp: 5;
	line-clamp: 5;
	-webkit-box-orient: vertical;
	background-color: transparent;
	backdrop-filter: blur(4px);
	-webkit-backdrop-filter: blur(4px);
}

/* 推文底部样式 */
.el-card__footer {
	padding: 12px 20px;
	background-color: transparent;
	border-top: 1px solid rgba(255, 255, 255, 0.15);
	color: rgba(127, 140, 141, 0.7);
	font-size: 14px;
	border-radius: 0 0 8px 8px;
	backdrop-filter: blur(4px);
	-webkit-backdrop-filter: blur(4px);
}

/* 对话框样式 */
.edit-dialog :deep(.el-dialog) {
	border-radius: 8px;
	overflow: hidden;
}

.edit-dialog :deep(.el-dialog__header) {
	margin: 0;
	padding: 20px;
	background-color: #f5f7fa;
	border-bottom: 1px solid #ebeef5;
}

.edit-dialog :deep(.el-dialog__title) {
	font-size: 18px;
	font-weight: 600;
	color: #303133;
}

.edit-dialog :deep(.el-dialog__body) {
	padding: 24px;
}

.dialog-header {
	margin-bottom: 24px;
}

.edit-time {
	margin: 8px 0 0;
	font-size: 13px;
	color: #909399;
}

/* 表单样式 */
.edit-form :deep(.el-form-item__label) {
	font-weight: 500;
	color: #606266;
}

.edit-form :deep(.el-input__wrapper) {
	border-radius: 4px;
	transition: all 0.3s;
}

.edit-form :deep(.el-textarea__inner) {
	border-radius: 4px;
	resize: none;
	line-height: 1.6;
	font-size: 14px;
}

.title-input :deep(.el-input__wrapper) {
	background-color: #f5f7fa;
}

.content-input :deep(.el-textarea__inner) {
	background-color: #f5f7fa;
	min-height: 120px;
}

.note-input :deep(.el-textarea__inner) {
	background-color: #f5f7fa;
	min-height: 80px;
}

/* 按钮样式 */
.dialog-footer {
	display: flex;
	justify-content: flex-end;
	gap: 12px;
	margin-top: 24px;
	padding-top: 16px;
	border-top: 1px solid #ebeef5;
}

.dialog-footer .el-button {
	padding: 8px 20px;
	font-size: 14px;
	border-radius: 4px;
}

.dialog-footer .cancel-btn {
	color: #606266;
	border-color: #dcdfe6;
}

.dialog-footer .cancel-btn:hover {
	color: var(--el-color-primary);
	border-color: var(--el-color-primary-light-5);
	background-color: var(--el-color-primary-light-9);
}

.dialog-footer .confirm-btn {
	background-color: var(--el-color-primary);
	border-color: var(--el-color-primary);
}

.dialog-footer .confirm-btn:hover {
	background-color: var(--el-color-primary-light-3);
	border-color: var(--el-color-primary-light-3);
}

/* 内容编辑与预览标签页 */
.content-tabs {
	margin-bottom: 24px;
}

.preview-container {
	background-color: #f5f7fa;
	border-radius: 6px;
	padding: 16px;
	min-height: 240px;
	max-height: 500px;
	overflow-y: auto;
}

.preview-content {
	font-size: 15px;
	line-height: 1.8;
	color: #303133;
}

.preview-content p {
	margin-bottom: 16px;
}

/* 代码块样式 */
.code-block {
	margin: 16px 0;
	border-radius: 6px;
	overflow: hidden;
	background-color: #282c34;
	box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

.code-block code {
	display: block;
	padding: 16px;
	font-family: 'Monaco', 'Menlo', 'Consolas', monospace;
	font-size: 14px;
	line-height: 1.5;
	overflow-x: auto;
}

/* 代码输入指南样式 */
.coding-guide {
	margin-top: 16px;
}

.guide-link {
	color: rgba(52, 152, 219, 0.8);
}

.guide-link:hover {
	color: rgba(41, 128, 185, 0.9);
}

.guide-content {
	padding: 16px;
}

.guide-content h4 {
	margin-bottom: 16px;
	font-size: 18px;
	font-weight: 600;
	color: #303133;
}

.guide-content p {
	margin-bottom: 16px;
	font-size: 14px;
	color: #606266;
}

.guide-content pre {
	background-color: #f5f7fa;
	padding: 16px;
	border-radius: 4px;
}

/* 详情对话框样式 */
.tweet-detail {
	padding: 24px;
}

.tweet-meta {
	margin-bottom: 24px;
	color: #909399;
	font-size: 14px;
}

.tweet-content {
	white-space: pre-line;
	line-height: 1.8;
	font-size: 15px;
	color: #303133;
}

.tweet-note {
	margin-top: 24px;
	padding-top: 16px;
	border-top: 1px solid #ebeef5;
	color: #909399;
	font-size: 14px;
}

/* 添加按钮样式 */
.action-bar .el-button--primary {
	background-color: rgba(52, 152, 219, 0.7);
	border: none;
	transition: all 0.3s;
}

.action-bar .el-button--primary:hover {
	background-color: rgba(41, 128, 185, 0.8);
}
</style>
