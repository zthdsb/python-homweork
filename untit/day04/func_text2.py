# def text(x,y):
#     print(x)
#     print(y)
# text(1,2)


#含默认参数的
# def text(x,y=2):
#     print(x)
#     print(y)
# text(1,6)
#默认参数特点，调用函数的时候，默认参数非必须传输



#参数组 *arge接收N个位置参数，转换成元祖的形式
# def text(*arge):
#     print(arge)
# text(1,2,8,3,5,6)
# text(*[1,2,3,4,5]) #erge=tuple([1,2,3,4,5])
#
# def text2(x,*args):
#     print(x)
#     print(args)
# text(1,2,3,4,5,6)
#
# #**keargs  把N个关键字参数，转化成字典的格式
# def text3(**kwargs):
#     print(kwargs)
#     print(kwargs['name'])
#     print(kwargs['age'])
#     print(kwargs['sex'])
# text3(name='alex',age=8,sex='f')
# text3(**{'name':'alex','age':8,'sex':'f'})

#
# def text3(name, **kwargs):
#     print(name)
#     print(kwargs)
# text3('alex',age=6,sex='f')

def text3(name, age=24,**kwargs):
    print(name)
    print(age)
    print(kwargs)
text3('alex',habyt='tesla',sex='f',age=5)

def text3(name, age=24,*arge,**kwargs):
    print(name)
    print(age)
    print(arge)
    print(kwargs)
text3('alex',habyt='tesla',sex='f',age=5)

#函数当中在嵌套一个函数
def text3(name, age=24,*arge,**kwargs):
    print(name)
    print(age)
    print(arge)
    print(kwargs)
    text4(45)
def text4(socure):
    print("from the %s"%socure)
text3('alex',habyt='tesla',sex='f',age=5)