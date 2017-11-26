product_list=[
    ('Iphone',5800),
    ('Mac',9800),
    ('Bike',800),
    ('Watch',10600),
    ('Coffee',31),
    ('Alex Pyhton',120)
]
shopping_list=[]
salary=input("你的余额是：")
if salary.isdigit():
    salary=int(salary)
    while True:
        for index,product in enumerate(product_list):#enumerate是提取列表前的序号的
            print(index,product)
        #for product in product_list:
            #print(product_list.index(product),product)
        choise = input("请选择你想购买的产品编号")
        if choise.isdigit():
            choise=int(choise)
            if choise < len(product_list) and choise>=0:
                user_choise=product_list[choise]
                if user_choise[1]<= salary:
                    shopping_list.append(user_choise)
                    salary -=user_choise[1]
                    print("Added \033[32;1m%s\033[0m into shopping cart,your salary is \033[31;1m%s\033[0m"%(user_choise[0],salary))
                else:
                    print("你的钱不足以支付当前所选产品")
            else:
                print("没有你选择的产品编号，请重新选择")
        elif choise=='q':
            print('''-------product list--------''')
            for p_choise in shopping_list:
                print(p_choise)
            print("你的余额是\033[31;1m%s\033[0m"%(salary))
            exit()
else:
    print("WORNING")





