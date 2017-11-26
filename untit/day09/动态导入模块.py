import importlib
aa=importlib.import_module('lib.aa')
# print(aa.C().name)

#断言
obj=aa.C()
assert type(obj.name) is str
print("obj.name 的类型是字符串的")

# 上诉断言等同于以下代码：
if type(obj.name) is str:
    print("obj.name 的类型是字符串的")
    绑定