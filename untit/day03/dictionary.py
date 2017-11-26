#字典key-value 是无序的
info={
    'stu1101':"TengLan Wu",
    'stu1102':"LongZe LuoLa" ,
    'stu1103':"Xiaoze Maliya"
}
'''b={
    'stu1101':"Alex",
    1:3,
    2:5
}
info.update(b)#将两个字典合并，有交叉的就合并更改，没有交叉的就添加
print(info)
print(info.items())
c=dict.fromkeys([6,7,8],[1,{"name":"alex"},444])#创建一个字典，其中每个关键字都添加一个项目
print(c)
c[7][1]["name"]="Jack Chen"
print(c)
'''
#循环
for i in info:
    print(i,info[i])#这种方式更好一些

for k,v in info.items():
    print(k,v)

'''#输出和替换 添加
print(info['stu1101'])
info['stu1101']='武藤兰'
info['stu1104']='Canglaoshi'
#删除
#del info['stu1101']
#info.pop('stu1102')
#print(info)

#查找
print(info.get('stu1103'))
print('stu1103' in info)
'''
#多级字典的嵌套
'''av_catalog = {
    "欧美":{
        "www.youporn.com": ["很多免费的,世界最大的","质量一般"],
        "www.pornhub.com": ["很多免费的,也很大","质量比yourporn高点"],
        "letmedothistoyou.com": ["多是自拍,高质量图片很多","资源不多,更新慢"],
        "x-art.com":["质量很高,真的很高","全部收费,屌比请绕过"]
    },
    "日韩":{
        "tokyo-hot":["质量怎样不清楚,个人已经不喜欢日韩范了","听说是收费的"]
    },
    "大陆":{
        "1024":["全部免费,真好,好人一生平安","服务器在国外,慢"]
    }
}
av_catalog["大陆"]["1024"][1]="好人一生平安"
av_catalog.setdefault("台湾",{"www.cctv.com":["hehe"]})#添加新的标签，在字典中取，如果有台湾这个标签那就返回他原本的值，如果没有就添加进去
print(av_catalog)
print(av_catalog.values())
print(av_catalog.keys())
'''
