
f_news=open("C:/Users/ANNMARIYA/Desktop/pythonwork/tokenization/news.txt")

f_stop=open("C:/Users/ANNMARIYA/Desktop/pythonwork/tokenization/stopwords.txt")

stop_words={line.rstrip("\n") for line in f_stop}
# print(stop_words)

news_set=set()

for line in f_news:
    words=line.split()
    for w in words:
        news_set.add(w)

print(news_set.difference(stop_words))