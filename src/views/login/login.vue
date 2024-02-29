<template>
	<div id="login">
		<div id="contain">
			<div
				id="left_card"
				v-if="!isMobile"
			>
				<h1>欢迎来到我的个人博客</h1>
				<span>Welcome to my Personal-Blog</span>
			</div>
			<div id="right_card">
				<el-card class="el-card">
					<h2>欢迎登录</h2>
					<form
						@submit.prevent="handleLogin"
						class="login"
					>
						<input
							type="text"
							placeholder="请输入账号"
							autocomplete="username"
							v-model="account"
						/>
						<input
							type="password"
							placeholder="请输入密码"
							autocomplete="current-password"
							v-model="password"
						/>
						<div
							id="btn"
							style="margin-top: 20px"
						>
							<button
								type="submit"
								class="loginbtn"
							>
								登陆
							</button>
						</div>
					</form>
				</el-card>
			</div>
		</div>
	</div>
</template>

<script lang="ts" setup name="appLogin">
	import { ref, onUnmounted } from 'vue';
	import { useRouter } from 'vue-router';
	import { getUsers } from './../../api/detailed.js';
	import Cookies from 'js-cookie';
	import { h } from 'vue';
	import { ElNotification } from 'element-plus';

	const account = ref('');
	const password = ref('');
	const router = useRouter();
	const isMobile = ref(false);

	function updateMobileView() {
		isMobile.value = window.innerWidth <= 768;
	}

	updateMobileView();
	window.addEventListener('resize', updateMobileView);

	onUnmounted(() => {
		window.removeEventListener('resize', updateMobileView);
	});

	const open1 = () => {
		ElNotification({
			title: '警告',
			message: h('i', { style: 'color: teal' }, '密码或账户错误'),
		});
	};

	const handleLogin = async () => {
		try {
			const response = await getUsers();

			// 从相应数据中获取用户数组
			// @ts-ignore
			const users = response.data.account;

			const user = users.find(
				(user: { account: string; password: string }) =>
					user.account === account.value && user.password === password.value
			);

			if (user) {
				const token = Math.random().toString(36).substring(2, 18); // 生成一个随机 token，长度为16
				console.log('生成的 token：', token);
				Cookies.set('token', token); // 将生成的 token 存入 cookie
				router.push('/index');
			} else {
				// 否则，提示用户账号或密码错误
				open1();
			}
		} catch (error) {
			console.error(error);
		}
	};
</script>

<style lang="less" scoped>
	@keyframes animate {
		0% {
			filter: hue-rotate(0deg);
		}
		100% {
			filter: hue-rotate(360deg);
		}
	}
	#login {
		position: relative;
		width: 100vw;
		height: 100vh;
		overflow: auto;
		background-image: url('/src/assets/gif/login.gif');
		background-size: 100% 100%;
		background-color: #a7a8bd;
		#contain {
			height: 400px;
			position: absolute;
			top: 50%;
			left: 50%;
			transform: translate(-50%, -50%);
			border-radius: 25px;
			border: 1px solid black;
			background-color: rgba(255, 255, 255, 0.1) !important;
			backdrop-filter: blur(5px);
		}
	}
	#contain {
		display: flex;
		flex-direction: row;
		text-align: center;
		align-items: center;
		#left_card {
			width: 550px;
			h1 {
				color: white;
				white-space: nowrap;
			}
			span {
				font-size: 1.2rem;
				text-align: center;
				color: white;
				white-space: nowrap;
			}
		}
		#right_card {
			width: 350px;
			.el-card {
				margin: 0 45px;
				border-radius: 25px;
				background-color: rgba(255, 255, 255, 0.1);
			}
		}
	}
	#right_card {
		display: flex;
		justify-content: center;
		align-items: center;
		h2 {
			margin-bottom: 0px;
		}
		.login {
			input {
				width: 80%;
				height: 45px;
				margin-top: 10px;
				border: 1px solid white;
				background-color: rgba(255, 255, 255, 0.5);
				border-radius: 10px;
				font-size: inherit;
				padding-left: 20px;
				outline: none;
			}
		}

		.loginbtn {
			width: 100%;
			height: 35px;
			margin-top: 10px;
			border-radius: 10px;
			background-color: rgba(207, 38, 38, 0.8);
		}
	}
</style>
