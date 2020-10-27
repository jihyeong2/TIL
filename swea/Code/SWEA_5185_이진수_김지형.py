def tobin(x):
    res,num='',int(x,16)
    while num>0:
        res=str(num%2)+res
        num//=2
    while len(res)<4:
        res='0'+res
    return res
T=int(input())
for tc in range(1,T+1):
    n,hex_num=input().split()
    bin_num=''
    for num in hex_num:
        bin_num+=tobin(num)
    print('#{} {}'.format(tc,bin_num))