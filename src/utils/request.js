import axios from 'axios'

// 创建axios实例
const service = axios.create({
    baseURL: 'http://localhost:5000/api',
    timeout: 5000
})

// 请求拦截器
service.interceptors.request.use(
    config => {
        return config
    },
    error => {
        console.log(error)
        return Promise.reject(error)
    }
)

// 响应拦截器
service.interceptors.response.use(
    response => {
        return response
    },
    error => {
        console.log('err' + error)
        return Promise.reject(error)
    }
)

export default service 