# bin()#把十进制转成二进制
# callable([])#判断可不可以调用
# def sayhi(n):
#     print(n)
# sayhi(5)
# s=lambda n:print(n)
# s(5)
# a=lambda n:3 if n<4 else n
# print(a(6))
res=map(lambda n:n*n,range(10))
for i in res:
    print(i)