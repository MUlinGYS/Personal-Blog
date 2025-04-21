import { createApp } from 'vue'
import router from './router'  // 引入路由实例
import App from './App.vue'
import ElementPlus from 'element-plus'
import store from './store';
import 'element-plus/dist/index.css'
import * as ElementPlusIconsVue from '@element-plus/icons-vue'
// import './api/mock' //mockjs模拟后端数据//暂时弃用

// 导入highlight.js和样式
import hljs from 'highlight.js';
import 'highlight.js/styles/atom-one-dark.css'; // 导入代码高亮样式

const app = createApp(App)
// 注册 Element Plus 图标
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
  app.component(key, component)
}

// 全局配置highlight.js
app.directive('highlight', function (el) {
  const blocks = el.querySelectorAll('pre code');
  blocks.forEach((block) => {
    hljs.highlightElement(block);
  });
});

app
  .use(store)     // 使用 Vuex 状态管理
  .use(router)   // 使用路由实例
  .use(ElementPlus)  // 使用 Element Plus
  .mount('#app')   // 应用挂载点