from flask import Blueprint


# 创建蓝图对象

blu = Blueprint('lgh', __name__)

# 使用蓝图对象

from . import views

