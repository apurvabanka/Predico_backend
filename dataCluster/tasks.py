# Create your tasks here
from __future__ import absolute_import, unicode_literals

from celery import shared_task
import time


from celery.decorators import task

@task(name="sum_two_numbers")
def add(x, y):
    time.sleep(10)
    return x + y