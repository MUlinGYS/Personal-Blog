from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, User, Tweet, Resource, TechTip, Archive
from config import Config
import datetime
import secrets  # 添加token

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)
db.init_app(app)

# 初始化数据库
with app.app_context():
    # 创建所有数据库表
    db.create_all()
    # # 检查是否存在默认管理员账号,如果不存在则创建一个
    # if not User.query.filter_by(username=Config.DEFAULT_ADMIN_USERNAME).first():
    #     # 创建新的管理员用户对象
    #     admin = User(username=Config.DEFAULT_ADMIN_USERNAME)
    #     # 设置管理员密码
    #     admin.set_password(Config.DEFAULT_ADMIN_PASSWORD)
    #     # 将管理员用户添加到数据库会话
    #     db.session.add(admin)
    #     # 提交更改到数据库
    #     db.session.commit()

# 登录接口
@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        # 生成随机token
        token = secrets.token_hex(16)  # 生成32位的随机token
        return jsonify({
            'success': True, 
            'message': '登录成功',
            'token': token  # 返回token
        })
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
    try:
        search = request.args.get('search', '')
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
        
        # 构建基础查询
        query = Tweet.query
        
        # 如果有搜索关键词，先进行搜索
        if search:
            # 使用SQLAlchemy的like进行模糊搜索
            query = query.filter(Tweet.title.like(f'%{search}%'))
            
        # 按创建时间倒序排序
        query = query.order_by(Tweet.created_at.desc())
        
        # 分页查询
        pagination = query.paginate(page=page, per_page=per_page, error_out=False)
        tweets = pagination.items
        
        return jsonify({
            'items': [{
                'id': t.id,
                'title': t.title,
                'content': t.content,
                'note': t.note,
                'created_at': t.created_at.isoformat() if t.created_at else None,
                'updated_at': t.updated_at.isoformat() if t.updated_at else None
            } for t in tweets],
            'total': pagination.total,
            'pages': pagination.pages,
            'current_page': page
        })
    except Exception as e:
        print(f"Error in get_tweets: {str(e)}")
        return jsonify({'error': str(e)}), 500

# 修改推文接口
@app.route('/api/tweets/<int:tweet_id>', methods=['PUT'])
def update_tweet(tweet_id):
    tweet = Tweet.query.get_or_404(tweet_id)
    data = request.get_json()
    
    if 'title' in data:
        tweet.title = data['title']
    if 'content' in data:
        tweet.content = data['content']
    if 'note' in data:
        tweet.note = data['note']
    
    db.session.commit()
    return jsonify({'success': True, 'message': '推文修改成功'})

# 删除推文接口
@app.route('/api/tweets/<int:tweet_id>', methods=['DELETE'])
def delete_tweet(tweet_id):
    tweet = Tweet.query.get_or_404(tweet_id)
    db.session.delete(tweet)
    db.session.commit()
    return jsonify({'success': True, 'message': '推文删除成功'})

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
    try:
        search = request.args.get('search', '')
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
        
        # 构建基础查询
        query = Resource.query
        
        # 如果有搜索关键词，先进行搜索
        if search:
            # 使用SQLAlchemy的like进行模糊搜索
            query = query.filter(Resource.name.like(f'%{search}%'))
            
        # 按创建时间倒序排序
        query = query.order_by(Resource.created_at.desc())
        
        # 分页查询
        pagination = query.paginate(page=page, per_page=per_page, error_out=False)
        resources = pagination.items
        
        return jsonify({
            'items': [{
                'id': r.id,
                'name': r.name,
                'url': r.url,
                'note': r.note,
                'created_at': r.created_at.isoformat() if r.created_at else None,
                'updated_at': r.updated_at.isoformat() if r.updated_at else None
            } for r in resources],
            'total': pagination.total,
            'pages': pagination.pages,
            'current_page': page
        })
    except Exception as e:
        print(f"Error in get_resources: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/resources/<int:resource_id>', methods=['GET'])
def get_resource(resource_id):
    try:
        resource = Resource.query.get_or_404(resource_id)
        return jsonify({
            'id': resource.id,
            'name': resource.name,
            'url': resource.url,
            'note': resource.note,
            'created_at': resource.created_at.isoformat() if resource.created_at else None,
            'updated_at': resource.updated_at.isoformat() if resource.updated_at else None
        })
    except Exception as e:
        print(f"Error in get_resource: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/resources/<int:resource_id>', methods=['PUT'])
def update_resource(resource_id):
    try:
        resource = Resource.query.get_or_404(resource_id)
        data = request.get_json()
        
        if 'name' in data:
            resource.name = data['name']
        if 'url' in data:
            resource.url = data['url']
        if 'note' in data:
            resource.note = data['note']
        
        db.session.commit()
        return jsonify({
            'success': True,
            'message': '资源更新成功',
            'resource': {
                'id': resource.id,
                'name': resource.name,
                'url': resource.url,
                'note': resource.note,
                'created_at': resource.created_at.isoformat() if resource.created_at else None,
                'updated_at': resource.updated_at.isoformat() if resource.updated_at else None
            }
        })
    except Exception as e:
        print(f"Error in update_resource: {str(e)}")
        return jsonify({'error': str(e)}), 500

# 删除资源接口
@app.route('/api/resources/<int:resource_id>', methods=['DELETE'])
def delete_resource(resource_id):
    try:
        resource = Resource.query.get_or_404(resource_id)
        db.session.delete(resource)
        db.session.commit()
        return jsonify({'success': True, 'message': '资源删除成功'})
    except Exception as e:
        print(f"Error in delete_resource: {str(e)}")
        return jsonify({'error': str(e)}), 500

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
    try:
        search = request.args.get('search', '')
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
        
        # 构建基础查询
        query = TechTip.query
        
        # 如果有搜索关键词，先进行搜索
        if search:
            # 使用SQLAlchemy的like进行模糊搜索
            query = query.filter(TechTip.name.like(f'%{search}%'))
            
        # 按创建时间倒序排序
        query = query.order_by(TechTip.created_at.desc())
        
        # 分页查询
        pagination = query.paginate(page=page, per_page=per_page, error_out=False)
        tech_tips = pagination.items
        
        return jsonify({
            'items': [{
                'id': t.id,
                'name': t.name,
                'content': t.content,
                'note': t.note,
                'created_at': t.created_at.isoformat() if t.created_at else None,
                'updated_at': t.updated_at.isoformat() if t.updated_at else None
            } for t in tech_tips],
            'total': pagination.total,
            'pages': pagination.pages,
            'current_page': page
        })
    except Exception as e:
        print(f"Error in get_tech_tips: {str(e)}")
        return jsonify({'error': str(e)}), 500

# 修改技术锦囊接口
@app.route('/api/tech-tips/<int:tip_id>', methods=['PUT'])
def update_tech_tip(tip_id):
    try:
        tech_tip = TechTip.query.get_or_404(tip_id)
        data = request.get_json()
        
        if 'name' in data:
            tech_tip.name = data['name']
        if 'content' in data:
            tech_tip.content = data['content']
        if 'note' in data:
            tech_tip.note = data['note']
        
        # 更新updated_at字段
        tech_tip.updated_at = datetime.datetime.utcnow()
        
        db.session.commit()
        return jsonify({
            'success': True,
            'message': '技术锦囊更新成功',
            'tech_tip': {
                'id': tech_tip.id,
                'name': tech_tip.name,
                'content': tech_tip.content,
                'note': tech_tip.note,
                'created_at': tech_tip.created_at.isoformat() if tech_tip.created_at else None,
                'updated_at': tech_tip.updated_at.isoformat() if tech_tip.updated_at else None
            }
        })
    except Exception as e:
        print(f"Error in update_tech_tip: {str(e)}")
        return jsonify({'error': str(e)}), 500

# 删除技术锦囊接口
@app.route('/api/tech-tips/<int:tip_id>', methods=['DELETE'])
def delete_tech_tip(tip_id):
    try:
        tech_tip = TechTip.query.get_or_404(tip_id)
        db.session.delete(tech_tip)
        db.session.commit()
        return jsonify({'success': True, 'message': '技术锦囊删除成功'})
    except Exception as e:
        print(f"Error in delete_tech_tip: {str(e)}")
        return jsonify({'error': str(e)}), 500

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