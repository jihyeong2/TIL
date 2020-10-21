import sys
sys.stdin=open("input.txt","r")
T=int(input())
for tc in range(1,T+1):
    str1=input()
    str2=input()
    visit=set()
    result=0
    for s1 in str1:
        if s1 in visit : continue
        cnt = 0
        visit.add(s1)
        for s2 in str2:
            if s1==s2: cnt+=1
        result=max(cnt,result)
    print('#{} {}'.format(tc,result))