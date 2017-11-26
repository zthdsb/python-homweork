from multiprocessing import Process, Manager


def f(d, l):
    d[1] = '1'
    d['2'] = 2
    d[0.25] = None
    l.append(1)
    print(l)


if __name__ == '__main__':
    with Manager() as manager:  #相当于 manager=Manager()
        d = manager.dict()  #   生成一个字典，可以在多个进程之间共享和传递

        l = manager.list(range(5))  #生成一个列表，可以在多个进程之间共享和传递
        p_list = []
        for i in range(10):
            p = Process(target=f, args=(d, l))
            p.start()
            p_list.append(p)
        for res in p_list:  #等待结果
            res.join()

        print(d)
        print(l)