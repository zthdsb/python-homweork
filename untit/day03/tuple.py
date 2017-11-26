#元组中的元素是不能改变的，用括号包括元素
salary=int(input("You salary is:"))
T=([1,'iphone',2800],
[2, 'Mac Pro',1200],
[3,'Starbuck Latter',31],
[4,'Alex Python',81])
while salary > 0:
    print(T)
    i=int(input("Please choise the number thing what you want:"))
    if i==1:
        print("Added [iphone] to your shopping cart")
        salary=salary-2800
        print("You salary is:", salary)
    elif i==2:
        print("Added [Mac Pro] to your shopping cart")
        salary = salary-1200
        print("You salary is:", salary)
    elif i==3:
        print("Added [Starbuck Latter] to your shopping cart")
        salary = salary - 31
        print("You salary is:", salary)
    elif i==4:
        print("Added [Alex Python] to your shopping cart")
        salary = salary - 81
        print("You salary is:", salary)
    else:
        print("WARNING")
print("You salary isn't enough!")

