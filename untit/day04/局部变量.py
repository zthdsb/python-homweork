

'''
school='shanghai'

def change(name):
    global school#在函数中只有“global+全局变量的名称”这种形式，全局变量的值才能彻底的更改，否则只在函数中改一次
    school = 'haishi'

    print("before name is %s"%name)
    name="ALEX"
    print("after change name is %s"%name)
    print("school is：",school)

print(school)
name='alse'
change(name)
print(school)

'''


#字符串形式的全局变量可以被修改

name=["Alse","adam","jack"]
def change(name):
    print("the name is",name)
    name[0]="MACK"

print(name)
change(name)
print(name)