import { createRouter, createWebHistory } from 'vue-router'
import login from '../views/login/login.vue'

const routes = [
    // 定义你的路由路径，每一个对象一个路由，例如：
    {
        path: '/',
        component: login
    },
    {
        name: 'index',
        path: '/index',
        component: () => import('../views/index/index.vue'),
        children: [
            {
                name: 'main',
                path: '',
                component: () => import('../views/main/main.vue')
            }
        ],
    },
    {
        name: 'publishpage',
        path: '/publishpage',
        component: () => import('../views/Publish page/PublishPage.vue'),
    },
    
]

const router = createRouter({
history: createWebHistory(),
routes,
})

export default router