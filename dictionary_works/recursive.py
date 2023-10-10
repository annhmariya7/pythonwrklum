text="ABCDA"
#print first recursive character means repeated character


wc={}
for ch in text:          #ch=A
    # print(ch)
    if ch in wc:
        print("first recursice character is",ch)
        break
    else:
        wc[ch]=1
