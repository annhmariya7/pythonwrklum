foods=[
    {"id":1,"name":"ghee-roast","price":70,"category":"veg"},
    {"id":2,"name":"chicken-roast","price":170,"category":"non-veg"},
    {"id":3,"name":"cb","price":170,"category":"non-veg"},
    {"id":4,"name":"bb","price":190,"category":"non-veg"},
    {"id":5,"name":"fried-rice","price":140,"category":"veg"},
    {"id":6,"name":"chicken-friedrice","price":170,"category":"non-veg"},
    {"id":7,"name":"nan","price":70,"category":"veg"},
    {"id":8,"name":"alfham","price":370,"category":"non-veg"},
     
]


# print total number of items
# print(len(foods),"items")


# print name whose category = veg

#using list comprehesion
# veg_items=[f.get("name") for f in foods if f.get("category")=="veg"]
# print(veg_items)


# for f in foods:
#     if f.get("category")=="veg":
#         print(f.get("name"))




# food names available under rs 100
#using list comprehesion
# price_filter=[f.get("name") for f in foods if f.get("price")<=100]
# print(price_filter)


# for f in foods:
#     if f.get("price")<=100:
#         print(f.get("name"))


# costly item
# costly_food=max(foods,key=lambda i:i.get("price"))
# print(costly_food)


# costly non-veg food
# non_veg=[f for f in foods if f.get("category")=="non-veg"]
# costly_non_veg=max(non_veg,key=lambda f:f.get("price"))
# print(costly_non_veg)

#print all categories
categories={f.get("category") for f in foods }       #use set{} to avoid duplications (only one veg &nonveg)
print(categories)






