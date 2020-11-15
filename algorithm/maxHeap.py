class MaxHeap():
    def __init__(self):
        self.h=[]

    def push(self,data):
        self.h.append(data)
        idx=len(self.h)-1
        while idx>=0:
            p_idx=(idx-1)//2
            if p_idx>=0 and self.h[idx]>self.h[p_idx]:
                self.h[idx],self.h[p_idx]=self.h[p_idx],self.h[idx]
                idx=p_idx
            else:
                break

    def pop(self):
        self.h[0],self.h[-1]=self.h[-1],self.h[0]
        max_res=self.h.pop(-1)
        idx=0
        while idx<len(self.h):
            l,r=(idx*2)+1,(idx*2)+2
            max_idx=idx
            if l<len(self.h) and self.h[max_idx]<self.h[l]:
                max_idx=l
            if r<len(self.h) and self.h[max_idx]<self.h[r]:
                max_idx=r
            if idx==max_idx:
                break
            self.h[idx],self.h[max_idx]=self.h[max_idx],self.h[idx]
            idx=max_idx
        return max_res

h=MaxHeap()
h.push(1)
h.push(3)
h.push(11)
h.push(6)
h.push(5)
h.push(2)
print(h.pop())
print(h.pop())
print(h.pop())
print(h.pop())
print(h.pop())
print(h.pop())