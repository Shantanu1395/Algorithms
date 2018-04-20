#Remove unbalanced paranthesis

class Stack():
    def __init__(self):
        self.stack=[]
        self.size=0

    def push(self,data):
        self.stack.append(data)
        self.size+=1
        
    def pop(self):
        temp=self.stack[self.size-1]
        del self.stack[self.size-1]
        self.size-=1

    def getsize(self):
        return self.size

    def printStack(self):
        print(self.stack[::-1])
        
def process(s):
    asciistr='qwertyuioplkjhgfdsazxcvbnm'
    stack=Stack()
    outString=""
    for i in range(len(s)):
        if i-1>0 and i<len(s)-1:
            if (s[i]=='+' or s[i]=='-' or s[i]=='*' or s[i]=='/' or s[i]=='%'):
                if (s[i-1] in asciistr and s[i+1] not in asciistr) or (s[i-1] not in asciistr and s[i+1] in asciistr):
                    return False
                
        if s[i]=='(':
            stack.push(i)
        if s[i]==')':
            stack.pop()
                
    if stack.getsize()==0:
        return True
    return False

inString="(a+b)(a*b)"
outString=process(inString)
print("Valid" if outString else "Invalid")

inString="(ab)(ab+)"
outString=process(inString)
print("Valid" if outString else "Invalid")

inString="((a+b)"
outString=process(inString)
print("Valid" if outString else "Invalid")

