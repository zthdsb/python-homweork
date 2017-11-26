list_1=[1,4,5,7,3,6,7,9]
list_1=set(list_1)  #将列表换成集合，去掉重复的元素

list_2=set([4,5,6,58,65,48,])
print(list_1,type(list_1))
print(list_2)

l=list_1.intersection(list_2)#两个集合的交集
print(l)

print(list_1.union(list_2))#两个集合的并集

#差集 在集合一里有的但是集合二中没有的（去掉集合二中有的 ）
print(list_1.difference(list_2))

#子集
list_3=set([1,3,9,7])
print(list_1.issubset(list_2)) #判断list1是不是2的子集
print(list_1.issuperset(list_2))#判断list1是不是2的父集
print(list_3.issubset(list_1))

#对称差集
print(list_1.symmetric_difference(list_2))#去掉两个集合都有的元素，在把两个集合合并

list_3=set([1,3,9,7])
list_4=set([5,6,8])
print(list_3.isdisjoint(list_4)) #判断有没有交集

#交集
print(list_1 & list_2)
#并集
print(list_1 | list_2)
#差集
print(list_1 - list_2) #在list1中不在2中
#对称差集
print(list_1 ^ list_2)

#添加
list_1.add(23)#添加一个元素
list_1.update([22,33,44])#添加多个元素
print(list_1)
#删除
list_1.remove(22)
print(list_1.pop())#删除任意元素并将删除的元素值返回输出出来

print(list_1.discard(222))