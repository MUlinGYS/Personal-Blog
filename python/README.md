# 个人博客后端 API

这是一个基于 Flask 和 SQLite 的个人博客后端 API 项目。

## 功能特点

- 用户管理（登录、修改账号、新建账号）
- 推文管理
- 资源链接管理
- 技术锦囊管理
- 归档管理

## 安装依赖

```bash
pip install -r requirements.txt
```

## 运行项目

```bash
python app.py
```

服务器将在 http://localhost:5000 启动

## API 接口说明

### 用户相关

- POST /api/login - 用户登录
- PUT /api/user - 修改账号
- POST /api/user - 新建账号

### 推文相关

- POST /api/tweets - 创建推文
- GET /api/tweets - 获取所有推文

### 资源链接相关

- POST /api/resources - 创建资源链接
- GET /api/resources - 获取所有资源链接

### 技术锦囊相关

- POST /api/tech-tips - 创建技术锦囊
- GET /api/tech-tips - 获取所有技术锦囊

### 归档相关

- POST /api/archives - 创建归档
- GET /api/archives - 获取所有归档

## 默认管理员账号

- 用户名：admin
- 密码：admin
