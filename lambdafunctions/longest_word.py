text="hi is am hello good goodmorning ziyad"
# find longest word using their length
# words=text.split(" ")
# longest_word=max(words,key=lambda w:len(w))
# print(longest_word)



#sorted in descending order
words=text.split(" ")
srt_words=sorted(words,key=lambda w:len(w),reverse=True)
print(srt_words)