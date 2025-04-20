from app import app, db
from models import User
from config import Config

def init_db():
    with app.app_context():
        # 删除所有表
        db.drop_all()
        # 创建所有表
        db.create_all()
        
        # 检查是否存在默认管理员账号
        if not User.query.filter_by(username=Config.DEFAULT_ADMIN_USERNAME).first():
            # 创建新的管理员用户对象
            admin = User(username=Config.DEFAULT_ADMIN_USERNAME)
            # 设置管理员密码
            admin.set_password(Config.DEFAULT_ADMIN_PASSWORD)
            # 将管理员用户添加到数据库会话
            db.session.add(admin)
            # 提交更改到数据库
            db.session.commit()
            print("数据库初始化成功！已创建默认管理员账号。")
        else:
            print("数据库已存在，无需初始化。")

if __name__ == '__main__':
    init_db() 