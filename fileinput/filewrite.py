f=open("C:/Users/ANNMARIYA/Desktop/pythonwork/fileinput/write.txt","w")
f.write("writting")     #before this code no write.txt file exists in fileinput folder    after code run write.txt with a message writting new file creates



f=open("C:/Users/ANNMARIYA/Desktop/pythonwork/fileinput/write.txt","w")
f.write("hey guyz")    #using "w" then hey guyz will overwrite on writting in write.txt file in fileinput folder



# to print a list in write.txt file in fileinput folder
lst=["tea","coffee","sugar"]
f=open("C:/Users/ANNMARIYA/Desktop/pythonwork/fileinput/write.txt","w")

for ob in lst:
    f.write(ob+"\n")    #\n used to print one text in a line

  
    