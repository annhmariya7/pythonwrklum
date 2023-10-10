# f=open("C:/Users/ANNMARIYA/Desktop/pythonwork/fileinput/data.txt","r")    #in windows path shows error in output so use/ instead of \ in file cpy path
# for line in f:
#     print(line)



#to add data.txt texts to a list
f=open("C:/Users/ANNMARIYA/Desktop/pythonwork/fileinput/data.txt","r")    #in windows path shows error in output so use/ instead of \ in file cpy path
lst=[]  #an empty list
for line in f:
    lst.append(line.rstrip("\n"))   #in list data.txt texts output will be hello/n,hai/n,hello/n,hey    but we dont need /n to remove /n from right side of a text use a list method rstrip
print(lst)



#to print longest word from data.txt
# f=open("C:/Users/ANNMARIYA/Desktop/pythonwork/fileinput/data.txt","r")    
# lst=[]  
# for line in f:
#     lst.append(line.rstrip("\n"))   
# print(lst)
# longest_word=max(lst,key=lambda w:len(w))
# print(longest_word)

#or
# print(max([line.rstrip("/n") for line in f ],key=lambda w:len(w)))