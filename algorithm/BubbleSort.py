def bubbleSort(data):
    for i in range(len(data)-1,0,-1):
        print(data)
        for j in range(i):
            if data[j]>data[j+1]:
                temp=data[j]
                data[j]=data[j+1]
                data[j+1]=temp

data=[9,8,7,6,5,4,3,2,1,0]
bubbleSort(data)