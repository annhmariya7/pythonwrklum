nums=[
    [10,20],
    [30,5],
    [15,45]
]


#to print each number from nested list

for ls in nums:       #ls means 1st list that is [10,20]
    for n in ls:       #n means from ls that is [10,20] take 10 and 20 seperate
        print(n)