'''
将十进制转换为三进制的整数
'''
def change_num(num):
    '''

    :param num: 一个十进制的整数
    :return: 对应的三进制数字
    '''
    three_list = list()
    while num:
        mod = num % 3
        num = num // 3
        three_list.append(mod)
    three_list.reverse()
    three_num = '0T'+''.join([str(i) for i in three_list])
    if num==0:
        three_num = '0T'+'0'
    # print(three_list)
    print(three_num)


def xxx():
    xc = int(input('请输入整数： '))
    change_num(xc)
xxx()