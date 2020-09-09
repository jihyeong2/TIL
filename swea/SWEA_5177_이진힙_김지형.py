import sys
sys.stdin=open("input.txt","r")
def push(num,trie):
    trie.append(num)
    idx=len(trie)-1
    while True:
        p,c=idx//2,idx
        if p<=0 or trie[p]<trie[c]: break
        trie[p],trie[c]=trie[c],trie[p]
        idx//=2
T=int(input())
for tc in range(1,T+1):
    n=int(input())
    nums=list(map(int, input().split()))
    trie=[-1]
    for num in nums:
        push(num,trie)
    result,idx=0,len(trie)-1
    while True:
        idx//=2
        if idx<=0: break
        result+=trie[idx]
    print('#{} {}'.format(tc,result))