#number swapping
num1=10
num2=20

#logic1
#temp=num1
#num1=num2
#num2=temp
#print(num1)
#values after swapping num1=20 num2=10
#print(f"values after swapping num1={num1} num2={num2}")

#logic2 without temp var   only support in python
num1=num1+num2
num2=num1-num2
num1=num1-num2
print(f"values after swapping num1={num1} num2={num2}")


