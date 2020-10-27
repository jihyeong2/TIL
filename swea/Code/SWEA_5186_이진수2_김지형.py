def tobin(d_num,bin_num,idx):
    b_num=float(2**idx)
    if d_num>=b_num:
        return d_num-b_num,bin_num+'1'
    return d_num,bin_num+'0'
T=int(input())
for tc in range(1,T+1):
    num=float(input())
    bin_num,idx='',-1
    while num:
        if idx<-13:
            bin_num='overflow'
            break
        num,bin_num=tobin(num,bin_num,idx)
        idx-=1
    print('#{} {}'.format(tc,bin_num))