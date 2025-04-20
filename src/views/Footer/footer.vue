<template>
	<footer data-block-type="footers" data-id="6" class="fdb-block footer-large fp-active">
		<el-divider border-style="dashed" />
		<div class="container">
			<div class="row align-items-top">
				<div class="col-12 col-sm-6 col-md-4 col-lg-3 text-sm-left">
					<h3>
						<strong>网站统计</strong>
					</h3>
					<nav style="display: flex;flex-direction: column">
						<a class="nav-link active">已运行：{{ timePassed }}</a>
						<a class="nav-link">本月访问：{{ statistics.monthly_views }}</a>
						<a class="nav-link">总访问量：{{ statistics.total_views }}</a>
						<a class="nav-link">总阅读量：{{ statistics.total_reads }}</a>
						<a class="nav-link">总篇数：{{ statistics.total_articles }}</a>
						<a class="nav-link">总字数：{{ statistics.total_words }}</a>
					</nav>
				</div>
				<div class="col-12 col-sm-6 col-md-4 col-lg-3 mt-5 mt-sm-0 text-sm-left">
					<h3>
						<strong>网站项目指向</strong>
					</h3>
					<nav class="nav flex-column">
						<a href="https://github.com/MUlinGYS/Personal-Blog" class="nav-link active">GitHub</a>
					</nav>
				</div>
				<div class="col-12 col-md-4 col-lg-3 text-md-left mt-5 mt-md-0">
					<h3>
						<strong>关于CHENKAI.CN个人博客</strong>
					</h3>
					<p>
						欢迎访问我的个人博客网站，这是我创作，分享，思考和探索的地方。我试图使我的博客成为一个充满知识和智慧的资源库。<a style="color: red">该网站仅作为个人和分享使用</a>
					</p>
				</div>
				<div class="col-12 col-lg-2 ml-auto text-lg-left mt-4 mt-lg-0">
					<h3>
						<strong>联系作者</strong>
					</h3>
					<p class="text-h3">
						<!-- QQ -->

						<a plain @click="open"><svg t="1708396896464" class="icon" viewBox="0 0 1024 1024" version="1.1"
								xmlns="http://www.w3.org/2000/svg" p-id="3571" width="16" height="16">
								<path
									d="M824.8 613.2c-16-51.4-34.4-94.6-62.7-165.3C766.5 262.2 689.3 112 511.5 112 331.7 112 256.2 265.2 261 447.9c-28.4 70.8-46.7 113.7-62.7 165.3-34 109.5-23 154.8-14.6 155.8 18 2.2 70.1-82.4 70.1-82.4 0 49 25.2 112.9 79.8 159-26.4 8.1-85.7 29.9-71.6 53.8 11.4 19.3 196.2 12.3 249.5 6.3 53.3 6 238.1 13 249.5-6.3 14.1-23.8-45.3-45.7-71.6-53.8 54.6-46.2 79.8-110.1 79.8-159 0 0 52.1 84.6 70.1 82.4 8.5-1.1 19.5-46.4-14.5-155.8z"
									p-id="3572" fill="#515151"></path>
							</svg>
						</a>
						<!-- 微信 -->
						<a :plain="true" @click="openVn"><svg t="1708396816932" class="icon" viewBox="0 0 1024 1024"
								version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="2555" width="16" height="16">
								<path
									d="M664.250054 368.541681c10.015098 0 19.892049 0.732687 29.67281 1.795902-26.647917-122.810047-159.358451-214.077703-310.826188-214.077703-169.353083 0-308.085774 114.232694-308.085774 259.274068 0 83.708494 46.165436 152.460344 123.281791 205.78483l-30.80868 91.730191 107.688651-53.455469c38.558178 7.53665 69.459978 15.308661 107.924012 15.308661 9.66308 0 19.230993-0.470721 28.752858-1.225921-6.025227-20.36584-9.521864-41.723264-9.521864-63.862493C402.328693 476.632491 517.908058 368.541681 664.250054 368.541681zM498.62897 285.87389c23.200398 0 38.557154 15.120372 38.557154 38.061874 0 22.846334-15.356756 38.156018-38.557154 38.156018-23.107277 0-46.260603-15.309684-46.260603-38.156018C452.368366 300.994262 475.522716 285.87389 498.62897 285.87389zM283.016307 362.090758c-23.107277 0-46.402843-15.309684-46.402843-38.156018 0-22.941502 23.295566-38.061874 46.402843-38.061874 23.081695 0 38.46301 15.120372 38.46301 38.061874C321.479317 346.782098 306.098002 362.090758 283.016307 362.090758zM945.448458 606.151333c0-121.888048-123.258255-221.236753-261.683954-221.236753-146.57838 0-262.015505 99.348706-262.015505 221.236753 0 122.06508 115.437126 221.200938 262.015505 221.200938 30.66644 0 61.617359-7.609305 92.423993-15.262612l84.513836 45.786813-23.178909-76.17082C899.379213 735.776599 945.448458 674.90216 945.448458 606.151333zM598.803483 567.994292c-15.332197 0-30.807656-15.096836-30.807656-30.501688 0-15.190981 15.47546-30.477129 30.807656-30.477129 23.295566 0 38.558178 15.286148 38.558178 30.477129C637.361661 552.897456 622.099049 567.994292 598.803483 567.994292zM768.25071 567.994292c-15.213493 0-30.594809-15.096836-30.594809-30.501688 0-15.190981 15.381315-30.477129 30.594809-30.477129 23.107277 0 38.558178 15.286148 38.558178 30.477129C806.808888 552.897456 791.357987 567.994292 768.25071 567.994292z"
									fill="#5D5D5D" p-id="2556"></path>
							</svg>
						</a>
						<!-- 电脑 -->
						<el-tooltip class="box-item" effect="dark" content="宏碁-暗影骑士" placement="top">
							<a><svg t="1708397076908" class="icon" viewBox="0 0 1024 1024" version="1.1"
									xmlns="http://www.w3.org/2000/svg" p-id="6398" width="16" height="16">
									<path
										d="M554 849.574c0 23.365-18.635 42.307-42 42.307s-42-18.941-42-42.307V662.719c0-23.365 18.635-42.307 42-42.307v-7.051c23.365 0 42 25.993 42 49.358v186.855z"
										fill="#666666" p-id="6399"></path>
									<path
										d="M893 888.5c0 17.397-14.103 31.5-31.5 31.5h-700c-17.397 0-31.5-14.103-31.5-31.5s14.103-31.5 31.5-31.5h700c17.397 0 31.5 14.103 31.5 31.5zM926 174.426C926 135.484 894.686 105 855.744 105H168.256C129.314 105 98 135.484 98 174.426V533h828V174.426zM98 630.988C98 669.931 129.314 702 168.256 702h687.488C894.686 702 926 669.931 926 630.988V596H98v34.988z"
										fill="#666666" p-id="6400"></path>
								</svg>
							</a>
						</el-tooltip>
					</p>
				</div>
			</div>
			<div class="row mt-3">
				<div class="col text-center">
					© 2024 CHENKAI.CN. All Rights Reserved
				</div>
			</div>
		</div>
	</footer>
</template>

<script>
import { ref, computed, onMounted, onUnmounted, defineComponent, h } from 'vue';
import { ElMessage, ElMessageBox } from 'element-plus';
import axios from 'axios';

export default defineComponent({
	name: 'Footer',
	setup() {
		const startDateTime = new Date('2024-02-20T00:00:00Z');
		const startTime = ref(startDateTime.getTime());
		const statistics = ref({
			monthly_views: 0,
			total_views: 0,
			total_reads: 0,
			total_articles: 0,
			total_words: 0,
			tweet_count: 0,
			resource_count: 0,
			tech_tip_count: 0
		});

		const timePassed = computed(() => {
			const diffInSeconds = Math.floor(
				(new Date().getTime() - startTime.value) / 1000
			);
			const daysPassed = Math.floor(diffInSeconds / (24 * 60 * 60));
			const hoursPassed = Math.floor(diffInSeconds / (60 * 60)) % 24;
			return daysPassed + ' 天 - ' + hoursPassed + ' 小时';
		});

		let intervalId;

		onMounted(() => {
			intervalId = setInterval(() => {
				startTime.value = startDateTime.getTime();
			}, 1000);

			// 获取统计数据
			fetchStatistics();

			// 增加网站访问量
			incrementViewCount();
		});

		onUnmounted(() => {
			if (intervalId) {
				clearInterval(intervalId);
			}
		});

		// 获取统计数据
		const fetchStatistics = async () => {
			try {
				const response = await axios.get('http://localhost:5000/api/statistics');
				// 将后端返回的数据映射到前端需要的格式
				statistics.value = {
					monthly_views: response.data.monthly_views || 0,
					total_views: response.data.total_views || 0,
					total_reads: response.data.total_reads || 0,
					total_articles: response.data.total_articles || 0,
					total_words: response.data.total_words || 0,
					tweet_count: response.data.tweet_count || 0,
					resource_count: response.data.resource_count || 0,
					tech_tip_count: response.data.tech_tip_count || 0
				};
				console.log('获取到的统计数据:', statistics.value);
			} catch (error) {
				console.error('获取统计数据失败:', error);
			}
		};

		// 增加访问量
		const incrementViewCount = async () => {
			try {
				await axios.post('http://localhost:5000/api/view-count/website/1');
				// 增加访问量后重新获取统计数据
				await fetchStatistics();
			} catch (error) {
				console.error('增加访问量失败:', error);
			}
		};

		const open = () => {
			ElMessage({
				message: h('p', null, [
					h('span', null, 'QQ'),
					h('i', { style: 'color: teal' }, '3069394597'),
				]),
			});
		};

		const openVn = () => {
			ElMessage({
				message: h('p', null, [
					h('span', null, '微信 '),
					h('i', { style: 'color: teal' }, 'CK25he469'),
				]),
			});
		};

		return {
			timePassed,
			statistics,
			open,
			openVn
		};
	}
});
</script>

<style scoped>
* {
	box-sizing: border-box;
}

body {
	margin: 0;
}

footer {
	font-size: 16px;
	background-color: transparent;
	padding: 2rem 0;
	transition: all 0.3s ease;
}

footer a {
	color: #4a4a4a;
	text-decoration: none;
	transition: all 0.3s ease;
	position: relative;
}

footer a:hover {
	color: #1890ff;
}

footer .nav-link {
	display: inline-block;
	padding: 0.5rem 0rem;
	border-radius: 4px;
	transition: all 0.3s ease;
}

footer .nav-link:hover {
	background-color: rgba(24, 144, 255, 0.1);
}

.fdb-block .text-h3 {
	font-size: 1rem;
	margin: 0;
	font-weight: 400;
	display: flex;
	align-items: center;
	flex-wrap: nowrap;
	gap: 12px;
}

.fdb-block .text-h3 a {
	display: inline-flex;
	align-items: center;
	justify-content: center;
	width: 32px;
	height: 32px;
	border-radius: 50%;
	background-color: rgba(240, 240, 240, 0.8);
	transition: all 0.3s ease;
	margin: 0;
}

.fdb-block .text-h3 a:hover {
	background-color: rgba(230, 247, 255, 0.8);
	transform: scale(1.1);
}

.text-center {
	text-align: center;
	color: #666;
	font-size: 0.9rem;
}

.mt-3 {
	margin-top: 1.5rem;
	padding-top: 1rem;
	border-top: 1px solid rgba(238, 238, 238, 0.5);
}

h3 {
	font-size: 1.25rem;
	font-weight: 600;
	color: #333;
	margin-bottom: 1.2rem;
	position: relative;
	padding-bottom: 0.5rem;
}

h3::after {
	content: '';
	position: absolute;
	left: 0;
	bottom: 0;
	width: 40px;
	height: 3px;
	background-color: #1890ff;
	border-radius: 2px;
}

.container {
	max-width: 1200px;
	margin: 0 auto;
	padding: 0 1rem;
}

.row {
	display: flex;
	flex-wrap: wrap;
	margin: 0 -1rem;
	align-items: flex-start;
}

/* 列布局 */
.col-12 {
	flex: 0 0 100%;
	max-width: 100%;
	padding: 0 1rem;
}

.col-sm-6 {
	flex: 0 0 50%;
	max-width: 50%;
}

.col-md-4 {
	flex: 0 0 33.333333%;
	max-width: 33.333333%;
}

.col-lg-3 {
	flex: 0 0 25%;
	max-width: 25%;
}

.col-lg-2 {
	flex: 0 0 16.666667%;
	max-width: 16.666667%;
}

/* 响应式布局 */
@media (max-width: 768px) {
	footer {
		padding: 1.5rem 0;
	}

	.col-sm-6,
	.col-md-4,
	.col-lg-3,
	.col-lg-2 {
		flex: 0 0 100%;
		max-width: 100%;
		margin-bottom: 1.5rem;
	}

	.fdb-block .text-h3 {
		justify-content: center;
	}
}

/* 对齐方式 */
.text-sm-left {
	text-align: left;
}

.text-md-left {
	text-align: left;
}

.text-lg-left {
	text-align: left;
}

.ml-auto {
	margin-left: auto;
}

/* 间距调整 */
.mt-4 {
	margin-top: 1.5rem;
}

.mt-md-0 {
	margin-top: 0;
}

.mt-lg-0 {
	margin-top: 0;
}
</style>
