import { createApp } from 'vue'
import router from './router'  // 引入路由实例
import App from './App.vue'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'

createApp(App)
  .use(router)   // 使用路由实例
  .use(ElementPlus)  // 使用 Element Plus
  .mount('#app')   // 应用挂载点