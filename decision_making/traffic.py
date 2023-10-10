#decision making stmt

#if.....else                   #check only one condition
#syntax
#if(condition):              #condition ans must be boolean value  
    #stmt1
    #stmt2
#else:                         #no condition check in else
    #stmt3
    # stmt4  

#elif                          #check multiple condition   eg:numcheck.py
#syntax
#if(condition):               
    #stmt1
    #stmt2
#elif(condition2):                        # condition check in elif
    #stmt3
    # stmt4  
#elif(condition3):                        # condition check in elif
    #stmt3
    # stmt4  

 


# colour="red"

# if(colour=="red"):                #use double=
#     print("stop")
# else:
#     print("go")


#To take input from user
colour=input("enter the colour red green")
if(colour=="red"):               
    print("stop")
else:
    print("go")
