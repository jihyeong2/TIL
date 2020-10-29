import sys
sys.stdin=open("input.txt","r")
def change(z,nums):
    if z==n:
        global result
        for num in nums:
            result=max(result,int(num))
        return
    n_nums=[]
    for num in nums:
        for i in range(length-1):
            for j in range(i+1,length):
                s,e=(i,j) if i<j else (j,i)
                n_num=num[:s]+num[e]+num[s+1:e]+num[s]+num[e+1:]
                if n_num not in n_nums:
                    n_nums.append(n_num)
    change(z+1,n_nums)
T=int(input())
for tc in range(1,T+1):
    number,n=input().split()
    n=int(n)
    length=len(number)
    result=0
    change(0,[number])
    print('#{} {}'.format(tc,result))