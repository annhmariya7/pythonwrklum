#check given year is leap yr or not

year=int(input("enter a year  "))
#case1:if the year is centuary yr (last 2 numbers 00 eg:2200 ) check year%100==0
#case2:if the year is not centuary yr (normal yr ) check year%100!=0


if(year % 100==0 and year % 400==0):
    print("it is a leap year")
elif(year % 100!=0 and year % 4==0):
    print("it is a leap year")
else:
    print("it is not a leap year")
