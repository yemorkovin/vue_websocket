from dotenv import load_dotenv
import os
import mysql.connector
from mysql.connector import Error
import json


class DB:
    def __init__(self):
        load_dotenv()
        self.db_config = {
            'host': os.getenv('DB_HOST'),
            'port': os.getenv('DB_PORT'),
            'database': os.getenv('DB_NAME'),
            'user': os.getenv('DB_USER'),
            'password': os.getenv('DB_PASSWORD')
        }

        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(**self.db_config)
            if self.connection.is_connected():
                print('Подключение к MySQL успешно установлено!')
                self.cursor = self.connection.cursor()
                self.cursor.execute('''
                    create table if not exists schedule(
                    id int auto_increment primary key,
                    day_of_week text,
                    time text,
                    format text,
                    class text,
                    students text,
                    subject text,
                    teacher text,
                    cabinet text,
                    link text,
                    teacher_z text,
                    link_z text     
                    )               
                ''')
                self.connection.commit()
        except Error as e:
            print(f'Ошибка подключения к БД: {e}')

    def getFromJson(self):
        str_json = open('json/data.json', 'r').read()
        return json.loads(str_json)

    def save(self):
        self.connect()
        self.cursor.execute('delete from schedule')
        self.connection.commit()
        for time, data in self.getFromJson().items():
            d = (data[0].split('_')[1], time, data[1], data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9])
            self.cursor.execute('insert into schedule (day_of_week,time,format,class,students,subject,teacher,cabinet,link,teacher_z,link_z) values (?,?,?,?,?,?,?,?,?,?,?)', d)
            self.connection.commit()




db = DB()
db.save()
#print(db.getFromJson())