from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


# 初始化数据库操作
# 初始化数据库操作
def init_db(app):
    # 配置数据库的连接地址
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1:3306/flask-orm?charset=utf8'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app=app)
    migrate.init_app(app, db)


"""
==============支付宝配置=================
"""
# import os
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# # 支付宝注册应用生成的IP
# APP_ID = '2016092300580718'
#
# # 沙箱环境支付网关就是沙箱那面那个关口
# PAY_URL_DEV = 'https://openapi.alipaydev.com/gateway.do'
# # 正式支付的网关
# PAY_URL = 'https://openapi.alipay.com/gateway.do'
# # 公钥,私钥
# APP_PRIVATE_KEY_STR = open(os.path.join(BASE_DIR, 'pay/app_private_key.pem')).read()
# APP_PUBLICK_KEY_STR = open(os.path.join(BASE_DIR, 'pay/app_public_key.pem')).read()

"""
==============支付宝配置=================
"""
