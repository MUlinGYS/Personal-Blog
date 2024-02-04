<template>
	<div id="login">
		<div id="contain">
			<div id="left_card">
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
						<input
							type="radio"
							id="psd"
							class="radio"
						/><label for="psd"></label>记住密码
					</div>
					<div class="message">
						<span></span>
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
<script lang="ts" setup name="appLogin"></script>

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
			width: 500px;
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
			width: 400px;
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
			margin-bottom: 5px;
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
			float: right;
			height: 26px;
			text-align: center;
			font-size: 1rem;
			position: relative;
			.radio {
				height: 1rem;
				width: 1rem;
				vertical-align: middle;
				margin-top: -2px;
				opacity: 0;
			}
			label {
				position: absolute;
				left: -2px;
				top: 5px;
				height: 1rem;
				width: 1rem;
				vertical-align: middle;
				margin-top: -2px;
				border-radius: 50%;
				border: 1px solid black;
			}
			//radio选中后修改labe内的内容 :after 选择器在被选元素的内容后面插入内容。
			input:checked + label::after {
				content: '';
				width: 0.6rem;
				height: 0.6rem;
				position: absolute;
				left: 50%;
				top: 50%;
				transform: translate(-50%, -50%);
				border-radius: 50%;
				background-color: rgba(207, 38, 38, 0.8);
				border: 1px solid rgba(207, 38, 38, 0.8);
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
