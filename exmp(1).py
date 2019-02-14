import pymysql

conn = pymysql.connect(host='172.16.43.175', port=3306,
                       user='beiwang',
                       password='123456',
                       db='python1802',
                       charset='utf8')

cur = conn.cursor()

data = {
    'choices': [
        {'question': '下面哪个是桥接模式：',
         'a': 'NAT',
         'b': 'Bridged',
         'c': 'Host-Only',
         'd': 'user-defined',
         'answer': 'B',
         'knowledge': '虚拟机桥接模式',
         'is_mult_choice': 0,
         'author': '张文斌'
         }
    ]
}
# 取出所有choices
choices = data['choices']
print(choices)
# 遍历每个choice
for choice in choices:
    print(choice)
# 把每个choice添加到数据库
sql = 'insert into choices(question,a,b,c,d,answer,knowledge,is_mult_choice,author) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)'
cur.execute(sql, (
    choice['question'], choice['a'], choice['b'], choice['c'], choice['d'],
    choice['answer'], choice['knowledge'], choice['is_mult_choice'],
    choice['author']))

# 提交变更
conn.commit()
cur.close()
conn.close()
