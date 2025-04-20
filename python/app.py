from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, User, Tweet, Resource, TechTip, Archive
from config import Config
import datetime

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)
db.init_app(app)

# 初始化数据库
with app.app_context():
    db.create_all()
    # 创建默认管理员账号
    if not User.query.filter_by(username=Config.DEFAULT_ADMIN_USERNAME).first():
        admin = User(username=Config.DEFAULT_ADMIN_USERNAME)
        admin.set_password(Config.DEFAULT_ADMIN_PASSWORD)
        db.session.add(admin)
        db.session.commit()

# 登录接口
@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        return jsonify({'success': True, 'message': '登录成功'})
    return jsonify({'success': False, 'message': '用户名或密码错误'}), 401

# 修改账号接口
@app.route('/api/user', methods=['PUT'])
def update_user():
    data = request.get_json()
    old_username = data.get('old_username')
    old_password = data.get('old_password')
    new_username = data.get('new_username')
    new_password = data.get('new_password')
    
    user = User.query.filter_by(username=old_username).first()
    if user and user.check_password(old_password):
        user.username = new_username
        user.set_password(new_password)
        db.session.commit()
        return jsonify({'success': True, 'message': '账号修改成功'})
    return jsonify({'success': False, 'message': '原账号或密码错误'}), 401

# 新建账号接口
@app.route('/api/user', methods=['POST'])
def create_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if User.query.filter_by(username=username).first():
        return jsonify({'success': False, 'message': '用户名已存在'}), 400
    
    user = User(username=username)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return jsonify({'success': True, 'message': '账号创建成功'})

# 推文接口
@app.route('/api/tweets', methods=['POST'])
def create_tweet():
    data = request.get_json()
    tweet = Tweet(
        title=data['title'],
        content=data['content'],
        note=data.get('note')
    )
    db.session.add(tweet)
    db.session.commit()
    return jsonify({'success': True, 'message': '推文创建成功'})

@app.route('/api/tweets', methods=['GET'])
def get_tweets():
    tweets = Tweet.query.all()
    return jsonify([{
        'id': t.id,
        'title': t.title,
        'content': t.content,
        'note': t.note,
        'created_at': t.created_at
    } for t in tweets])

# 资源链接接口
@app.route('/api/resources', methods=['POST'])
def create_resource():
    data = request.get_json()
    resource = Resource(
        name=data['name'],
        url=data['url'],
        note=data.get('note')
    )
    db.session.add(resource)
    db.session.commit()
    return jsonify({'success': True, 'message': '资源链接创建成功'})

@app.route('/api/resources', methods=['GET'])
def get_resources():
    resources = Resource.query.all()
    return jsonify([{
        'id': r.id,
        'name': r.name,
        'url': r.url,
        'note': r.note,
        'created_at': r.created_at
    } for r in resources])

# 技术锦囊接口
@app.route('/api/tech-tips', methods=['POST'])
def create_tech_tip():
    data = request.get_json()
    tech_tip = TechTip(
        name=data['name'],
        content=data['content'],
        note=data.get('note')
    )
    db.session.add(tech_tip)
    db.session.commit()
    return jsonify({'success': True, 'message': '技术锦囊创建成功'})

@app.route('/api/tech-tips', methods=['GET'])
def get_tech_tips():
    tech_tips = TechTip.query.all()
    return jsonify([{
        'id': t.id,
        'name': t.name,
        'content': t.content,
        'note': t.note,
        'created_at': t.created_at
    } for t in tech_tips])

# 归档接口
@app.route('/api/archives', methods=['POST'])
def create_archive():
    data = request.get_json()
    archive = Archive(name=data['name'])
    db.session.add(archive)
    db.session.commit()
    
    # 添加推文到归档
    if 'tweet_ids' in data:
        tweets = Tweet.query.filter(Tweet.id.in_(data['tweet_ids'])).all()
        for tweet in tweets:
            tweet.archive_id = archive.id
    
    # 添加资源链接到归档
    if 'resource_ids' in data:
        resources = Resource.query.filter(Resource.id.in_(data['resource_ids'])).all()
        for resource in resources:
            resource.archive_id = archive.id
    
    # 添加技术锦囊到归档
    if 'tech_tip_ids' in data:
        tech_tips = TechTip.query.filter(TechTip.id.in_(data['tech_tip_ids'])).all()
        for tech_tip in tech_tips:
            tech_tip.archive_id = archive.id
    
    db.session.commit()
    return jsonify({'success': True, 'message': '归档创建成功'})

@app.route('/api/archives', methods=['GET'])
def get_archives():
    archives = Archive.query.all()
    return jsonify([{
        'id': a.id,
        'name': a.name,
        'created_at': a.created_at,
        'tweets': [{'id': t.id, 'title': t.title} for t in a.tweets],
        'resources': [{'id': r.id, 'name': r.name} for r in a.resources],
        'tech_tips': [{'id': t.id, 'name': t.name} for t in a.tech_tips]
    } for a in archives])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)