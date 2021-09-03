import pymysql

from .celery import app as celery_app

__all__ = ['celery_app']
pymysql.install_as_MySQLdb()


from skywalking import agent, config
#default grpc
config.init(collector='http://127.0.0.1:8888',protocol_type="grpc",service='python_service')
agent.start()