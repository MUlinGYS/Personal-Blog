import { createRouter, createWebHistory } from 'vue-router'
import index from '../views/index/index.vue'

const routes = [
// 定义你的路由路径，每一个对象一个路由，例如：
{
path: '/',
component: index
},
]

const router = createRouter({
history: createWebHistory(),
routes,
})

export default router