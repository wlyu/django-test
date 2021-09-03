import os
from celery import Celery,platforms #导入platforms

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')  # 设置django环境
platforms.C_FORCE_ROOT = True #加上这一行 //celeryd后台启动时root用户
app = Celery('mysite')
app.config_from_object('django.conf:settings', namespace='CELERY')  # 使用CELERY_ 作为前缀，在settings中写配置
app.autodiscover_tasks()  # 发现任务文件每个app下的task.py
app.conf.beat_schedule = {
    "every-mytask": {
        'task': 'polls.tasks.mytask',
        'schedule': 10,
        'args': ()
    }
}
@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
