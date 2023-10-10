tummy_size=int(input("enter tummy size=>"))
buttock_size=int(input("enter buttock size=>"))
gender=input("enter gender male or female=>")
measurement=tummy_size/buttock_size

val=round(measurement,2)              #round fn is used to reduce many numders after decimal point eg:0.98712323=>0.98  if we give round(measurement,2)
print(val)

if gender=="female":
    if(val<0.80):
        print("health risk is low body shape is pear")
    elif(val<0.85):
        print("health risk is moderate body shape is avocado")

    else:
        print("health risk is high body shape is apple")


elif gender=="male":
    if(val<0.95):
        print("health risk is low body shape is pear")
    elif(val<1.0):
        print("health risk is moderate body shape is avocado")

    else:
        print("health risk is high body shape is apple")

else:
    print("please enter a invalid gender ")




