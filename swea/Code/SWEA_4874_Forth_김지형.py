import sys
sys.stdin=open("input.txt","r")
def cal(a,b,op):
    if op=='*': return a*b
    elif op=='+': return a+b
    elif op=='-': return a-b
    else: return a//b
T=int(input())
for tc in range(1,T+1):
    expr=list(input().split())
    s=list()
    for x in expr:
        if x=='*' or x=='+' or x=='-' or x=='/':
            if len(s)<2:
                result='error'
                break
            b,a=s.pop(-1),s.pop(-1)
            s.append(cal(a,b,x))
        elif x=='.':
            result= s.pop(-1) if len(s)==1 else 'error'
        else : s.append(int(x))

    print('#{} {}'.format(tc,result))