
#引用模块，第三方库
'''import sys
print(sys.path) #path打印环境变量
print(sys.argv)'''


'''import os
#cmd_res=os.system("dir")  #执行命令，不保存结果
cmd_res=os.popen("dir").read() #能够打印出结果
print("-->",cmd_res)
#os.mkdir("new_dir")#创建一个文件夹'''
#import login
'''其中这个login模块是在同一目录下的自己编写的，只有在同一个目录下才能调用；当他不在一个目录下的时候
   有两种方法可以解决：1.直接把相应的模块拷贝到当前目录；2.修改环境变量，添加模块所在的目录。'''


#三元运算
a,b,c=1,2,3,
d=a if a<b else c