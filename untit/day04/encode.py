#-*-coding:gbk-*-  #文件编码是gbk
s="你好"  #python默认的就是unicode类型
s_gbk=s.encode("gbk")#将unicode转换成gbk
print("gbk",s_gbk)
gbk_to_utf8=s_gbk.decode("gbk").encode("utf-8")
print(s.encode())#encode后边不写格式，默认的是utf-8
print("utf-8",gbk_to_utf8)