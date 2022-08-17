def push(item):
    global top
    top += 1
    stack[top] = item

def pop():
    if len(stack) == 0:
        return
    else:
        return stack.pop()

stack = [0]*3
top = -1

for _ in range(3):
    push(input())

for _ in range(3):
    print(pop())

