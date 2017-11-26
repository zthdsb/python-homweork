# f=open("yesterday2",'r',encoding="utf-8")
# f_new=open("yesterday3",'w',encoding="utf-8")
# for lain in f:
#     if "肆意的快乐等我享受" in lain:
#         lain=lain.replace("肆意的快乐等我享受","肆意的快乐等alax享受")#替换，用后边的内容替换前面的
#     f_new.write(lain)
#     # f.close()
#     # f_new.close()

#with语句可以将打开的文件自动关闭，同时也可以打开多个文件
with open("yesterday2",'r',encoding="utf-8") as f,\
        open("yesterday3",'w',encoding="utf-8")as f2:
    for lain in f:
        print(lain.strip())