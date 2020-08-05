for tc in range(1,11):
    n=int(input())
    result=0
    buildings=list(map(int,input().split()))
    for i in range(2,n-2):
        max_height=-1
        center = buildings[i]
        for j in range(1,3):
            right=buildings[i+j]
            left=buildings[i-j]
            if left>=center or right>=center:
                max_height=-1
                break
            if max_height<left :
                max_height=left
            if max_height<right:
                max_height=right
        if max_height==-1:
            continue
        result+=center-max_height
    print(f'#{tc} {result}')