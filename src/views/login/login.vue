<template>
	<div id="login">
		<div id="contain">
			<div
				id="left_card"
				v-if="!isMobile"
			>
				<h1>欢迎来到我的Personal-Blog</h1>
				<span>Welcome to my Personal-Blog</span>
			</div>
			<div id="right_card">
				<el-card class="el-card">
					<h2>欢迎登录</h2>
					<div class="login">
						<input
							type="text"
							placeholder="请输入账号"
						/>
						<input
							type="password"
							placeholder="请输入密码"
						/>
					</div>
					<div class="remember">
						<div style="height: 31px; display: flex; align-items: center">
							<input
								type="checkbox"
								id="remember-me"
							/>
						</div>
						<div
							style="
								height: 31px;
								display: flex;
								align-items: center;
								margin-left: 5px;
							"
						>
							<label for="remember-me">记住我</label>
						</div>
					</div>

					<div id="btn">
						<router-link to="/index">
							<button class="loginbtn">登陆</button>
						</router-link>
					</div>
				</el-card>
			</div>
		</div>
	</div>
</template>

<script lang="ts" setup name="appLogin">
	import { ref, onUnmounted } from 'vue';

	const isMobile = ref(false);

	function updateMobileView() {
		isMobile.value = window.innerWidth <= 768;
	}

	updateMobileView();
	window.addEventListener('resize', updateMobileView);

	onUnmounted(() => {
		window.removeEventListener('resize', updateMobileView);
	});
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
		.remember {
			display: flex;
			align-items: center;
			justify-content: flex-end;

			label {
				margin: 0 !important;
			}

			#remember-me {
				appearance: none; /* Clear browser default styles */
				width: 12px;
				height: 12px;
				background: #fff;
				border: 1px solid;
				border-radius: 50%;
				outline: none;
				position: relative;
			}

			#remember-me:before {
				content: '';
				position: absolute;
				top: 50%;
				left: 50%;
				transform: translate(-50%, -50%);
				width: 10px;
				height: 10px;
				border-radius: 50%;
				background: transparent;
				transition: background 0.3s ease;
			}

			#remember-me:checked:before {
				background: #333;
			}
		}
		.message {
			margin-top: 26px;
			font-size: 0.9rem;
			color: red;
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
