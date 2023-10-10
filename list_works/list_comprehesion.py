lst=[2,3,4,6,7,8]

#to find squares
# squares=[]
# for n in lst:
#     sq=n**2
#     squares.append(sq)
# print(squares)

# use listcomprehsion to consize the prgrm
# variable=[return loop condition]

#only return without condition prgrms

# squares=[n**2 for n in lst ]
# print(squares)

# cube=[n**3 for n in lst ]
# print(cube)

# add_two=[n+2 for n in lst]
# print(add_two)

#with condition prgrms

# numgt_five=[n for n in lst if n>5]
# print(numgt_five)

# even_num=[n for n in lst if n%2==0]
# print(even_num)

# odd=[n for n in lst if n%2!=0]
# print(odd)

#print all years btw 1800-2025
years=[y for y in range(1800,2026)]
# print(years)


# centuary_yrs=[y for y in years if y%100==0]
# print(centuary_yrs)

non_centuary=[y for y in years if y%100!=0]
print(non_centuary)
