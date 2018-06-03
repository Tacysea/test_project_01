from redis import StrictRedis
class Config(object):
    DEBUG = None
    # 设置密钥
    SECRET_KEY = 'xjXwFyIzzcspKMfeOSCJcep4m7yaWt6P6iqrrtw+0FM='
    # 链接数据库
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@127.0.0.1:3306/test_01'
    # 设置数据库动态追踪修改
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 配置redis数据库的ip和端口号
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379
    # 设置保存session信息的数据库类型
    SESSION_TYPE = 'redis'
    SESSION_RDIES = StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    # 使用签名给session信息编码（加密）
    SESSION_USE_SIGNER = True
    # 设置session信息保存时间，以秒为单位，设置时间为一天
    PERMANENT_SESSION_LIFETIME = 86400

class development_model(Config):
    DEBUG = True

class production_model(Config):
    DEBUG = False

config = {

    'development':development_model,
    'production':production_model
}