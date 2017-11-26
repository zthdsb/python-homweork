from urllib import request
import gevent,time
def func1(url):
    print("GET:%s"%url)
    resp=request.urlopen(url)
    data= resp.read()
    print("%d  besty recover from %s "%(len(url),url))
    # f=open("wangye.html","wb")
    # f.write(data)
    # f.close()

# func1("https://www.baidu.com")
yibu_start_time=time.time()
gevent.joinall([
    gevent.spawn(func1,"http://www.cnblogs.com/alex3714/articles/5248247.html"),
    gevent.spawn(func1,"http://www.cnblogs.com"),
    gevent.spawn(func1,"http://www.cnblogs.com/alex3714/")
])
print("异步所用时间",time.time()-yibu_start_time)


gevent_list=[
"http://www.cnblogs.com/alex3714/articles/5248247.html",
"http://www.cnblogs.com",
"http://www.cnblogs.com/alex3714/"
]
tongbu_start_time=time.time()
for i in gevent_list:
    func1(i)
print("同步所用时间：",time.time()-tongbu_start_time)