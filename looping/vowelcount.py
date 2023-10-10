text="AnnMariyaJaison"
word=text.casefold()

v_count=0
c_count=0
for ch in word:
    if ch in ["a","e","i","o","u"]:                #in is a membership operator
        v_count+=1
    elif ch not in [" ",".",",","/"]:
        c_count+=0
    else:
        c_count+=1
print("vowels=", v_count)
print("consonants=", c_count)