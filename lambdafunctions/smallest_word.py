text="hello good goodmorning"
# find smallest word using their length
words=text.split(" ")
smallest_word=min(words,key=lambda w:len(w))
print(smallest_word)