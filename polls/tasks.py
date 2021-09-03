import time
from celery import shared_task


@shared_task(name="add")
def add(x, y):
    time.sleep(10)
    print("执行函数")
    return x + y


@shared_task
def mytask():
    print("mytask----------")
    return "ok"
