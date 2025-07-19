todo =[
    
]



while True:
    print("enter 1,2,3,4")
    option=int(input())
    if option==1:
        add=input()
        todo.append(add)
        print(todo)
    elif option==2:
        remove=input()
        todo.remove(remove)
        print(todo)
    elif option==3:
        print("all items")
        print(todo)
    elif option==4:
        break;