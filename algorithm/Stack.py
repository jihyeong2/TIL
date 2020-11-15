class Stack():
    def __init__(self):
        self.s=[]

    def push(self,data):
        self.s.append(data)
    def pop(self):
        if len(self.s)==0:
            return -1
        return self.s.pop(-1)
    def top(self):
        if len(self.s)==0:
            return -1
        return self.s[-1]
s=Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.top())
s.pop()
s.push(1)
print(s.top())