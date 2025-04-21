FROM python:3.8

# 设置工作目录
WORKDIR /app

# FROM registry.cn-hangzhou.aliyuncs.com/library/python:3.8-slim

# 配置pip使用清华大学镜像源
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple


# 复制项目文件
COPY . .

# 安装项目依赖
RUN pip install -r requirements.txt

# 暴露端口
EXPOSE 8989

# 设置环境变量
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# 启动应用
CMD ["flask", "run", "--host=0.0.0.0", "--port=8989"] 