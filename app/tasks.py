# tasks.py
from celery import shared_task

from .add_data import ImportToModel
from .parser import parser

@shared_task
def update_schedule():
    print('Задача парсинг json  выполняется')
    parser()
    print('Задача парсинг json выполнена')
    print('Задача парсинг модель  выполняется')
    i = ImportToModel()
    import asyncio
    asyncio.run(i.import_data_async())
    print('Задача парсинг модель выполнена')