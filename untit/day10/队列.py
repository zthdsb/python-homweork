import queue
q=queue.PriorityQueue()#  有优先级的
q.put((8,"zth"))
q.put((4,"res"))
q.put((1,"yut"))
print(q.get())
print(q.get())
print(q.get())
