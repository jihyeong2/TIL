from itertools import permutations
n=int(input())
hit_result=[list(map(int, input().split())) for _ in range(n)]
result=0
perms=list(map(list,permutations(range(1,9),8)))
for player in perms:
    player.insert(3,0)
    p_num = 0
    score = 0
    for i in range(n):
        outCnt = 3
        first,second,third=0,0,0
        while outCnt:
            hit = hit_result[i][player[p_num]]
            if hit == 0:
                outCnt -= 1
            elif hit==1:
                score+=third
                first,second,third=1,first,second
            elif hit==2:
                score+=(second+third)
                first, second, third = 0,1,first
            elif hit==3:
                score+=(first+second+third)
                first, second, third = 0, 0, 1
            elif hit==4:
                score+=(first+second+third+1)
                first, second, third = 0, 0, 0
            p_num = (p_num + 1) % 9
    result = max(result, score)
print(result)