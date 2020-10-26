import sys
sys.stdin=open("input.txt","r")
code={
    '0001101':0,
    '0011001':1,
    '0010011':2,
    '0111101':3,
    '0100011':4,
    '0110001':5,
    '0101111':6,
    '0111011':7,
    '0110111':8,
    '0001011':9,
}
T=int(input())
def isPossible(password):
    res=0
    for i in range(0,8,2):
        res+=password[i]*3
    for i in range(1,8,2):
        res+=password[i]
    if res%10 == 0 : return True
    return False
for tc in range(1,T+1):
    n,m=map(int,input().split())
    arrs=[input() for _ in range(n)]
    for arr in arrs:
        idx=arr[::-1].find('1')
        if idx==-1: continue
        p_code=arr[m-idx-56:m-idx]
        break
    password=[]
    for i in range(0,56,7):
        tmp=p_code[i:i+7]
        password.append(code[''.join(tmp)])
    result=0
    if isPossible(password):
        result=sum(password)
    print('#{} {}'.format(tc,result))