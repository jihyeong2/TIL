t = int(input())
for tc in range(1, t+1):
    k,n,m=map(int, input().split())
    add = list(map(int, input().split()))
    # 1. 내 현재 위치에서 최대한 갈수있는 거리안에 충전소가 없으면 그냥 끝
    # 2. 내가 갈수있는 범위 내에 충전소가 있으면 그중 가장 먼거리에 있는 충전소로 이동
    # 3. 최종적으로 n에 도착하면 충전횟수를 출력
    place=0
    result=0
    while True :
        cnt=0
        for i in range(place+k+1)[::-1]:
            if i in add: # 충전소가 거리범위내에 있으면 거기로 이동하라는 조건
                place=i
                break
            cnt+=1
        if cnt>=k: #거리 범위내에 충전소가 없으면 탈출하라는 조건
            result=0
            break
        else: # 거리범위내에 충전소가 있어서 충전소로 이동을 했으면 충전횟수를 늘리는 조건
            result+=1
        if place+k>=n: #종료지점 도착여부 확인하는 조건
            break
    print(f'#{tc} {result}')