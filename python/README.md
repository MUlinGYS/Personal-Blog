# 个人博客后端 API

这是一个基于 Flask 和 SQLite 的个人博客后端 API 项目，提供了完整的博客管理功能。

## 技术栈

- Flask：轻量级 Web 框架
- SQLAlchemy：ORM 数据库工具
- SQLite：轻量级数据库
- Flask-CORS：处理跨域请求

## 功能特点

- 用户管理
  - 用户登录
  - 修改账号信息
  - 创建新账号
- 推文管理
  - 创建推文
  - 获取推文列表
  - 搜索推文
  - 修改推文
- 资源链接管理
  - 创建资源链接
  - 获取资源列表
- 技术锦囊管理
  - 创建技术锦囊
  - 获取技术锦囊列表
- 归档管理
  - 创建归档
  - 获取归档列表
  - 将推文、资源、技术锦囊添加到归档

## 安装依赖

```bash
pip install -r requirements.txt
```

## 初始化数据库

```bash
python init_db.py
```

## 运行项目

```bash
python app.py
```

服务器将在 http://localhost:5000 启动

## API 接口文档

### 用户相关接口

#### 用户登录

- **接口**：`POST /api/login`
- **请求体**：
  ```json
  {
    "username": "用户名",
    "password": "密码"
  }
  ```
- **响应**：
  ```json
  {
    "success": true,
    "message": "登录成功",
    "token": "登录令牌"
  }
  ```

#### 修改账号

- **接口**：`PUT /api/user`
- **请求体**：
  ```json
  {
    "old_username": "原用户名",
    "old_password": "原密码",
    "new_username": "新用户名",
    "new_password": "新密码"
  }
  ```

#### 创建账号

- **接口**：`POST /api/user`
- **请求体**：
  ```json
  {
    "username": "用户名",
    "password": "密码"
  }
  ```

### 推文相关接口

#### 创建推文

- **接口**：`POST /api/tweets`
- **请求体**：
  ```json
  {
    "title": "推文标题",
    "content": "推文内容",
    "note": "备注（可选）"
  }
  ```

#### 获取推文列表

- **接口**：`GET /api/tweets`
- **查询参数**：
  - `search`：搜索关键词（可选）
- **响应**：
  ```json
  [
    {
      "id": 1,
      "title": "推文标题",
      "content": "推文内容",
      "note": "备注",
      "created_at": "创建时间",
      "updated_at": "更新时间"
    }
  ]
  ```

#### 修改推文

- **接口**：`PUT /api/tweets/<tweet_id>`
- **请求体**：
  ```json
  {
    "title": "新标题",
    "content": "新内容",
    "note": "新备注"
  }
  ```

### 资源链接相关接口

#### 创建资源链接

- **接口**：`POST /api/resources`
- **请求体**：
  ```json
  {
    "name": "资源名称",
    "url": "资源链接",
    "note": "备注（可选）"
  }
  ```

#### 获取资源列表

- **接口**：`GET /api/resources`
- **响应**：
  ```json
  [
    {
      "id": 1,
      "name": "资源名称",
      "url": "资源链接",
      "note": "备注",
      "created_at": "创建时间"
    }
  ]
  ```

### 技术锦囊相关接口

#### 创建技术锦囊

- **接口**：`POST /api/tech-tips`
- **请求体**：
  ```json
  {
    "name": "锦囊名称",
    "content": "锦囊内容",
    "note": "备注（可选）"
  }
  ```

#### 获取技术锦囊列表

- **接口**：`GET /api/tech-tips`
- **响应**：
  ```json
  [
    {
      "id": 1,
      "name": "锦囊名称",
      "content": "锦囊内容",
      "note": "备注",
      "created_at": "创建时间"
    }
  ]
  ```

### 归档相关接口

#### 创建归档

- **接口**：`POST /api/archives`
- **请求体**：
  ```json
  {
    "name": "归档名称",
    "tweet_ids": [1, 2, 3],
    "resource_ids": [1, 2],
    "tech_tip_ids": [1, 2]
  }
  ```

#### 获取归档列表

- **接口**：`GET /api/archives`
- **响应**：
  ```json
  [
    {
      "id": 1,
      "name": "归档名称",
      "created_at": "创建时间",
      "tweets": [{ "id": 1, "title": "推文标题" }],
      "resources": [{ "id": 1, "name": "资源名称" }],
      "tech_tips": [{ "id": 1, "name": "锦囊名称" }]
    }
  ]
  ```

## 默认管理员账号

- 用户名：admin
- 密码：admin

## 注意事项

1. 所有接口都需要在登录后使用
2. 接口返回的错误信息会包含在响应体中
3. 数据库文件默认存储在项目根目录下的 `instance` 文件夹中
4. 建议定期备份数据库文件
