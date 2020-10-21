import sys
sys.stdin=open("input.txt")
def in_order(node,trie):
    res,left,right='',node*2,node*2+1
    if node>n: return res
    res+=in_order(left,trie)+trie[node]+in_order(right,trie)
    return res
for tc in range(1,11):
    n=int(input())
    trie=[0]*(n+1)
    for _ in range(n):
        tmp=input().split()
        trie[int(tmp[0])]=tmp[1]
    result=in_order(1,trie)
    print('#{} {}'.format(tc,result))