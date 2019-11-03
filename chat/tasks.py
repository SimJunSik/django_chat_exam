from __future__ import absolute_import, unicode_literals 
from celery import shared_task 
from .models import *

@shared_task 
def add(x, y): 
    return x + y 
    
    
@shared_task 
def mul(x, y): 
    return x * y 
    
@shared_task 
def xsum(numbers): 
    return sum(numbers)


@shared_task
def save_chat(sender, room_name, text):
    test = Test.objects.create(
        sender = sender,
        room_name = room_name,
        text = text,
    )
    test.save()

    return True
