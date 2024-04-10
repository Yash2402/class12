stk = []
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

def Display(stk):
    global top
    top = len(stk)-1
    for i in range(top, -1, -1):
        if i != top:
            print("      ",stk[i])
        else:
            print(f"Top -> {stk[top]}")

run = True
while run:
    print("Choose From Following Options:\n\
          \t 1. Push\n\
          \t 2. Pop\n\
          \t 3. Display\n\
          \t 4. Exit.\n")
    choice = int(input("Enter Your Choice: "))
    if choice == 1:
        element = eval(input("Enter the item to be pushed: "))
        Push(element, stk)
    if choice == 2:
        Pop(stk)
    if choice == 3:
        Display(stk)
    if choice == 4:
        run = False




        