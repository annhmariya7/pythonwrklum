arr=[#0 1 2
    [2,0,1],    #0
    [1,1,0],    #1
    [2,0,3]     #2
]


# position value matrix
#row+column-element
#0+0-2=2
#0+1-0=1
#0+2-1=1

for row in range(0,3):
    for col in range(0,3):
        value=row+col-arr[row][col]
        print(value,end="\t")
    print()