data = {
    '北京':{
        "昌平":{
            "沙河":["oldboy","test"],
            "天通苑":["链家地产","我爱我家"]
        },
        "朝阳":{
            "望京":["奔驰","陌陌"],
            "国贸":{"CICC","HP"},
            "东直门":{"Advent","飞信"},
        },
        "海淀":{},
    },
    '山东':{
        "德州":{},
        "青岛":{},
        "济南":{}
    },
    '广东':{
        "东莞":{},
        "常熟":{},
        "佛山":{},
    },
}

while True:
    for i in data:
        print(i)   #打印一级列表
    city=input("请选择列表中的城市：")
    while city !='q':
        for j in data[city]:
            print(j)     #打印所选的二级列表
        city1 = input("请选择列表中的城市：")
        while city1 !='q':
            for k in data[city][city1]:
                print(k)   #打印三级列表
            city2 = input("请选择列表中的城市：")
            while city2 !='q':
                for l in data[city][city1][city2]:
                    print(l)   #打印四级列表
                city3=input("输入p返回上一层")
                if city3=='p':
                    pass
                elif city3=='q':
                    city2='q'
            break
        break
    break