import os

rs = '/Users/DYJ05/Desktop/新建文件夹'
def file_dir(arg):

    for i in [os.path.join(arg,ph) for ph in os.listdir(arg)]:
        print(i)
        if os.path.isdir(i):
            file_dir(i)



print(file_dir(rs))




'''
rs = os.getcwd()   #获取当前路径

rss = os.walk(rs)
for dirs in rss:
    print(dirs)

'''
