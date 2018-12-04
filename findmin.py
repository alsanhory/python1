def findmin(mylist):
    min=mylist[0]
    for i in mylist:
        if i < min:
            min=i
    print(min)
findmin([3,5,6,7,2,-1,10])


