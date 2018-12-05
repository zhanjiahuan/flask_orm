from flask import Flask
from apps.ext import init_db
from apps.user.views import user


# 入口
def create_app():
    app = Flask(__name__)
    app.debug = True
    # 注册蓝图
    register_bp(app)
    # 初始化数据库相关配置
    init_db(app)
    return app


# 注册蓝图对象
def register_bp(app):
    # 注册用户模块
    app.register_blueprint(user, url_prefix='/user')
