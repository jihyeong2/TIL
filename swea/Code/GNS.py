import sys
sys.stdin=open("input.txt","r")
dic={
    'ZRO':0,'0':'ZRO',
    'ONE':1,'1':'ONE',
    'TWO':2,'2':'TWO',
    'THR':3,'3':'THR',
    'FOR':4,'4':'FOR',
    'FIV':5,'5':'FIV',
    'SIX':6,'6':'SIX',
    'SVN':7,'7':'SVN',
    'EGT':8,'8':'EGT',
    'NIN':9,'9':'NIN'
}
T=int(input())
for _ in range(T):
    tc,n=input().split()
    arr=input().split()
    result=[]
    # print(dic[arr[0]])
    for i in range(int(n)):
        result.append(dic[arr[i]])
    result.sort()
    for i in range(int(n)):
        result[i]=dic[chr(result[i]+48)]
    print(tc)
    for num in result:
        print(num,end=' ')