#1
user_text=int(input("enter the number   "))
if user_text>10 and user_text<=20:
    print("thank you")
else:
    print("incorrect answer")


#2
user=int(input("enter the number  "))
if user<10:
    print("too low")
elif user<=20:
    print("correct")
else:
    print("too high")


#3
age=int(input("enter your age: "))
if age>=18:
    print("you can vote")
elif age==17:
    print("you can learn to drive")
elif age<=16:
    print("you can go to treat")


#4
number=int(input("enter a number 1 or 2 or 3  "))
if number==1:
    print("thank you")
elif number==2:
    print("well done")
elif number==3:
    print("correct")
else:
    print("error msg")


#5
num=int(input("enter the number  "))
if num%2==0 and num%3==0:
    print(num,"is divisible by both 2 & 3")
else:
    print("not divisible")


#6
num=int(input("enter the number  "))
if num%2==0 and num%3==0:
    print(num,"is divisible by both 2 & 3")
else:
    print("not divisible")


#7
num=int(input("enter the number  "))
i=1
for i in range(1,11):
    print(num*i)


#8
for num in range(10,51):
    if num%2==0:
        print(num)


#9
user=str(input("enter your name  "))
# multi=user*3
# print(multi)

#or
b=1
while(b<=3):
    print(user)
    b=b+1


#10
user_name=str(input("enter your name  "))
num=int(input("enter a number"))
if num<10:
    for i in range(1,num+1):
        print(user_name)
else:
    print("too high")


#11
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


#12
num=int(input("enter a number  "))
while(num<=5):
    num=int(input("enter a number  "))
print("the number you entered was a",num)


# 13
while(True):
    num=int(input("enter a number"))
    if num<10:
        print("too low")
    elif num>20:
        print("too long")
    else:
        print("thank you")
        break


#14
for i in range(10,301,10):
    print(i)

#15
sum=0
for i in range(1,6):
    num=int(input("enter a number:"))
    sum=sum+num
avg=sum/5
print(avg)