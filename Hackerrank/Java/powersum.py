def compute(num,p,index):
    if(pow(index,p)<num):
        return compute(num,p,index+1)+compute(num-pow(index,p),p,index+1)
    if pow(index,p)==num:
        return 1
    else:
        return 0

num=int(input())
p=int(input())
print(compute(num,p,1))
