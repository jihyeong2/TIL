import sys
sys.stdin=open("input.txt","r")
for _ in range(10):
    n=int(input())
    arr=[list(map(int,input().split())) for _ in range(100)]
    sum1,sum2,sum3,sum4 = 0,0,0,0
    for i in range(100):
        sum1=max(sum1,sum(arr[i]))
        temp=0
        for j in range(100):
            temp+=arr[j][i]
        sum2=max(sum2,temp)
        sum3+=arr[i][i]
        sum4+=arr[i][99-i]
    print(f'#{n} {max(sum1,sum2,sum3,sum4)}')