import sys
sys.stdin=open("input.txt","r")
def traversal(node,trie):
    res=1
    for next in trie[node]:
        res+=traversal(next,trie)
    return res
T=int(input())
for tc in range(1,T+1):
    e,n=map(int, input().split())
    node=list(map(int, input().split()))
    trie=[[] for _ in range(e+2)]
    for i in range(0,len(node),2):
        trie[node[i]].append(node[i+1])
    result=traversal(n,trie)
    print('#{} {}'.format(tc,result))