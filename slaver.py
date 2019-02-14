"""
每次从master的redis队列中提取一个url，下载url对应的页面，
并把页面中的内容按照指定的格式保存到master的数据库中。
"""
import requests
from bs4 import BeautifulSoup
import time
import redis
import pymysql


def get_content(url):
    """
    获取指定页面的内容
    :param url: 网页的地址
    :return: 返回作者、标题、诗歌内容
    """
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    sons_div = soup.find(name='div', class_='sons')
    title = sons_div.h1.text
    author = sons_div.find(name='p', class_='source').text
    content = sons_div.find(name='div', class_='contson').text
    return title, author, content


def main():
    # 连接数据库   表sons
    conn = pymysql.connect(host='172.16.43.175',
                           port=3306,
                           db='1802C',
                           user='beiwang',
                           password='123456',
                           charset='utf8'
                           )
    # 创建游标
    cur = conn.cursor()

    rds = redis.Redis(host='172.16.43.175')
    # 获取 redis中键为"gushi_urls"的数据
    while True:
        time.sleep(1)
        url = rds.lpop('gushi_urls')
        if url is None:
            break
        title, author, content = get_content(url)
        sql = 'insert into sons(title,author,content,`name`) VALUES (%s,%s,%s,%s)'
        cur.execute(sql, (title, author, content, '段力华'))
        print(title, author, content)
        conn.commit()

    # 关闭游标
    cur.close()
    # 关闭数据库
    conn.close()


if __name__ == '__main__':
    main()
