#data = open("yesterday").read()   #打开并读里边的内容
'''f = open("yesterday",'r',encoding="utf-8")#文件句柄（文件的内存对象）'r'模式是读模式，不能写"w’模式是写模式，是创建一个新的文档
date=f.read()
print(date)

f2 = open("yesterday2",'w',encoding="utf-8")#‘w’模式只进行写的操作
f2.write("我爱北京天安门,\n")
f2.write("天安门上太阳升。")

f2 = open("yesterday2",'a',encoding="utf-8")#‘a’模式相当于append 追加
f2.write("我爱北京天安门123\n")
f2.write("天安门上太阳升4566")
#关闭文件（不写系统会自动关闭）
f2.close()
'''



#这种方式占用内存比较多
f = open("yesterday2",'r',encoding="utf-8")
'''for index,li in enumerate(f):
    print(li.strip())
    if index == 9:
        print ("----我是分割线---")
 '''

#还有一种简单的方式
count=0
for lain in f:
    if count==9:
        print("------分割线------")
        continue
    print (lain)
    count+=1



for i in range(5):
    print(f.readline())#读5行