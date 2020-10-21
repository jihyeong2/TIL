import sys
sys.stdin=open("input.txt","r")
def cal(node,result):
    res,node_val=0,trie[node][1]
    if node_val=='+':
        res=cal(int(trie[node][2]),trie)+cal(int(trie[node][3]),trie)
    elif node_val=='-':
        res=cal(int(trie[node][2]),trie)-cal(int(trie[node][3]),trie)
    elif node_val=='*':
        res=cal(int(trie[node][2]),trie)*cal(int(trie[node][3]),trie)
    elif node_val=='/':
        res=cal(int(trie[node][2]),trie)//cal(int(trie[node][3]),trie)
    else:
        res=int(node_val)
    return res

for tc in range(1,11):
    n=int(input())
    trie=[[]]
    for _ in range(n):
        trie.append(input().split())
    # print(trie)
    result=cal(1,trie)
    print('#{} {}'.format(tc,result))
