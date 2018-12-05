from flask import Blueprint, request, render_template, redirect

from apps import ext
from apps.ext import db
from apps.user.models import User

user = Blueprint('user', __name__)


@user.route("/add/", methods=['GET', 'POST'])
def add():
    # user = User(username='娇娇', price=888)
    # db.session.add(user)
    # db.session.commit()
    # 批量添加
    db.session.add_all([User(username='娇娇1', price=888),
                        User(username='娇娇2', price=888),
                        User(username='娇娇3', price=888)])
    db.session.commit()
    return '添加成功'


@user.route('/find/')
def find():
    users = User.query.all()

    return render_template('users.html', users=users)


@user.route('/detail/')
def details():
    #获取到get请求的id
    uid = request.args.get('uid')
    """
    user = User.query.filter(User.username == '娇娇').frist()
    # filter_by只支持关键字参数
    user = User.query.filter_by(username='娇娇').frist()
    # get方法只能查询主键
    # 如果没有返回none
    """
    user = User.query.get(uid)

    return render_template('details.html',user=user)

# from
# def pay(request):
#     #实例化Alipay对象
#     alipay = AliPay(
#         appid=settings.APP_ID,
#         app_notify_url=None,
#         app_private_key_string=settings.APP_PRIVATE_KEY_STR,
#         alipay_public_key_string=settings.APP_PUBLICK_KEY_STR,
#         sign_type='RSA',
#         debug=True,
#     )
#
#     # 生成支付的参数
#     '''
#     subject 支付的标题
#     out_trade_no 生成的订单号
#     total_amount 支付的总金额
#     return_url  支付完成之后前端跳转的界面 get请求
#     notify_url 支付完成后台回调接口  post请求
#     '''
#     order_str = alipay.api_alipay_trade_page_pay(
#         subject='91支付6',
#         out_trade_no='1234653678',
#         total_amount='588',
#         return_url='https:www.baidu.com',
#     )
#     return redirect(ext.PAY_URL_DEV+'?'+order_str)

