import { createApp } from 'vue'
import router from './router'  // 引入路由实例
import App from './App.vue'
import ElementPlus from 'element-plus'
import store from './store';
import 'element-plus/dist/index.css'
import * as ElementPlusIconsVue from '@element-plus/icons-vue'
// import './api/mock' //mockjs模拟后端数据//暂时弃用


const app = createApp(App)
// 注册 Element Plus 图标
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
  app.component(key, component)
}

app
  .use(store)     // 使用 Vuex 状态管理
  .use(router)   // 使用路由实例
  .use(ElementPlus)  // 使用 Element Plus
  .mount('#app')   // 应用挂载点