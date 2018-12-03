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

Print nafisa 10 times

Print numbers from 0 to 10

""" 
Write a function to print event numbers from given range
Write a function to calculate sum of given range of numbers
Write a function to remove duplications from  a list
Write a function to find factorial of given number
Write a function to all prime nubmers of given list of numbers


 """
