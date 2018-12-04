def findnumber(mylist,num):
    find=False
    for item in mylist:
        if num == item:
            find=True
            break
    print(find)
findnumber([3,4,5,5,2,2],2)    