class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
    def __str__(self):
        return (self.data,self.next)

class linkedList():
    def __init__(self):
        self.head=None

    def append(self,node):
        if self.head==None:
            self.head=node
        else:
            curr=self.head
            while curr.next!=None:
                curr=curr.next
            curr.next=node

    def getDataIndex(self,data):
        cur=self.head
        idx=0
        while cur:
            if cur.data==data:
                return idx
            cur=cur.next
            idx+=1
        return -1

    def insertNodeAtIndex(self,idx,node):
        curr=self.head
        curr_idx=0
        prev=None
        if idx==0:
            if self.head:
                next_node=self.head
                self.head=node
                self.head.next=next_node
            else:
                self.head=node
        else:
            while curr_idx!=idx:
                if curr:
                    prev=curr
                    curr=curr.next
                else:
                    break
                curr_idx+=1
            if curr_idx==idx:
                prev.next=node
                node.next=curr
            else:
                return -1

    def insertNodeAtData(self,data,node):
        curr=self.head
        while curr:
            if curr.data==data:
                node.next=curr.next
                curr.next=node.next
            else:
                curr=curr.next
        return -1

    def deleteAtIdx(self,idx):
        curr=self.head
        prev=None
        curr_idx=0
        if idx==0:
            self.head=self.head.next
        else:
            while curr:
                if curr_idx==idx:
                    prev.next=curr.next
                    break
                prev=curr
                curr=curr.next
                curr_idx+=1
        if curr_idx!=idx:
            return -1

    def clear(self):
        self.head=None

    def print_list(self):
        curr=self.head
        list_str=''
        while curr:
            list_str+=str(curr.data)
            if curr.next:
                list_str+=' ->'
            curr=curr.next
        print(list_str)

l1=linkedList()
l1.append(Node(1))
l1.append(Node(2))
l1.append(Node(3))
l1.append(Node(5))
l1.print_list()
l1.insertNodeAtIndex(3,Node(4))
l1.print_list()
l1.insertNodeAtIndex(0,Node(0))
l1.print_list()
l1.deleteAtIdx(0)
l1.print_list()
l1.deleteAtIdx(2)
l1.print_list()