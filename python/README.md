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
- 代码锦囊管理
  - 创建代码锦囊
  - 获取代码锦囊列表
- 归档管理
  - 统计各板块文章梳理
  - 统计阅读量
  - 统计最近新增的 6 篇文章
- 统计相关数据
  - 统计推文数量
  - 资源数量
  - 代码锦囊数量
  - 本月访问量
  - 总访问量总
  - 阅读量
  - 总文章数
  - 总字数

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
- **描述**：用户登录接口，验证用户名和密码
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
- **错误响应**：
  ```json
  {
    "success": false,
    "message": "用户名或密码错误"
  }
  ```
- **状态码**：
  - 200：登录成功
  - 401：用户名或密码错误

#### 修改账号

- **接口**：`PUT /api/user`
- **描述**：修改用户账号信息，包括用户名和密码
- **请求体**：
  ```json
  {
    "old_username": "原用户名",
    "old_password": "原密码",
    "new_username": "新用户名",
    "new_password": "新密码"
  }
  ```
- **响应**：
  ```json
  {
    "success": true,
    "message": "账号修改成功"
  }
  ```
- **错误响应**：
  ```json
  {
    "success": false,
    "message": "原账号或密码错误"
  }
  ```
- **状态码**：
  - 200：修改成功
  - 401：原账号或密码错误

#### 创建账号

- **接口**：`POST /api/user`
- **描述**：创建新用户账号
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
    "message": "账号创建成功"
  }
  ```
- **错误响应**：
  ```json
  {
    "success": false,
    "message": "用户名已存在"
  }
  ```
- **状态码**：
  - 200：创建成功
  - 400：用户名已存在

### 推文相关接口

#### 创建推文

- **接口**：`POST /api/tweets`
- **描述**：创建新的推文
- **请求体**：
  ```json
  {
    "title": "推文标题",
    "content": "推文内容",
    "note": "备注（可选）"
  }
  ```
- **响应**：
  ```json
  {
    "success": true,
    "message": "推文创建成功"
  }
  ```
- **状态码**：
  - 200：创建成功

#### 获取推文列表

- **接口**：`GET /api/tweets`
- **描述**：获取推文列表，支持分页和搜索
- **查询参数**：
  - `search`：搜索关键词（可选）
  - `page`：页码，默认为 1
  - `per_page`：每页数量，默认为 10
- **响应**：
  ```json
  {
    "items": [
      {
        "id": 1,
        "title": "推文标题",
        "content": "推文内容",
        "note": "备注",
        "created_at": "2023-01-01T12:00:00",
        "updated_at": "2023-01-01T12:00:00"
      }
    ],
    "total": 100,
    "pages": 10,
    "current_page": 1
  }
  ```
- **状态码**：
  - 200：获取成功

#### 修改推文

- **接口**：`PUT /api/tweets/<tweet_id>`
- **描述**：修改指定 ID 的推文
- **路径参数**：
  - `tweet_id`：推文 ID
- **请求体**：
  ```json
  {
    "title": "新标题",
    "content": "新内容",
    "note": "新备注"
  }
  ```
- **响应**：
  ```json
  {
    "success": true,
    "message": "推文修改成功"
  }
  ```
- **错误响应**：
  ```json
  {
    "error": "推文不存在"
  }
  ```
- **状态码**：
  - 200：修改成功
  - 404：推文不存在

#### 删除推文

- **接口**：`DELETE /api/tweets/<tweet_id>`
- **描述**：删除指定 ID 的推文
- **路径参数**：
  - `tweet_id`：推文 ID
- **响应**：
  ```json
  {
    "success": true,
    "message": "推文删除成功"
  }
  ```
- **错误响应**：
  ```json
  {
    "error": "推文不存在"
  }
  ```
- **状态码**：
  - 200：删除成功
  - 404：推文不存在

### 资源链接相关接口

#### 创建资源链接

- **接口**：`POST /api/resources`
- **描述**：创建新的资源链接
- **请求体**：
  ```json
  {
    "name": "资源名称",
    "url": "资源链接",
    "note": "备注（可选）"
  }
  ```
- **响应**：
  ```json
  {
    "success": true,
    "message": "资源链接创建成功"
  }
  ```
- **状态码**：
  - 200：创建成功

#### 获取资源列表

- **接口**：`GET /api/resources`
- **描述**：获取资源链接列表，支持分页和搜索
- **查询参数**：
  - `search`：搜索关键词（可选）
  - `page`：页码，默认为 1
  - `per_page`：每页数量，默认为 10
- **响应**：
  ```json
  {
    "items": [
      {
        "id": 1,
        "name": "资源名称",
        "url": "资源链接",
        "note": "备注",
        "created_at": "2023-01-01T12:00:00",
        "updated_at": "2023-01-01T12:00:00"
      }
    ],
    "total": 100,
    "pages": 10,
    "current_page": 1
  }
  ```
- **状态码**：
  - 200：获取成功

#### 修改资源链接

- **接口**：`PUT /api/resources/<resource_id>`
- **描述**：修改指定 ID 的资源链接
- **路径参数**：
  - `resource_id`：资源 ID
- **请求体**：
  ```json
  {
    "name": "新名称",
    "url": "新链接",
    "note": "新备注"
  }
  ```
- **响应**：
  ```json
  {
    "success": true,
    "message": "资源更新成功",
    "resource": {
      "id": 1,
      "name": "新名称",
      "url": "新链接",
      "note": "新备注",
      "created_at": "2023-01-01T12:00:00",
      "updated_at": "2023-01-01T12:00:00"
    }
  }
  ```
- **错误响应**：
  ```json
  {
    "error": "资源不存在"
  }
  ```
- **状态码**：
  - 200：修改成功
  - 404：资源不存在

#### 删除资源链接

- **接口**：`DELETE /api/resources/<resource_id>`
- **描述**：删除指定 ID 的资源链接
- **路径参数**：
  - `resource_id`：资源 ID
- **响应**：
  ```json
  {
    "success": true,
    "message": "资源删除成功"
  }
  ```
- **错误响应**：
  ```json
  {
    "error": "资源不存在"
  }
  ```
- **状态码**：
  - 200：删除成功
  - 404：资源不存在

### 代码锦囊相关接口

#### 创建代码锦囊

- **接口**：`POST /api/tech-tips`
- **描述**：创建新的代码锦囊
- **请求体**：
  ```json
  {
    "name": "锦囊名称",
    "content": "锦囊内容",
    "note": "备注（可选）"
  }
  ```
- **响应**：
  ```json
  {
    "success": true,
    "message": "代码锦囊创建成功"
  }
  ```
- **状态码**：
  - 200：创建成功

#### 获取代码锦囊列表

- **接口**：`GET /api/tech-tips`
- **描述**：获取代码锦囊列表，支持分页和搜索
- **查询参数**：
  - `search`：搜索关键词（可选）
  - `page`：页码，默认为 1
  - `per_page`：每页数量，默认为 10
- **响应**：
  ```json
  {
    "items": [
      {
        "id": 1,
        "name": "锦囊名称",
        "content": "锦囊内容",
        "note": "备注",
        "created_at": "2023-01-01T12:00:00",
        "updated_at": "2023-01-01T12:00:00"
      }
    ],
    "total": 100,
    "pages": 10,
    "current_page": 1
  }
  ```
- **状态码**：
  - 200：获取成功

#### 修改代码锦囊

- **接口**：`PUT /api/tech-tips/<tip_id>`
- **描述**：修改指定 ID 的代码锦囊
- **路径参数**：
  - `tip_id`：代码锦囊 ID
- **请求体**：
  ```json
  {
    "name": "新名称",
    "content": "新内容",
    "note": "新备注"
  }
  ```
- **响应**：
  ```json
  {
    "success": true,
    "message": "代码锦囊更新成功",
    "tech_tip": {
      "id": 1,
      "name": "新名称",
      "content": "新内容",
      "note": "新备注",
      "created_at": "2023-01-01T12:00:00",
      "updated_at": "2023-01-01T12:00:00"
    }
  }
  ```
- **错误响应**：
  ```json
  {
    "error": "代码锦囊不存在"
  }
  ```
- **状态码**：
  - 200：修改成功
  - 404：代码锦囊不存在

#### 删除代码锦囊

- **接口**：`DELETE /api/tech-tips/<tip_id>`
- **描述**：删除指定 ID 的代码锦囊
- **路径参数**：
  - `tip_id`：代码锦囊 ID
- **响应**：
  ```json
  {
    "success": true,
    "message": "代码锦囊删除成功"
  }
  ```
- **错误响应**：
  ```json
  {
    "error": "代码锦囊不存在"
  }
  ```
- **状态码**：
  - 200：删除成功
  - 404：代码锦囊不存在

### 统计相关接口

#### 获取统计数据

- **接口**：`GET /api/statistics`
- **描述**：获取博客统计数据，包括文章数量、访问量等
- **响应**：
  ```json
  {
    "tweet_count": 10, // 推文数量
    "resource_count": 5, // 资源数量
    "tech_tip_count": 8, // 代码锦囊数量
    "monthly_views": 100, // 本月访问量
    "total_views": 1000, // 总访问量
    "total_reads": 500, // 总阅读量
    "total_articles": 23, // 总文章数
    "total_words": 5000 // 总字数
  }
  ```
- **状态码**：
  - 200：获取成功

#### 增加访问量

- **接口**：`POST /api/view-count/<content_type>/<content_id>`
- **描述**：增加指定内容的访问量
- **路径参数**：
  - `content_type`：内容类型（tweet/resource/tech_tip）
  - `content_id`：内容 ID
- **响应**：
  ```json
  {
    "success": true,
    "view_count": 10
  }
  ```
- **状态码**：
  - 200：操作成功

### 提交记录相关接口

#### 获取提交记录

- **接口**：`GET /api/submissions`
- **描述**：获取最近的提交记录，包括推文、资源和代码锦囊
- **查询参数**：
  - `limit`：限制返回数量，默认为 6
- **响应**：
  ```json
  [
    {
      "id": 1,
      "type": "tweet",
      "title": "推文标题",
      "content": "推文内容...",
      "note": "备注",
      "created_at": "2023-01-01T12:00:00"
    },
    {
      "id": 2,
      "type": "resource",
      "name": "资源名称",
      "url": "资源链接...",
      "note": "备注",
      "created_at": "2023-01-01T11:00:00"
    },
    {
      "id": 3,
      "type": "tech_tip",
      "name": "锦囊名称",
      "content": "锦囊内容...",
      "note": "备注",
      "created_at": "2023-01-01T10:00:00"
    }
  ]
  ```
- **状态码**：
  - 200：获取成功

## 默认管理员账号

- 用户名：admin
- 密码：admin

## 注意事项

1. 所有接口都需要在登录后使用
2. 接口返回的错误信息会包含在响应体中
3. 数据库文件默认存储在项目根目录下的 `instance` 文件夹中
4. 建议定期备份数据库文件
