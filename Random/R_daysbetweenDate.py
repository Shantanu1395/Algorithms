#Days between 2 dates

def leapyears(m,y):
    if m<=2:
        y-=1
    return y//4-y//100+y//400    

def monthDays(m):
    s=0
    arr=[31,28,31,30,31,30,31,31,30,31,30,31]
    for i in range(m-1):
        s+=arr[i]
    return s    

d1,m1,y1=list(map(int,(input().split())))
d2,m2,y2=list(map(int,(input().split())))

n1=y1*365+d1
n1+=monthDays(m1)
n1+=leapyears(m1,y1)

n2=y2*365+d2
n2+=monthDays(m2)
n2+=leapyears(m2,y2)

print(n2-n1)
