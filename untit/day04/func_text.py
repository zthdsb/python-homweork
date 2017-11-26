# # 定义一个函数
# def func1():
#     '''texting'''
#     print("in the func1")
#     return 0
# # 定义一个过程
# def func2():
#     print("in the func2")
#
#
# x=func1()
# y=func2()
# print("in the func1 is %s"%x)
# print("in the func2 is %s"%y)


import time
def loge():
    with open("text",'a+') as f:
        time_format = '%Y-%m-%d %X'
        tiem_count = time.strftime(time_format)
        f.write("%s end action\n" %tiem_count)
def text1():
    print("in the text1")
    loge()
def text2():
    print("in the text2")
    loge()
text1()
text2()