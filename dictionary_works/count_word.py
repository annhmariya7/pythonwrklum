text="good morning good evening"

word=text.split(" ")          #split each string with spce in text
wc={}     #an empty dictionary

for w in word:
    if w in wc:
        wc[w]+=1
    else:
        wc[w]=1
print(wc)