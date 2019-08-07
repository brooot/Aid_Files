import pymysql
import re

f = open('dict.txt')
db = pymysql.connect('localhost', 'root',
                     'xzl1122', 'dict')
cur = db.cursor()

sql = 'insert into words (word,interpret) \
VALUES (%s,%s)'
a = 1
for line in f:
    # 　获取匹配内容元组　(word,mean)
    tup = re.findall(r'(\w+)\s+(.*)', line)[0]  
     '''要加[0]是因为返回的是查找到的子组的tupple组成的数组,
     如[(子组1,子组2),(),...,()]
     findall在有子组的情况下会只会返回子组匹配到的内容,
     当存在两个及以上的子组的时候便会将每次匹配到的子组放在一个元组内返回,
     组成一个列表的元素'''


    if a:
        print(tup)
        a = 0
    try:
        pass
        # cur.execute(sql, tup)
        # db.commit()
    except Exception:
        db.rollback()

f.close()
cur.close()
db.close()
