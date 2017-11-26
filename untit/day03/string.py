name="my name is \t{name},i'm {year} "
print(name.capitalize())#首字母大写
print(name.count("a"))#统计字符串中a的个数
print(name.center(50,"-"))#从第50个开始输出，前面后边输出-
print(name.endswith("ex"))#以什么结尾
print(name.expandtabs(tabsize=20))#tab键的空间大小
print(name.find("name"))#查找元素的起始位置，也可以用来索引
print(name[name.find("name"):8])
print(name.format(name='alex',year=23))
print(name.format_map( {'name':'alex','year':23}))
print(name.isalnum())#用来判断是否只具有英文字母和数字
print(name.isalpha())#判断是否只包含英文字符
print(name.isdecimal())#判断是否为十进制
print(name.isdigit())#判断是否为整数
print(name.isidentifier())#判断是否是合法的变量名
print(name.isnumeric())#判断是否只有一个数字
print(name.isupper())#是否都是大写

print('+'.join(['1','2','3']))
print(name.ljust(50,'*'))
print(name.rjust(50,'-'))
print("Alse".lower())
print('\nalse\n'.split())#去掉左右两边的空格和回车，lsplit是只去掉左边的，rsplit是只去掉右边的


p=str.maketrans("abcdef",'1234*/')
print("my name is elfc".translate(p))#可以用来编写密码

print('alex li'.replace('l','L',1))#替换，第三个参数表示替换的个数
print('alexl   lil'.rfind('l'))#返回最右侧查找值的位置
print('1+2+3+4'.split('+'))#分割
print('1\n234\n55'.splitlines())#按照换行符进行分割
print('kasd kl'.title())#每个的首字母大写
