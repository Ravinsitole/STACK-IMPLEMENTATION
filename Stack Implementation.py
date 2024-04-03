stack=[]
while True:
    choice=int(input("""
            1 Push Item
            2 Pop Item
            3 Peek Item
            4 Size
 Enter programme:-"""))
    if choice==1:
        n=input("Enter the value:")
        stack.append(n)
        print(stack)

    if choice==2:
        if len(stack)==0:
            print("Empty stack:")
        else:
            p=stack.pop()
            print(p)
            print(stack)

    elif choice==3:
        if len(stack)==0:
            print("Empty stack")
        else:
            print("Last stack Value:", stack[-1])

    elif choice==4:
        print("Display stack  Size:",stack)
