#实现三次年龄的猜测在第三次尝试后输出你想继续的提示

age_of_oldboy=56
count=0
while count<3:
    guess_age=int(input("guess age:"))
    if guess_age == age_of_oldboy :
        print("yes,you get it!")
        break
    elif guess_age > age_of_oldboy:
        print("think smaller!")
    else:
        print("think bigger!")
    count += 1
else:
     print("you have tried too many times,funk off")

#上诉程序运行三次后会退出，接下来的程序能够自己控制是否继续
age_of_oldboy = 56
count = 0
while count < 3:
    guess_age = int(input("guess age:"))
    if guess_age == age_of_oldboy:
        print("yes,you get it!")
        break
    elif guess_age > age_of_oldboy:
        print("think smaller!")
    else:
        print("think bigger!")
    count += 1
    if count== 3:
        key=input("Do you want to keep guessing?")
        if key !="n":
            count=0
else:
    print("you have tried too many times,funk off")
