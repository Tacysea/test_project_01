from redis import StrictRedis
class Config(object):
    DEBUG = None
    # 设置密钥
    SECRET_KEY = 'xjXwFyIzzcspKMfeOSCJcep4m7yaWt6P6iqrrtw+0FM='
    # 链接数据库
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@127.0.0.1:3306/test_01'
    # 设置数据库动态追踪修改
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 配置redis信息
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379
    SESSION_TYPE = 'redis'
    SESSION_RDIES = StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    SESSION_USE_SIGNER = True
    PERMANENT_SESSION_LIFETIME = 86400

class development_model(Config):
    DEBUG = True

class production_model(Config):
    DEBUG = False

config = {

    'development':development_model,
    'production':production_model
}