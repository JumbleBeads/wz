'''
练习2 :
   创建数据库 dict
   创建数据表  words
     id    word    mean
   将单词本中的单词插入数据库
'''
import pymysql

f = open('dict.txt')

#连接数据库
db = pymysql.connect(user = 'root',passwd = '123456',database = 'stu',charset = 'utf8')

#获取游标
cur = db.cursor()

sql = "insert into words (word,mean) values (%s,%s)"

for ling in f:
    tmp =ling.split(' ',1)
    word = tmp[0]
    neam = tmp[1].split()
    cur.execute(sql,[word,neam])
try:
    db.commit()
except:
    db.rollback()

cur.close()
db.close()