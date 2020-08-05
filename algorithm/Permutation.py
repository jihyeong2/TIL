def permutation(z,data,result,check):
    if z>=len(data):
        print(result)
    else:
        for i in range(len(data)):
            if check[data[i]]!=0:
                continue
            check[data[i]]=1
            result[z]=data[i]
            permutation(z+1,data,result,check)
            check[data[i]]=0
check=[0]*100
data=[1,2,3,4,5,6]
result=[0]*6
permutation(0,data,result,check)