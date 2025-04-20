import axios from 'axios'

// 创建 axios 实例
const request = axios.create({
    // 设置基础URL
    baseURL: 'http://localhost:5000/api',
    // 设置超时时间
    timeout: 5000
})

// 请求拦截器
request.interceptors.request.use(
    config => {
        // 在这里可以添加token等认证信息
        return config
    },
    error => {
        return Promise.reject(error)
    }
)

// 响应拦截器
request.interceptors.response.use(
    response => {
        return response
    },
    error => {
        return Promise.reject(error)
    }
)

export default request 