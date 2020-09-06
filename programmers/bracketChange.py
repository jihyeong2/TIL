import sys
sys.stdin=open("input.txt","r")
def check(u):
    s=list()
    for i in range(len(u)):
        if u[i]=='(': s.append(u[i])
        else:
            if len(s)==0: return False
            s.pop(-1)
    return True
def solution(p):
    if len(p)==0 or check(p): return p
    answer=''
    u,v,openCnt,closeCnt='','',0,0
    for i in range(len(p)):
        if p[i]=='(': openCnt+=1
        else: closeCnt+=1
        u+=p[i]
        if openCnt==closeCnt:
            v+=p[i+1:]
            break
    if check(u):
        answer+=u+solution(v)
    else:
        answer+='('+solution(v)+')'
        for x in u[1:-1]:
            if x=='(': answer+=')'
            else: answer+='('
    return answer
for _ in range(4):
    p=input()
    print(solution(p))