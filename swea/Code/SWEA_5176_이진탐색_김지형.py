import sys
sys.stdin=open("input.txt","r")
def traversal(node_idx,num,n,trie):
    res=1
    left,right=node_idx*2,node_idx*2+1
    if left<=n: res+=traversal(left,num,n,trie)
    trie[node_idx]=num+res
    if right<=n: res+=traversal(right,num+res,n,trie)
    return res
T=int(input())
for tc in range(1,T+1):
    n=int(input())
    trie=[0]*(n+1)
    traversal(1,0,n,trie)
    print('#{} {} {}'.format(tc,trie[1],trie[n//2]))