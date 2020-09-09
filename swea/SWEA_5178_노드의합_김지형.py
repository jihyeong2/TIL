import sys
sys.stdin=open("input.txt","r")
def set_other(n,node,trie):
    sum,left,right=0,node*2,node*2+1
    if left>n:
        return trie[node]
    sum+=set_other(n,left,trie)
    if right<=n:    sum+=set_other(n,right,trie)
    trie[node]=sum
    return sum
T=int(input())
for tc in range(1,T+1):
    n,m,l=map(int, input().split())
    trie = [0] * (n + 1)
    for _ in range(m):
        idx,val=map(int, input().split())
        trie[idx]=val
    set_other(n,1,trie)
    print('#{} {}'.format(tc,trie[l]))