L="你好"
print(L)

#在格式输出方面，主要有三种方式：
#1.用替代符代替位置，然后在输出位置依次对应相应的要输出的值
#2.用大括号定义一个变量，然后在外边对变量进行相应的赋值
#3.用大括号对应相应的位置，然后在外边对相应的位置进行赋值

name= input("name:")
age= int(input("age:"))
print(type(age),type(str(age)))
job= input("job:")
salary= input("salary:")
info='''
--------info of %s ------
Name:%s
Age:%d    
Job:%s
Salary:%s
'''%(name,name,age,job,salary)   #%d 是数字类型  %s是字符串类型
print(info)
info2='''
-------info of {_name}-----
Name:{_name}
Age:{_age}   
Job:{_job}
Salary:{_salary}
'''.format(_name=name,
            _age=age,
            _job=job,
            _salary=salary)
print(info2)
info3='''
-------info of {0}-----
Name:{0}
Age:{1}   
Job:{2}
Salary:{3}
'''.format(name,age,job,salary)
print(info3)
