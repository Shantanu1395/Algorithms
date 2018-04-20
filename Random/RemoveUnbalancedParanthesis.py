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

    def size(self):
        return self.size

    def printStack(self):
        print(self.stack[::-1])
        
def process(s):
    stack=Stack()
    outString=""
    for i in range(len(s)):
        if s[i]=='(':
            stack.push(i)
        if s[i]==')':
            stack.pop()
                
    for i in range(len(s)):
        if i not in stack.stack:
            outString+=s[i]
    return outString

inString="((abc)((de))"
outString=process(inString)
print(outString)

inString="(((ab)"
outString=process(inString)
print(outString)
