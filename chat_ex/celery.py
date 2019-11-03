from __future__ import absolute_import, unicode_literals 
import os 
from celery import Celery 
app = Celery('chat_ex', broker='redis://localhost:6379/0')
app.config_from_object('chat_ex.settings', namespace='CELERY')
app.autodiscover_tasks() 
@app.task(bind=True) 
def debug_task(self): 
    print('Request: {0!r}'.format(self.request))
