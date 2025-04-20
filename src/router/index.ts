import { createRouter, createWebHistory, RouteRecordRaw, RouteLocationNormalized, NavigationGuardNext } from 'vue-router'
import login from '../views/login/login.vue'
import Cookies from 'js-cookie'

const routes: Array<RouteRecordRaw> = [
    {
        path: '/',
        name:'login',
        component: login
    },
    {
        name: 'index',
        path: '/index',
        meta: { requiresAuth: true }, 
        component: () => import('../views/index/index.vue'),
        children: [
            {
                name: 'main',
                path: '',
                component: () => import('../pages/main/main.vue')
            }
        ],
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

router.beforeEach((to: RouteLocationNormalized, _from: RouteLocationNormalized, next: NavigationGuardNext) => {
    const token = Cookies.get('token');
        if (to.matched.some(record => record.meta.requiresAuth)) {
            if (token) {
                if (to.path === '/') {
                    next({ path: '/index' });
                } else {
                    next();
                }
            } else {
                next({
                path: '/',
            });
            }
        } else {
    if (to.path === '/' && token) {
        next({ path: '/index' });
    } else {
        next();
    }
    }
});

export default router