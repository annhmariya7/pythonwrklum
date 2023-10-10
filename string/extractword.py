text="i love liam and anjali"

vowels="a","e","i","o","u"
words=text.split(" ")

for w in words:     #w=eight  w[0]=e
    if w.casefold().startswith(vowels):
        print(w)
#if w[0].casefold() in vowels:
#print(w)