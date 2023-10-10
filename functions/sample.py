# def sample():               #def is function name
#     print("hi dears")


# def sample(name):              #here sample is a variable,name is a parameter
#     print("hi dears its me " +name)
# sample("ann")                 #here ann is argument




# def f_l_name(f_name,l_name):         #f_l_name is a variable  ,f_name & l_name are parameters      #more than one parameters are possible but no. of  parameters must equal to number of arguments
#     print(f_name+" "+l_name)
# f_l_name("ann","mariya")              #ann & mariya are arguments




#sum
# def sum(a,b):
#     s=a+b
#     print(s)
# sum(10,9)




# def arithemetic(a,b):
#     ad=a+b
#     s=a-b
#     m=a*b
#     print(ad,s,m)
# arithemetic(4,2)


#largest among 3 nums using fn

a=int(input("Enter a number"))
b=int(input("Enter second number"))
c=int(input("enter third number"))

def largest(a,b,c):
    if(a>b) and (a>c):
        print("largest num is ",a)
    elif(b>a) and (b>c):
        print("largest num is ",b)
    else:
        print(c)
largest(a,b,c)





