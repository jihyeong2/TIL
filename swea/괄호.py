import sys
sys.stdin=open("input.txt","r")
def isPossible(arr):
    dic = {'}': '{', ']': '[', ')': '('}
    s = list()
    for ar in arr:
        if ar == '[' or ar == '{' or ar == '(':
            s.append(ar)
        elif ar==']' or ar=='}' or ar==')':
            if len(s) == 0 or dic[ar] != s[-1]:
                return 0
            s.pop(-1)
        else: continue
    if len(s)!=0 : return 0
    else : return 1
T=int(input())
for tc in range(1,T+1):
    arr=input()
    result=isPossible(arr)
    print('#{} {}'.format(tc,result))