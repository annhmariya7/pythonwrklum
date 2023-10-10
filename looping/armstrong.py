# num=370
# original=num      #to compare
# sum=0

# while(num !=0):
#     last_digit=num %10
#     cube=last_digit**3       #if 4 digit then use **4,5 digit use **5 eg:3700 **4
#     sum=sum+cube
#     num=num //10           #37   3     0
# if(original ==sum):
#     print("armstrong")
# else:
#     print("not armstrong")




#using 4 digit

# num=1634
# original=num
# sum=0

# while(num !=0):
#     last_digit=num %10
#     cube=last_digit**4       #if 4 digit then use **4,5 digit use **5 eg:3700 **4
#     sum=sum+cube
#     num=num //10           #37   3     0
# if(original ==sum):
#     print("armstrong")
# else:
#     print("not armstrong")


    # len() fn used to check length of an object (object count)    only used for string not in number to count number oject change number to string      that is digit_count=len(str(num))


# original prgrm    using object count
number=int(input("enter number  >"))
original=number
digit_count=len(str(number))
sum=0
while(number !=0):
    last_digit=number %10
    exponent=last_digit**digit_count
    sum=sum+exponent
    number=number //10
print("armstrong number" if sum==original else "not armstrong")

