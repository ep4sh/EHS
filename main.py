# EXPERT HOME 4 spy logger by SOFTEX
# moving ScreenShots from database to OUTDIR
# MIT lic

import os
import sqlite3
import datetime
import base64

#Настройки / Settings
appdir = '/home/ep4sh/appdata/'
outdir = appdir

# создаем имя базы (S<текущая_дата>)
db_string = "S"+"15.11.2018"
#db_string = "S"+ datetime.datetime.today().strftime("%d.%m.%Y").rstrip("\n\r")

db_byte = db_string.encode()
db_byte = base64.b64encode(db_byte)
db_now = db_byte.decode()

# запись в файл
def write_file(data, filename):
    with open(outdir+filename+str(datetime.datetime.now())+".jpg", 'wb') as f:
        f.write(data)

# проходим по директории и ищем базу с текущей датой
for db in os.listdir(appdir):
    if db == db_now:
        try:        
            #выводим название пойманной базы
            print("found: "+db)
            conn = sqlite3.connect(appdir+db)
            cc = conn.cursor()
            #грабим скрины
            cc.execute("select Stream from Screenshots;")
            pics = cc.fetchall()
            for pic in pics:
                write_file(pic[0], "SC" )
        #ловим ошибки        
        except sqlite3.Error as er:
            print('er:', er )
        #закрываем соединение    
        finally:
            cc.close()
            conn.close()
    