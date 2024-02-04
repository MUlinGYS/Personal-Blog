    import { createApp } from 'vue'
    import router from './router'  // 引入路由实例
    import App from './App.vue'

    createApp(App)
      .use(router)   // 使用路由实例
      .mount('#app')