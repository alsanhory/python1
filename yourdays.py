from datetime import datetime
def checkLeap(year):
    if year % 4 ==0 :
        return True
    else:
        return False

def noOfLeaps(formYear, toYear):
    count=0
    for i in range(formYear,toYear+1):
        if checkLeap(i):
            count=count + 1
    return count
def main(dob):
    age= datetime.now().year - dob
    
    leaps= noOfLeaps(dob,datetime.now().year)
    normal= age- leaps
    total = leaps * 366 + normal * 365
    print(total)

main(1989)


