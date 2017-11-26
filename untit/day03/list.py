
names=["zhangyang","guyun","xiangpeng",["alse","jack"],"gupeng"]

print(names)
print(names[0],names[2])
print(names[1:3])#起始位置的值取，结束位置的值不取（切块）
print(names[-1])
print(names[-3:-1])#由于顾头不顾尾，所以最后一个值取不到，这时可以省略最后一个位置从而取到，如下代码
print(names[-3:])#这样就是取从-3开始直到结束的值，同样也可以省略开始的值就从第一个开始取
#添加
names.append("leihaifeng")#最后位置追加一个元素
names.insert(1,"leihaifeng")#任意位置添加，其中第一个参数是位置，第二个是值
#替换
names[2]="zhangtihe"
#删除
names.remove("zhangyang")
del names[0]
names.pop()#默认删除最后一个，输入下标就能删除相应位置对应的值
print(names)
#寻找某个值的位置
print(names.index("zhangyang"))#其中index表示索引
print( names[names.index("zhangyang")])

print(names.count("zhangpeng"))#统计列表中有几个zhangpeng
names.reverse()#列表翻转
names.sort()#列表排序，按照首字母排序
names.extend()#列表合并


