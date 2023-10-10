# prev=0
# current=1
# start=1

# print(prev)
# print(current)

# while(start<=8):
#     sum=prev+current
#     print(sum)
#     prev=current
#     current=sum
#     # (prev,current)=(current,sum)
#     start+=1




   # num=24    

num=int(input("enter number ")) 
prev=0
current=1
is_fibo=False
fib_num=0        #sum=0

while(fib_num<=num):
    fib_num=prev+current
    prev=current
    current=fib_num
    if fib_num==num:
        is_fibo=True
        break
print(is_fibo)