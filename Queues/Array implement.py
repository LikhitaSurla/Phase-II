def enQueue(Q, ele):
    Q.append(ele)
    print(ele, " enqueued successfully")
 
 
def deQueue(Q):
    if len(Q) == 0:
        print("Queue is empty")
        return
    print(Q[0], " element is getting deleted")
    Q.pop(0)
 
Q = []
enQueue(Q, 10)
enQueue(Q, 20)
enQueue(Q, 30)
enQueue(Q, 40)
print(Q)
 
deQueue(Q)
print(Q)
 
deQueue(Q)
print(Q)
 
deQueue(Q)
print(Q)
 
deQueue(Q)
print(Q)
 
deQueue(Q)
print(Q)