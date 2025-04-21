from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
from sqlalchemy import func
from sqlalchemy.sql import expression

db = SQLAlchemy()

# 创建UTC+8时区的时间函数 (原来是+10，减少2小时变成+8)
def sqtime_8():
    # 使用datetime和timedelta而不是依赖数据库函数
    return datetime.datetime.utcnow() + datetime.timedelta(hours=8)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    note = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=sqtime_8)
    updated_at = db.Column(db.DateTime, default=sqtime_8, onupdate=sqtime_8)
    archive_id = db.Column(db.Integer, db.ForeignKey('archive.id'))

class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    url = db.Column(db.String(200), nullable=False)
    note = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=sqtime_8)
    updated_at = db.Column(db.DateTime, default=sqtime_8, onupdate=sqtime_8)
    archive_id = db.Column(db.Integer, db.ForeignKey('archive.id'))

class TechTip(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    note = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=sqtime_8)
    updated_at = db.Column(db.DateTime, default=sqtime_8, onupdate=sqtime_8)
    archive_id = db.Column(db.Integer, db.ForeignKey('archive.id'))

class Archive(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=sqtime_8)
    tweets = db.relationship('Tweet', backref='archive', lazy=True)
    resources = db.relationship('Resource', backref='archive', lazy=True)
    tech_tips = db.relationship('TechTip', backref='archive', lazy=True)

class ViewCount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content_type = db.Column(db.String(20), nullable=False)  # 'tweet', 'resource', 'tech_tip'
    content_id = db.Column(db.Integer, nullable=False)
    view_count = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=sqtime_8)
    updated_at = db.Column(db.DateTime, default=sqtime_8, onupdate=sqtime_8)

    __table_args__ = (db.UniqueConstraint('content_type', 'content_id', name='uix_content'),) 