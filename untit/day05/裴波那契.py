def fib(max):
    n,a,b=0,0,1
    while n<max:
        yield  b                                   #print(b)
        a,b=b,a+b
        n=n+1
    return "done"
#fib(10)
# f=fib(10)
g=fib(6)
while True:
    try:
        x=next(g)
        print('g:',x)
    except StopIteration as e:
        print('Genrator return value:',e.value)
        break
# print(f.__next__())
# print("=========")
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())


# for i in f:
#     print(i)