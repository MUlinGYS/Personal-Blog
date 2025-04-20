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
				<el-button type="primary" @click="openResourceDialog()">添加资源</el-button>
			</div>
		</div>

		<!-- 资源列表容器 -->
		<div class="tweets-container">
			<ul v-infinite-scroll="load" class="infinite-list" style="overflow: auto" infinite-scroll-distance="10px">
				<li v-for="resource in resources" :key="resource.id" class="infinite-list-item">
					<el-card shadow="hover" style="width: 100%">
						<template #header>
							<div class="card-header">
								<span>{{ formatDate(resource.created_at) }} ------- {{ resource.name }}</span>
								<div class="card-actions">
									<el-button type="primary" link @click="openResourceUrl(resource.url)">
										<el-icon>
											<Link />
										</el-icon>
										访问链接
									</el-button>
									<el-button type="primary" link @click="openResourceDialog(resource)">编辑</el-button>
									<el-button type="danger" link @click="handleDelete(resource)">删除</el-button>
								</div>
							</div>
						</template>
						<div class="text item">
							{{ truncateContent(resource.url) }}
						</div>
						<template #footer>备注: {{ resource.note || '无' }}</template>
					</el-card>
				</li>
			</ul>
		</div>

		<!-- 资源详情对话框 -->
		<el-dialog v-model="detailDialogVisible" :title="currentResource?.name" width="60%">
			<div class="tweet-detail">
				<div class="tweet-meta">
					<span class="time">发布时间：{{ formatDate(currentResource?.created_at) }}</span>
				</div>
				<div class="tweet-content">
					{{ currentResource?.url }}
				</div>
				<div class="tweet-note" v-if="currentResource?.note">
					<el-divider content-position="left">备注</el-divider>
					{{ currentResource.note }}
				</div>
			</div>
		</el-dialog>

		<!-- 添加/编辑资源对话框 -->
		<el-dialog v-model="resourceDialogVisible" :title="isEdit ? '编辑资源' : '添加资源'" width="50%" class="edit-dialog">
			<div class="dialog-header">
				<p class="edit-time" v-if="isEdit">最后编辑时间：{{ formatDate(resourceData.updated_at) }}</p>
			</div>
			<el-form :model="resourceData" label-width="80px" class="edit-form">
				<el-form-item label="名称" required>
					<el-input v-model="resourceData.name" placeholder="请输入资源名称" class="title-input" :maxlength="100"
						show-word-limit></el-input>
				</el-form-item>
				<el-form-item label="URL" required>
					<el-input v-model="resourceData.url" type="textarea" rows="6" placeholder="请输入资源URL"
						class="content-input" :maxlength="100000" show-word-limit></el-input>
				</el-form-item>
				<el-form-item label="备注">
					<el-input v-model="resourceData.note" type="textarea" rows="2" placeholder="请输入备注（可选）"
						class="note-input" :maxlength="1000" show-word-limit></el-input>
				</el-form-item>
			</el-form>
			<template #footer>
				<span class="dialog-footer">
					<el-button @click="resourceDialogVisible = false" class="cancel-btn">取消</el-button>
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
import { Search, Refresh, Link } from '@element-plus/icons-vue';
import axios from 'axios';

// 搜索查询
const searchQuery = ref('');
// 防抖定时器
let searchTimer = null;

// 当前页码
const currentPage = ref(1);
// 每页数量
const perPage = 10;

// 资源列表数据
const resources = ref([]);
// 对话框显示状态
const resourceDialogVisible = ref(false);
// 详情对话框显示状态
const detailDialogVisible = ref(false);
// 当前查看的资源
const currentResource = ref(null);
// 是否为编辑模式
const isEdit = ref(false);
// 资源表单数据
const resourceData = ref({
	id: null,
	name: '',
	url: '',
	note: ''
});

// 加载状态
const loading = ref(false);
// 是否还有更多数据
const hasMore = ref(true);

// 加载资源列表
const loadResources = async () => {
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

		const response = await axios.get('http://localhost:5000/api/resources', { params });
		const { items, total, pages } = response.data;

		// 如果搜索模式下，直接替换数据
		if (searchQuery.value || currentPage.value === 1) {
			resources.value = items;
		} else {
			// 非搜索模式下，追加数据
			resources.value = [...resources.value, ...items];
		}

		// 更新是否有更多数据
		hasMore.value = currentPage.value < pages;
		// 如果还有更多数据，增加页码
		if (hasMore.value) {
			currentPage.value++;
		}
	} catch (error) {
		ElMessage.error('加载资源失败');
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
		loadResources();
	}, 300);
};

// 打开资源对话框
const openResourceDialog = (resource = null) => {
	isEdit.value = !!resource;
	if (resource) {
		resourceData.value = {
			id: resource.id,
			name: resource.name,
			url: resource.url,
			note: resource.note,
			updated_at: resource.updated_at
		};
	} else {
		resourceData.value = {
			id: null,
			name: '',
			url: '',
			note: ''
		};
	}
	resourceDialogVisible.value = true;
};

// 提交表单
const handleSubmit = async () => {
	try {
		if (isEdit.value) {
			await axios.put(`http://localhost:5000/api/resources/${resourceData.value.id}`, {
				name: resourceData.value.name,
				url: resourceData.value.url,
				note: resourceData.value.note
			});
			ElMessage.success('修改资源成功');
		} else {
			await axios.post('http://localhost:5000/api/resources', {
				name: resourceData.value.name,
				url: resourceData.value.url,
				note: resourceData.value.note
			});
			ElMessage.success('添加资源成功');
		}
		resourceDialogVisible.value = false;
		loadResources();
	} catch (error) {
		ElMessage.error(isEdit.value ? '修改资源失败' : '添加资源失败');
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

// 显示资源详情
const showResourceDetail = (resource) => {
	currentResource.value = resource;
	detailDialogVisible.value = true;
};

// 删除资源
const handleDelete = (resource) => {
	ElMessageBox.confirm(
		'确定要删除这个资源吗？',
		'删除确认',
		{
			confirmButtonText: '确定',
			cancelButtonText: '取消',
			type: 'warning',
		}
	).then(async () => {
		try {
			await axios.delete(`http://localhost:5000/api/resources/${resource.id}`);
			ElMessage.success('删除资源成功');
			// 重新加载资源列表
			currentPage.value = 1;
			loadResources();
		} catch (error) {
			ElMessage.error('删除资源失败');
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
	loadResources();
};

// 刷新资源列表
const handleRefresh = () => {
	currentPage.value = 1;
	searchQuery.value = '';
	resources.value = []; // 清空现有数据
	hasMore.value = true; // 重置加载更多状态
	loadResources();
};

// 打开资源URL
const openResourceUrl = (url) => {
	window.open(url, '_blank');
};

// 组件挂载时加载资源
onMounted(() => {
	loadResources();
});
</script>

<style scoped>
/* 父容器样式 */
.tweets-wrapper {
	padding: 24px;
	min-height: 100vh;
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

/* 资源列表容器 */
.tweets-container {
	background-color: rgba(255, 255, 255, 0.15);
	border-radius: 12px;
	padding: 24px;
	box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.1);
	backdrop-filter: blur(8px);
	-webkit-backdrop-filter: blur(8px);
	border: 1px solid rgba(255, 255, 255, 0.15);
}

/* 资源列表样式 */
.infinite-list {
	height: calc(100vh - 200px);
	border-radius: 12px;
	padding: 0;
	margin: 0;
	overflow-x: hidden !important;
	overflow-y: auto !important;
	list-style: none;
}

.infinite-list::-webkit-scrollbar {
	width: 6px;
}

.infinite-list::-webkit-scrollbar-thumb {
	background-color: #dcdfe6;
	border-radius: 3px;
}

.infinite-list::-webkit-scrollbar-track {
	background-color: #f5f7fa;
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
	display: flex;
	align-items: center;
	gap: 4px;
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

/* 资源内容样式 */
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

/* 资源底部样式 */
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
