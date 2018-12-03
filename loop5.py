def seeprimes(num):
    newlist=[]
    for i in range(2,num+1):
        prime=True
        for k in range(2,i):
            if i %k==0:
                prime= False
        if prime==True:
            newlist.append(i)
    print(newlist)

seeprimes(100)