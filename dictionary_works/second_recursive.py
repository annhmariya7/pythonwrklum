text="ABBCDAE"
#print second recursive character
#here first recursive character is B & second recursive character is A
wc={}            #empty dictionary
dup_list=[]       #empty list to add repeated character & can print the second recursive character in list using index position [1]
for ch in text:       #ch=A
    if ch in wc:
        dup_list.append(ch)
    else:
        wc[ch]=1
print(dup_list[1])


