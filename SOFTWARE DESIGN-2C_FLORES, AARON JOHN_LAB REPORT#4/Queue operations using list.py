import queue

q = queue.Queue()

q.put(13)
q.put(22)
q.put(20)
q.put(7)
q.put(2)


n = q.qsize()
for i in range(n):
   
    x = q.get()
    for j in range(n - 1):
     
        y = q.get()
        if x > y:
            q.put(y)
        else:
            q.put(x)
            x = y  
    q.put(x)

while (q.empty() == False):
    print(q.queue[0], end=" ")
    q.get() 
