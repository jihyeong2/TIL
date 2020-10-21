import sys
sys.stdin=open("input.txt","r")
def solution(s):
    answer = len(s)
    for length in range(1,len(s)):
        start,cnt,before,temp=length,1,s[0:length],''
        while True:
            if start>=len(s): break
            next=s[start:start+length]
            if before==next:
                cnt+=1
            else:
                if cnt==1:
                    temp+=''.join(before)
                else:
                    temp += str(cnt) + ''.join(before)
                    cnt=1
                before=next[:]
            start+=length
        if cnt == 1:
            temp += ''.join(before)
        else:
            temp += str(cnt)+''.join(before)
        answer=min(answer,len(temp))
        # print(temp,length,len(s))
    return answer
for _ in range(5):
    s=input()
    print(solution(s))