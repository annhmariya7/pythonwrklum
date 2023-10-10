
#123
# o/p=36 (1**3  +  2**3   +  3**3)

num=123
sum=0

while(num !=0):
    last_digit=num %10
    cube=last_digit**3       #if 4 digit then use **4,5 digit use **5 eg:3700 **4
    sum=sum+cube
    num=num //10           #37   3     0
print(sum)