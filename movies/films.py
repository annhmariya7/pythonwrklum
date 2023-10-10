from json import load


path="C:/Users/ANNMARIYA/Desktop/pythonwork/movies/mdb (1).json"
with open(path) as f:
    movies=load(f)


#print total number of movies
# print(len(movies))


# movie_names=[m.get("title") for m in movies ]
# print(movie_names)

#print movie title released in 2005
# year_filter=[m.get("title") for m in movies if m.get("year")=="2005" ]
# print(year_filter)


#print movie titles whose genre ="comedy"
# comedy_movie=[m.get("title") for m in movies if "Comedy" in m.get("genres")]      #if comedy in use bcz genres is a list
# print(comedy_movie)

#lengthy movie title
# lengthy_movie=max(movies,key=lambda m:int(m.get("runtime")))
# print(lengthy_movie)



#print all genres
# genres={g for m in movies for g in m.get("genres")}     #here use set to avoid duplication means if morethan one comedy movie in generes we only need one comedy
# print(genres)


#comedy movies released in 2015
# comedy_movies=[m.get("title") for m in movies if "Comedy" in m.get("genres") and m.get("year")=="2015"]
# print(comedy_movies)


#year of maximum movies released
wc={}    #empty dictionary
for m in movies:
    year=m.get("year")
    if year in wc:
        wc[year]+=1
    else:
        wc[year]=1
print(max(wc,key=lambda k:wc.get(k)))
