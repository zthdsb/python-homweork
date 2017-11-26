try:
    a=1
    print(a)
    # open("te.text")
# except Exception as e:  #抓住所有错误（不建议用）
#     print("出错了",e)
except (KeyError,IndexError) as e:
    print("没有这个key",e)
except IndexError as e:
    print("列表操作错误",e)
except Exception as e:
    print("未知错误",e)

else:
    print("一切正常")

finally:
    print("不管有没有错，都执行")