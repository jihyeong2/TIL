class queue():
    def __init__(self):
        self.q=[]
        self.front=-1
        self.rear=-1

    def enqueue(self,data):
        self.q.append(data)
        self.rear+=1

    def dequeue(self):
        if self.front==self.rear:
            return -1
        self.front += 1
        data=self.q[self.front]
        self.q[self.front]=0
        return data

q=queue()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())
print(q.dequeue())
q.enqueue(1)
print(q.dequeue())