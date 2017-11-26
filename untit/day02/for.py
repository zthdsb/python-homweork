'''for i in range(10):
    print("loop",i)'''#这个代码实现的功能是打印出0-10个数字
'''for i in range(0,10,2):  #这个表示打印从0到10的数字，其中每两个间隔2
    print("loop",i)'''


#与while相比较记忆

age_of_oldboy=56
for i in range(3):
    guess_age=int(input("guess age:"))
    if guess_age == age_of_oldboy :
        print("yes,you get it!")
        break
    elif guess_age > age_of_oldboy:
        print("think smaller!")
    else:
        print("think bigger!")
else:
     print("you have tried too many times,funk off")