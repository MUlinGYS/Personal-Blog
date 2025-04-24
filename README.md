# Personal-Blog

这是一个使用 Vue 3、Vite、Less 和 Element Plus 构建的个人博客项目。

## 技术栈

- **前端框架:** [Vue 3](https://vuejs.org/)
- **构建工具:** [Vite](https://vitejs.dev/)
- **CSS 预处理器:** [Less](https://lesscss.org/)
- **UI 库:** [Element Plus](https://element-plus.org/)
- **包管理器:** [Yarn](https://yarnpkg.com/) / [npm](https://www.npmjs.com/)

## 项目设置

### 安装依赖

```bash
# 使用 yarn
yarn install

# 或者使用 npm
npm install
```

### 本地开发

启动开发服务器：

```bash
# 使用 yarn
yarn dev

# 或者使用 npm
npm run dev
```

### 生产构建

编译和压缩用于生产环境：

```bash
# 使用 yarn
yarn build

# 或者使用 npm
npm run build
```

## 项目结构

```
├── public/            # 静态资源目录 (不会被 Vite 处理)
├── src/
│   ├── api/           # API 请求模块
│   ├── assets/        # 静态资源 (会被 Vite 处理)
│   ├── components/    # 公共组件
│   ├── pages/         # 页面级组件 (也可能在 views/)
│   ├── router/        # 路由配置
│   ├── store/         # 状态管理 (Pinia/Vuex)
│   ├── utils/         # 工具函数
│   ├── views/         # 视图组件 (页面)
│   ├── App.vue        # 根组件
│   ├── main.js        # 应用入口文件
│   └── style.css      # 全局样式 (或 less/scss 文件)
├── .gitignore         # Git 忽略配置
├── index.html         # HTML 入口文件
├── package.json       # 项目依赖和脚本配置
├── vite.config.js     # Vite 配置文件
└── README.md          # 项目说明文档
```
