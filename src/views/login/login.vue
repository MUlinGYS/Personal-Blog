<template>
	<div id="login">
		<div id="contain">
			<div id="left_card" v-if="!isMobile">
				<h1>欢迎来到我的个人博客</h1>
				<span>Welcome to my Personal-Blog</span>
			</div>
			<div id="right_card">
				<el-card class="el-card">
					<h2>
						{{ isLogin ? "欢迎登录" : isCreate ? "新建账号" : "修改账号" }}
					</h2>
					<!-- 登录表单 -->
					<form v-if="isLogin" @submit.prevent="handleLogin" class="login">
						<input type="text" placeholder="请输入账号" autocomplete="username" v-model="account" />
						<input type="password" placeholder="请输入密码" autocomplete="current-password" v-model="password" />
						<div id="btn" style="margin-top: 20px">
							<button type="submit" class="loginbtn">登录</button>
						</div>
						<div class="action-links">
							<a @click="switchToCreate">新建账号</a>
							<a @click="switchToUpdate">修改账号</a>
						</div>
					</form>

					<!-- 新建账号表单 -->
					<form v-if="isCreate" @submit.prevent="handleCreate" class="login">
						<input type="text" placeholder="请输入新账号" v-model="createAccount" />
						<input type="password" placeholder="请输入新密码" v-model="createPassword" />
						<div id="btn" style="margin-top: 20px">
							<button type="submit" class="loginbtn">创建账号</button>
						</div>
						<div class="action-links">
							<a @click="switchToLogin">返回登录</a>
						</div>
					</form>

					<!-- 修改账号表单 -->
					<form v-if="isUpdate" @submit.prevent="handleUpdate" class="login">
						<input type="text" placeholder="请输入原账号" v-model="oldAccount" />
						<input type="password" placeholder="请输入原密码" v-model="oldPassword" />
						<input type="text" placeholder="请输入新账号" v-model="newAccount" />
						<input type="password" placeholder="请输入新密码" v-model="newPassword" />
						<div id="btn" style="margin-top: 20px">
							<button type="submit" class="loginbtn">修改账号</button>
						</div>
						<div class="action-links">
							<a @click="switchToLogin">返回登录</a>
						</div>
					</form>
				</el-card>
			</div>
		</div>
	</div>
</template>

<script setup>
import { ref, onUnmounted } from "vue";
import { useRouter } from "vue-router";
import Cookies from "js-cookie";
import { h } from "vue";
import { ElNotification } from "element-plus";
import request from "@/utils/request";

const account = ref("");
const password = ref("");
const createAccount = ref("");
const createPassword = ref("");
const oldAccount = ref("");
const oldPassword = ref("");
const newAccount = ref("");
const newPassword = ref("");
const router = useRouter();
const isMobile = ref(false);

// 表单状态
const isLogin = ref(true);
const isCreate = ref(false);
const isUpdate = ref(false);

function updateMobileView() {
	isMobile.value = window.innerWidth <= 768;
}

updateMobileView();
window.addEventListener("resize", updateMobileView);

onUnmounted(() => {
	window.removeEventListener("resize", updateMobileView);
});

const openNotification = (title, message, type = "error") => {
	ElNotification({
		title,
		message: h("i", { style: "color: teal" }, message),
		type,
	});
};

// 切换表单状态
const switchToLogin = () => {
	isLogin.value = true;
	isCreate.value = false;
	isUpdate.value = false;
};

const switchToCreate = () => {
	isLogin.value = false;
	isCreate.value = true;
	isUpdate.value = false;
};

const switchToUpdate = () => {
	isLogin.value = false;
	isCreate.value = false;
	isUpdate.value = true;
};

// 处理登录
const handleLogin = async () => {
	try {
		const response = await request.post("/login", {
			username: account.value,
			password: password.value,
		});
		const res = response.data;  // 获取实际的响应数据
		if (res.success) {
			const token = res.token;
			Cookies.set("token", token);
			openNotification("成功", "登录成功", "success");
			router.push("/index");
		} else {
			console.log(res);
			openNotification("警告", res.message);
		}
	} catch (error) {
		if (error.response?.data?.message) {
			openNotification("错误", error.response.data.message);
		} else {
			openNotification("错误", "登录失败，请检查网络连接");
		}
	}
};

// 处理新建账号
const handleCreate = async () => {
	try {
		const res = await request.post("/user", {
			username: createAccount.value,
			password: createPassword.value,
		});
		if (res.success) {
			openNotification("成功", "账号创建成功", "success");
			switchToLogin();
		} else {
			openNotification("警告", res.message);
		}
	} catch (error) {
		if (error.response?.data?.message) {
			openNotification("错误", error.response.message);
		} else {
			openNotification("错误", "创建账号失败，请检查网络连接");
		}
	}
};

// 处理修改账号
const handleUpdate = async () => {
	try {
		const res = await request.put("/user", {
			old_username: oldAccount.value,
			old_password: oldPassword.value,
			new_username: newAccount.value,
			new_password: newPassword.value,
		});
		if (res.success) {
			openNotification("成功", "账号修改成功", "success");
			switchToLogin();
		} else {
			openNotification("警告", res.message);
		}
	} catch (error) {
		if (error.response?.data?.message) {
			openNotification("错误", error.response.message);
		} else {
			openNotification("错误", "修改账号失败，请检查网络连接");
		}
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
	background-image: url("/src/assets/gif/login.gif");
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
		color: white;
		border: none;
		cursor: pointer;
	}

	.action-links {
		display: flex;
		justify-content: space-between;
		margin-top: 15px;
		padding: 0 20px;

		a {
			color: white;
			text-decoration: none;
			cursor: pointer;
			font-size: 14px;

			&:hover {
				text-decoration: underline;
			}
		}
	}
}
</style>
