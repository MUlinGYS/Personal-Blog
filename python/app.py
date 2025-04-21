from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from models import db, User, Tweet, Resource, TechTip, Archive, ViewCount
from config import Config
import datetime
import secrets  # 添加token

app = Flask(__name__, static_folder='../python/dist', static_url_path='')
app.config.from_object(Config)
CORS(app)
db.init_app(app)

# 添加根路由处理
@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')
    
# 处理其他前端路由
@app.route('/<path:path>')
def serve_vue_app(path):
    try:
        return send_from_directory(app.static_folder, path)
    except:
        return send_from_directory(app.static_folder, 'index.html')

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

# 统计接口
@app.route('/api/statistics', methods=['GET'])
def get_statistics():
    try:
        # 获取文章数量
        tweet_count = Tweet.query.count()
        resource_count = Resource.query.count()
        tech_tip_count = TechTip.query.count()
        total_articles = tweet_count + resource_count + tech_tip_count
        
        # 计算总访问量（网站访问）
        total_views = ViewCount.query.filter_by(content_type='website').with_entities(db.func.sum(ViewCount.view_count)).scalar() or 0
        
        # 计算总阅读量（文章阅读）
        total_reads = ViewCount.query.filter(ViewCount.content_type != 'website').with_entities(db.func.sum(ViewCount.view_count)).scalar() or 0
        
        # 计算本月访问量
        start_of_month = datetime.datetime.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        monthly_views = ViewCount.query.filter(
            ViewCount.content_type == 'website',
            ViewCount.created_at >= start_of_month
        ).with_entities(db.func.sum(ViewCount.view_count)).scalar() or 0
        
        # 计算总字数
        total_words = 0
        # 统计推文字数
        tweets = Tweet.query.all()
        for tweet in tweets:
            total_words += len(tweet.content)
        # 统计技术锦囊字数
        tech_tips = TechTip.query.all()
        for tip in tech_tips:
            total_words += len(tip.content)
        
        return jsonify({
            'tweet_count': tweet_count,      # 推文数量
            'resource_count': resource_count, # 资源数量
            'tech_tip_count': tech_tip_count, # 技术锦囊数量
            'monthly_views': monthly_views,   # 本月访问量
            'total_views': total_views,       # 总访问量
            'total_reads': total_reads,       # 总阅读量
            'total_articles': total_articles, # 总文章数
            'total_words': total_words        # 总字数
        })
    except Exception as e:
        print(f"Error in get_statistics: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/view-count/<content_type>/<int:content_id>', methods=['POST'])
def increment_view_count(content_type, content_id):
    try:
        # 查找或创建阅读量记录
        view_count = ViewCount.query.filter_by(
            content_type=content_type,
            content_id=content_id
        ).first()
        
        if not view_count:
            view_count = ViewCount(
                content_type=content_type,
                content_id=content_id,
                view_count=0
            )
            db.session.add(view_count)
        
        # 增加阅读量
        view_count.view_count += 1
        db.session.commit()
        
        return jsonify({
            'success': True,
            'view_count': view_count.view_count
        })
    except Exception as e:
        print(f"Error in increment_view_count: {str(e)}")
        return jsonify({'error': str(e)}), 500

# 获取提交记录接口
@app.route('/api/submissions', methods=['GET'])
def get_submissions():
    try:
        # 获取最近的提交记录，包括推文、资源和技术锦囊
        # 按创建时间倒序排序，限制返回数
        limit = int(request.args.get('limit', 6))  # 默认限制为6条
        
        # 获取最近的推文
        recent_tweets = Tweet.query.order_by(Tweet.created_at.desc()).limit(limit).all()
        tweet_submissions = [{
            'id': t.id,
            'type': 'tweet',
            'title': t.title,
            'content': t.content[:100] + '...' if len(t.content) > 100 else t.content,
            'note': t.note,
            'created_at': t.created_at.isoformat() if t.created_at else None
        } for t in recent_tweets]
        
        # 获取最近的资源
        recent_resources = Resource.query.order_by(Resource.created_at.desc()).limit(limit).all()
        resource_submissions = [{
            'id': r.id,
            'type': 'resource',
            'name': r.name,
            'url': r.url[:100] + '...' if len(r.url) > 100 else r.url,
            'note': r.note,
            'created_at': r.created_at.isoformat() if r.created_at else None
        } for r in recent_resources]
        
        # 获取最近的技术锦囊
        recent_tech_tips = TechTip.query.order_by(TechTip.created_at.desc()).limit(limit).all()
        tech_tip_submissions = [{
            'id': t.id,
            'type': 'tech_tip',
            'name': t.name,
            'content': t.content[:100] + '...' if len(t.content) > 100 else t.content,
            'note': t.note,
            'created_at': t.created_at.isoformat() if t.created_at else None
        } for t in recent_tech_tips]
        
        # 合并所有提交记录并按时间排序
        all_submissions = tweet_submissions + resource_submissions + tech_tip_submissions
        all_submissions.sort(key=lambda x: x['created_at'] if x['created_at'] else '', reverse=True)
        
        return jsonify(all_submissions)
    except Exception as e:
        print(f"Error in get_submissions: {str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)