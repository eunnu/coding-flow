def isEmpty():
    return front == rear


def is_Full():
    return rear == len(Q) - 1


def Qpeek():
    if isEmpty():
        print("empty")
    else:
        return Q[front+1]


def enQueue(item):
    global rear
    if is_Full():
        print("Full")
    else:
        rear += 1
        Q[rear] = item


def deQueue():
    global front
    if isEmpty():
        print("Empty")
    else:
        front += 1
        return Q[front]


Q = [0, 0, 0]
front = -1
rear = -1
enQueue(1)
enQueue(2)
enQueue(3)

for _ in range(3):
    print(deQueue())
