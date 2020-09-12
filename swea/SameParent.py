import sys
sys.stdin=open("input.txt","r")
class Node():
    def __init__(self):
        self.parent=-1
        self.child=[]
def findParent(s,trie,p):
    node=s
    while trie[node].parent!=-1:
        p.append(trie[node].parent)
        node=trie[node].parent
def subtree(node,trie):
    res=0
    for c in trie[node].child:
        res+=subtree(c,trie)
    res+=len(trie[node].child)
    return res
T=int(input())
for tc in range(1,T+1):
    v,e,n1,n2=map(int, input().split())
    nodes=list(map(int, input().split()))
    trie=[ Node() for _ in range(v+1)]
    for i in range(0,len(nodes),2):
        trie[nodes[i]].child.append(nodes[i+1])
        trie[nodes[i+1]].parent=nodes[i]
    p1,p2,sp=[],[],0
    findParent(n1,trie,p1)
    findParent(n2,trie,p2)
    for pp1 in p1:
        for pp2 in p2:
            if pp1==pp2:
                sp=pp1
                break
        if sp!=0: break
    result=1+subtree(sp,trie)
    print('#{} {} {}'.format(tc,sp,result))