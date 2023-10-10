text="fast"          #afst
out="fats"           #afst

wrd_srt=sorted(text)           
print(wrd_srt)

word_srt=sorted(out)           
print(word_srt)

if wrd_srt==word_srt:
    print("it is anagram")
else:
    print("not an anagram")