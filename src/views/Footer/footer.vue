<template>
	<footer
		data-block-type="footers"
		data-id="6"
		class="fdb-block footer-large fp-active"
	>
		<el-divider border-style="dashed" />
		<div class="container">
			<div class="row align-items-top">
				<div class="col-12 col-sm-6 col-md-4 col-lg-3 text-sm-left">
					<h3>
						<strong>网站统计</strong>
					</h3>
					<nav class="nav flex-column">
						<a class="nav-link active">已运行：{{ timePassed }}</a>
						<a class="nav-link">今日访问：</a>
						<a class="nav-link">昨日访问：</a>
						<a class="nav-link">本月访问：</a>
						<a class="nav-link">总访问量：</a>
						<a class="nav-link">总字数：</a>
						<a class="nav-link">阅读时间：</a>
						<a class="nav-link">最后阅读时间：</a>
					</nav>
				</div>
				<div
					class="col-12 col-sm-6 col-md-4 col-lg-3 mt-5 mt-sm-0 text-sm-left"
				>
					<h3>
						<strong>网站项目指向</strong>
					</h3>
					<nav class="nav flex-column">
						<a
							href="https://github.com/MUlinGYS/"
							class="nav-link active"
							>GitHub</a
						>
						<a class="nav-link">GitHub</a>
						<a class="nav-link">GitHub</a>
						<a class="nav-link">GitHub</a>
						<a class="nav-link">GitHub</a>
					</nav>
				</div>
				<div class="col-12 col-md-4 col-lg-3 text-md-left mt-5 mt-md-0">
					<h3>
						<strong>关于CHENKAI.CN个人博客</strong>
					</h3>
					<p>
						欢迎访问我的个人博客网站，这是我创作，分享，思考和探索的地方。我试图使我的博客成为一个充满知识和智慧的资源库。<a
							style="color: red"
							>该网站仅作为个人和分享使用</a
						>
					</p>
				</div>
				<div class="col-12 col-lg-2 ml-auto text-lg-left mt-4 mt-lg-0">
					<h3>
						<strong>联系作者</strong>
					</h3>
					<p class="text-h3">
						<!-- QQ -->

						<a
							plain
							@click="open"
							><svg
								t="1708396896464"
								class="icon"
								viewBox="0 0 1024 1024"
								version="1.1"
								xmlns="http://www.w3.org/2000/svg"
								p-id="3571"
								width="16"
								height="16"
							>
								<path
									d="M824.8 613.2c-16-51.4-34.4-94.6-62.7-165.3C766.5 262.2 689.3 112 511.5 112 331.7 112 256.2 265.2 261 447.9c-28.4 70.8-46.7 113.7-62.7 165.3-34 109.5-23 154.8-14.6 155.8 18 2.2 70.1-82.4 70.1-82.4 0 49 25.2 112.9 79.8 159-26.4 8.1-85.7 29.9-71.6 53.8 11.4 19.3 196.2 12.3 249.5 6.3 53.3 6 238.1 13 249.5-6.3 14.1-23.8-45.3-45.7-71.6-53.8 54.6-46.2 79.8-110.1 79.8-159 0 0 52.1 84.6 70.1 82.4 8.5-1.1 19.5-46.4-14.5-155.8z"
									p-id="3572"
									fill="#515151"
								></path>
							</svg>
						</a>
						<!-- 微信 -->
						<a
							:plain="true"
							@click="openVn"
							><svg
								t="1708396816932"
								class="icon"
								viewBox="0 0 1024 1024"
								version="1.1"
								xmlns="http://www.w3.org/2000/svg"
								p-id="2555"
								width="16"
								height="16"
							>
								<path
									d="M664.250054 368.541681c10.015098 0 19.892049 0.732687 29.67281 1.795902-26.647917-122.810047-159.358451-214.077703-310.826188-214.077703-169.353083 0-308.085774 114.232694-308.085774 259.274068 0 83.708494 46.165436 152.460344 123.281791 205.78483l-30.80868 91.730191 107.688651-53.455469c38.558178 7.53665 69.459978 15.308661 107.924012 15.308661 9.66308 0 19.230993-0.470721 28.752858-1.225921-6.025227-20.36584-9.521864-41.723264-9.521864-63.862493C402.328693 476.632491 517.908058 368.541681 664.250054 368.541681zM498.62897 285.87389c23.200398 0 38.557154 15.120372 38.557154 38.061874 0 22.846334-15.356756 38.156018-38.557154 38.156018-23.107277 0-46.260603-15.309684-46.260603-38.156018C452.368366 300.994262 475.522716 285.87389 498.62897 285.87389zM283.016307 362.090758c-23.107277 0-46.402843-15.309684-46.402843-38.156018 0-22.941502 23.295566-38.061874 46.402843-38.061874 23.081695 0 38.46301 15.120372 38.46301 38.061874C321.479317 346.782098 306.098002 362.090758 283.016307 362.090758zM945.448458 606.151333c0-121.888048-123.258255-221.236753-261.683954-221.236753-146.57838 0-262.015505 99.348706-262.015505 221.236753 0 122.06508 115.437126 221.200938 262.015505 221.200938 30.66644 0 61.617359-7.609305 92.423993-15.262612l84.513836 45.786813-23.178909-76.17082C899.379213 735.776599 945.448458 674.90216 945.448458 606.151333zM598.803483 567.994292c-15.332197 0-30.807656-15.096836-30.807656-30.501688 0-15.190981 15.47546-30.477129 30.807656-30.477129 23.295566 0 38.558178 15.286148 38.558178 30.477129C637.361661 552.897456 622.099049 567.994292 598.803483 567.994292zM768.25071 567.994292c-15.213493 0-30.594809-15.096836-30.594809-30.501688 0-15.190981 15.381315-30.477129 30.594809-30.477129 23.107277 0 38.558178 15.286148 38.558178 30.477129C806.808888 552.897456 791.357987 567.994292 768.25071 567.994292z"
									fill="#5D5D5D"
									p-id="2556"
								></path>
							</svg>
						</a>
						<!-- 电话 -->
						<el-tooltip
							class="box-item"
							effect="dark"
							content="17780527570"
							placement="top"
						>
							<a
								><svg
									t="1708397010931"
									class="icon"
									viewBox="0 0 1024 1024"
									version="1.1"
									xmlns="http://www.w3.org/2000/svg"
									p-id="4827"
									width="16"
									height="16"
								>
									<path
										d="M747.294464 958.409274 288.099005 958.409274c-34.171196 0-61.928321-27.873782-61.928321-62.107399L226.170684 127.335876c0-34.298085 27.757125-62.171867 61.928321-62.171867l459.195459 0c34.117984 0 61.871016 27.873782 61.871016 62.171867L809.165479 896.301875C809.165479 930.535492 781.412448 958.409274 747.294464 958.409274L747.294464 958.409274zM288.099005 95.594004c-17.351145 0-31.498325 14.234161-31.498325 31.741872L256.60068 896.301875c0 17.472918 14.14718 31.678427 31.498325 31.678427l459.195459 0c17.356262 0 31.44102-14.205508 31.44102-31.678427L778.735484 127.335876c0-17.506687-14.084758-31.741872-31.44102-31.741872L288.099005 95.594004 288.099005 95.594004zM517.698781 891.844362c-22.345893 0-40.477819-18.217884-40.477819-40.593452s18.131926-40.594476 40.477819-40.594476c22.347939 0 40.473726 18.218907 40.473726 40.594476S540.04672 891.844362 517.698781 891.844362L517.698781 891.844362zM517.698781 841.086429c-5.526866 0-10.041684 4.548587-10.041684 10.16448 0 11.233833 20.086437 11.233833 20.086437 0C527.742511 845.635016 523.22667 841.086429 517.698781 841.086429L517.698781 841.086429zM735.644146 781.295791l-438.629092 0c-8.377791 0-15.21244-6.804973-15.21244-15.216533L281.802614 150.451293c0-8.407467 6.834648-15.21244 15.21244-15.21244l438.629092 0c8.382908 0 15.216533 6.804973 15.216533 15.21244l0 615.627965C750.860679 774.490818 744.027054 781.295791 735.644146 781.295791L735.644146 781.295791zM312.23261 750.866819l408.199097 0L720.431706 165.668849 312.23261 165.668849 312.23261 750.866819 312.23261 750.866819zM312.23261 750.866819"
										fill="#272636"
										p-id="4828"
									></path>
								</svg>
							</a>
						</el-tooltip>
						<!-- 电脑 -->
						<el-tooltip
							class="box-item"
							effect="dark"
							content="宏碁-暗影骑士"
							placement="top"
						>
							<a
								><svg
									t="1708397076908"
									class="icon"
									viewBox="0 0 1024 1024"
									version="1.1"
									xmlns="http://www.w3.org/2000/svg"
									p-id="6398"
									width="16"
									height="16"
								>
									<path
										d="M554 849.574c0 23.365-18.635 42.307-42 42.307s-42-18.941-42-42.307V662.719c0-23.365 18.635-42.307 42-42.307v-7.051c23.365 0 42 25.993 42 49.358v186.855z"
										fill="#666666"
										p-id="6399"
									></path>
									<path
										d="M893 888.5c0 17.397-14.103 31.5-31.5 31.5h-700c-17.397 0-31.5-14.103-31.5-31.5s14.103-31.5 31.5-31.5h700c17.397 0 31.5 14.103 31.5 31.5zM926 174.426C926 135.484 894.686 105 855.744 105H168.256C129.314 105 98 135.484 98 174.426V533h828V174.426zM98 630.988C98 669.931 129.314 702 168.256 702h687.488C894.686 702 926 669.931 926 630.988V596H98v34.988z"
										fill="#666666"
										p-id="6400"
									></path>
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

<script setup lang="ts" name="Header">
	import '../../assets/page.min.css';

	import { ref, computed, onMounted, onUnmounted } from 'vue';

	//运行时间
	// 可以在这里设置起始时间戳
	const startDateTime = new Date('2024-02-20T00:00:00Z');
	const startTime = ref(startDateTime.getTime());

	const timePassed = computed(() => {
		const diffInSeconds = Math.floor(
			(new Date().getTime() - startTime.value) / 1000
		);
		const daysPassed = Math.floor(diffInSeconds / (24 * 60 * 60));
		const hoursPassed = Math.floor(diffInSeconds / (60 * 60)) % 24;
		return daysPassed + ' 天 - ' + hoursPassed + ' 小时';
	});

	let intervalId: ReturnType<typeof setInterval>;

	onMounted(() => {
		intervalId = setInterval(() => {
			startTime.value = startDateTime.getTime();
		}, 1000);
	});

	onUnmounted(() => {
		if (intervalId) {
			clearInterval(intervalId);
		}
	});

	// QQ弹框
	import { ElMessage, ElMessageBox } from 'element-plus';
	import img from '@/assets/img/avatar.jpeg';

	const open = () => {
		ElMessageBox.alert(
			`<img src="${img}" alt="3069394597"  width="396" height="300"/>`,
			'二维码暂替',
			{
				// if you want to disable its autofocus
				autofocus: false,
				confirmButtonText: 'OK',
				dangerouslyUseHTMLString: true, // 为了能够解析 HTML 设定这个选项为true
				callback: () => {
					ElMessage({
						type: 'info',
						message: `已退出`,
					});
				},
			}
		);
	};

	//微信提示
	import { h } from 'vue';

	const openVn = () => {
		ElMessage({
			message: h('p', null, [
				h('span', null, '作者未 '),
				h('i', { style: 'color: teal' }, '添加'),
			]),
		});
	};
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
	}
	footer a {
		color: rgb(68, 68, 68);
	}
	footer a:hover {
		color: rgb(0, 86, 179);
	}
	footer .nav-link {
		display: block;
		padding-top: 0.5rem;
		padding-right: 1rem;
		padding-bottom: 0.5rem;
		padding-left: 0px;
		text-decoration-line: none;
		text-decoration-thickness: initial;
		text-decoration-style: initial;
		text-decoration-color: initial;
	}
	.fdb-block .text-h3 {
		font-size: 0.875rem;
		margin-bottom: 0.5em;
		margin-top: 0.3em;
		font-weight: 400;
	}
	.fdb-block .text-h3 a {
		margin-right: 12px;
	}
	.text-center {
		text-align: center;
	}
	.mt-3 {
		margin-top: 1rem;
	}
	h3 {
		font-size: 18px;
	}
</style>
