#Revise
def printParanthesis(str,open,close,N):
        if open == N and close == N:
            print(str)
        else:
            if open < N:
                printParanthesis(str+"{",open+1,close,N)
            if close < open:
                printParanthesis(str+"}",open,close+1,N)


if __name__ == '__main__':
    n = int(input())
    str=""
    printParanthesis(str,0,0,n)