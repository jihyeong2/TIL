bytes=input().split()
for i in range(0,len(bytes),7):
    byte=int(''.join(bytes[i:i+7]),2)
    print(byte)