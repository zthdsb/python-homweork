'''f = open("yesterday2",'r',encoding='utf-8')
print (f.tell())#查看光标的位置
print(f.readline())
print(f.readline())
print(f.readline())
print(f.tell())
f.seek(0)  #将光标回到指定位置
print(f.readline())
print(f.tell())
print(f.encoding)
print(f.fileno())#返回文件的一个编号
#print(f.flush())

'''
#f = open("yesterday2",'r+',encoding='utf-8')#r+表示读写(最常用)
#f = open("yesterday2",'w+',encoding='utf-8')#w+表示写读
#f = open("yesterday2",'a+',encoding='utf-8')#a+追加读写
#f = open("yesterday2",'rb')#rb二进制文件
f = open("yesterday2",'wb')#
f.write("hello binary\n".encode())
#f.seek(10)#截断，从文章的起始位置开始   截断10个
'''print(f.readline())
print(f.readline())
print(f.readline())
f.write("------------------------")#从最后位置写入,并且只能从最后边写入
print(f.readline())
'''



'''
import sys,time
for i in range(20):
    sys.stdout.write("#")#标准输出
    sys.stdout.flush() #慢慢刷出来
    time.sleep(0.2)#延时显示的
'''
