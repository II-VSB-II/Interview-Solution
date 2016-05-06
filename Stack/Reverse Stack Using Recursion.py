def insertAtBottom(stack, item):
    if isEmpty(stack):
        push(stack, item)
    else:
        temp = pop(stack)
        insertAtBottom(stack, item)
        push(stack, temp)
 
# Below is the function that reverses the given stack
# using insertAtBottom()
def reverse(stack):
    if not isEmpty(stack):
        temp = pop(stack)
        reverse(stack)
        insertAtBottom(stack, temp)
        
def isEmpty( stack ):
    return len(stack) == 0
    
def createStack():
    stack=[]
    return stack

def push(stack,value):
    stack.append(value)
    
def pop(stack):
    return stack.pop()

def displayStack(stack):
    if len(stack)==0:
        print("Stack is Empty")
    else:    
        for i in range(len(stack)-1, -1, -1):
            print(stack[i], end ='->')

choice=True 
stack=createStack()  
print("Enter Choice Of Operation")
print("1 - Display Stack Elements")
print("2 - Check Size of Stack")
print("3 - Add Element in Stack")
print("4 - Delete Element From Stack")
print("5 - Reverse Stack Using Recursion")
print("6- Exit")    
while choice:
    t=int(input("Enter Choice: "))
    if t==1:
        displayStack(stack)
    elif t==2:
        print(stackemplty(stack))
    elif t==3:
        push(stack,int(input("Enter Item:")))
    elif t==4:
        print(stack.pop())
    elif t==5:
        reverse(stack)
    elif t==6:
        choice=False
    else:
        print("Wrong Choice")
    print("")
        
