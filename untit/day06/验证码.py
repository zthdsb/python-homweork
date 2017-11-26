import random
char=""
for i in range(4):
    count=random.randrange(0,4)
    if count==i:
        tmy=random.randint(0,9)
    else:
        tmy=chr(random.randint(65,90))
    char += str(tmy)   #????????????
print(char)

