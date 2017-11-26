

'''names=["zhangyang","guyun","xiangpeng",["alse","jack"],"gupeng"]
names2=names.copy()
names3=names
print(names)
print(names2)
names[2]="向鹏"
print(names)
print(names2)
names[3][0]="ALSA"#列表里的是内存地址，所以names[3][0]中的值也改了
print(names)
print(names2)
print(names3)
print(names[0:-1:2])

for i in names:
    print(i)
'''

#浅拷贝的三种代码方式
#p1=copy.copy(person)
#p2=person[:]
#p3=list(person)
#浅拷贝  (可以用来构建关联账号);类似于Lisa是Adam的老婆，他们有一个共同账号，Adam取钱后Lisa也能知道
person=['name',['saving',100]]
p1=person[:]
p2=person[:]
p1[0]="Adam"
p2[0]="Lisa"
person[1][1]=50
print(p1)
print(p2)