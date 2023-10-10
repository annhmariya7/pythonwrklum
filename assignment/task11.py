num=int(input("how many do you want to invite  "))
invite=[]
if num<10:
    for i in range(0,num):
        name=input("enter the name:")
        invite.append(name)
    for i in invite:
        print(f"{i} has been invited...")
    else:
        print("too many people..")