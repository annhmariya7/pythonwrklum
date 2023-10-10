#bmi     #body mass index

height_incm=165
weight_inkg=75

height_inmeter=height_incm/100
#bmi=weight(inkg)/(height^2)(inmeters)       #eq
bmi=weight_inkg//height_inmeter**2
print(bmi)

if(bmi<=19):
    print("underweight")
elif(bmi<=25):
    print("normal")
elif(bmi<=30):
    print("overweight")
else:
    print("obesity")




    #or

if(bmi<19):
    print("underweight")
elif(bmi>=19) and(bmi<25):
    print("normal")
elif(bmi>25) and(bmi<=30):
    print("over weight")
elif(bmi>30):
    print("obesity")







