import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue';
import { resolve, dirname } from 'path';    // 导入 resolve, dirname
import { fileURLToPath } from 'url';        // 导入 fileURLToPath

// 将文件URL转换为路径
const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

// https://vitejs.dev/config/
export default defineConfig({
    base: './',  // 添加这一行
    plugins: [vue()],
    resolve: {
        alias: {
        '@': resolve(__dirname, 'src')  // 将 '@' 的别名设置为 'src/' 
        }
    },
    css: {
        devSourcemap: false,
        preprocessorOptions: {
            css: {
                sourceMap: false
            }
        }
    }
}) 