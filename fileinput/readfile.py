#create 3 referrences to read nums from num.txt & print odd & even nums from num.txt
f_read=open("C:/Users/ANNMARIYA/Desktop/pythonwork/fileinput/num.txt")   #no need of read mode bcz automatically read mode is enabled
odd_write=open("C:/Users/ANNMARIYA/Desktop/pythonwork/fileinput/odd.txt","w")   #specify the path that is odd at the end of path with write mode
even_write=open("C:/Users/ANNMARIYA/Desktop/pythonwork/fileinput/even.txt","w")

for line in f_read:
    num=int(line.rstrip("\n"))
    if num%2==0:
        even_write.write(str(num)+"\n")
    else:
        odd_write.write(str(num)+"\n")



#1800-2025 read to year.txt file
year_write=open("C:/Users/ANNMARIYA/Desktop/pythonwork/fileinput/year.txt")
[year_write.write(str(y)+"\n") for f in range(1800,2024)]