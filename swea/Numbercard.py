T=int(input())
for tc in range(1,T+1):
    n=int(input())
    num=input()
    count=[0]*101
    for i in num:
        count[int(i)]+=1
    max_cnt=-1
    max_num=-1
    for i in range(n):
        if max_cnt<count[int(num[i])]:
            max_cnt=count[int(num[i])]
            max_num=int(num[i])
        elif max_cnt==count[int(num[i])] and max_num<int(num[i]):
            max_num=int(num[i])
    print(f'#{tc} {max_num} {max_cnt}')