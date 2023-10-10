source_code="deceased"
target=str(input("enter the text"))
wc={}

is_kangaroo=True
for ch in source_code:
    if ch in wc:
        wc[ch]+=1
    else:
        wc[ch]=1
# print(wc)
for ch in target:
    if ch in wc and wc.get(ch)>0:
        wc[ch]-=1
    else:
        is_kangaroo=False
        break
print(is_kangaroo)
        
