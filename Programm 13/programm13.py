stk = [2, 5, 13, 7, 234, 84]
top = len(stk) - 1
def Pop(stk):
    global top
    if stk:
        stk.pop()
        top = len(stk) - 1
    else:
        print("UnderFlow")
    return stk
def Push(item, stk):
    global top
    stk.append(item)
    top = len(stk) - 1
    return stk
    
print(Pop(stk), top)
print(Push(35, stk), top)