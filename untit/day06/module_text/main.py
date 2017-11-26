# import module_1  # 可以调用module_1中的函数，变量等 相当于将module运行了一遍后所有的代码复制给了module_1 module_1=“所有代码” 想调用里边的代码要加上前面的前缀  module_1.name
#
#
# print(module_1.name)
# module_1.say_hello()
# from module_1 import logger as logger_1
# def logger():
#     print("this is in main")
#
# logger()
# logger_1()


#导入包
# import package_text  #实际就是执行package_text 中的_init_.py 文件

import sys,os
print(sys.path)
print(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))
x=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(x)
import module_2
module_2.say()