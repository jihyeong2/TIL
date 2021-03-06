n=int(input())
stairs=[0]*300
for i in range(n):
  stairs[i]=int(input())

d=[0]*300
d[0]=stairs[0]
d[1]=stairs[0]+stairs[1]
d[2]=max(stairs[2]+stairs[0], stairs[2]+stairs[1])
for i in range(3,n):
  d[i]=max(stairs[i]+d[i-2], stairs[i]+stairs[i-1]+d[i-3])

print(d[n-1])