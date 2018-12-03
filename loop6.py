def seeprimes(num):
    newlist=[]
    anotherlist=[]
    for i in range(2,num+1):
        
        for k in range(2,i):
            if i %k!=0:
                newlist.append(i)
            else:
                anotherlist.append(i)
        
    print(newlist)

seeprimes(100)