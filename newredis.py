# redis是key-value数据库
# key是唯一的
# value的类型可以是字符串，列表，


import redis

res = redis.Redis(host='172.16.43.241',port=6379,db = 0,encoding='utf-8')

urls = [
    'http://www.baidu.com',
    'http://www.taobao.com'
]


URLS_KEY = 'urls'
res.lpush(URLS_KEY,'http://www.baidu.com')   #lpush  从左边添加
res.lpush(URLS_KEY,'http://www.sogou.com')
res.rpush(URLS_KEY,'http://www.taobao.com')

print(res.rpop(URLS_KEY))    #rpop从右边取出
print(res.lrange(URLS_KEY,0,-1))
print(res.blpop(URLS_KEY))   #blpop 如果没有值等待，直到有值为止