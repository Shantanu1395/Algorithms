#revise
def permuteUtil(s,answer):
    if len(s) == 0:
        print(answer)
    else:
        for i in range(len(s)):

            #Choose
            c=s[i]
            answer += c
            templist = list(s)
            templist.remove(s[i])
            s = "".join(templist)

            #Explore
            permuteUtil(s,answer)

            #Unchoose
            templist = list(s)
            templist.insert(i,c)
            s = "".join(templist)
            answer = answer[:-1]

def permute(s):
    permuteUtil(s,"")

if __name__ == '__main__':
    s = input()
    permute(s)