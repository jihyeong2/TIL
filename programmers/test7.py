def solution(sales, links):
    def goWork(z, money, sel,result):
        if money>result[0]:return
        if z==len(team):
            if sum(visit)==length:
                result[0]=min(result[0],money)
            return
        for emp in team[z]:
            if visit[emp]:
                goWork(z+1,money,sel,result)
            else:
                sel.append(emp)
                for t in team:
                    if emp in t:
                        for member in t: visit[member]=1
                goWork(z+1,money+sales[emp-1],sel,result)
                for t in team:
                    if emp in t:
                        for member in t: visit[member]=0
                sel.pop(-1)
    answer = 0
    length=len(sales)
    graph = [[] for _ in range(length+1)]
    visit=[0]*(length+1)
    team=[]
    for link in links:
        senior,junior=link[0],link[1]
        for t in team:
            if senior == t[0]:
                t.append(junior)
                break
        else:
            team.append([senior,junior])
        graph[senior].append(junior)
        graph[junior].append(senior)
    result=[2**31]
    goWork(0,0,[],result)
    answer=result[0]
    return answer

print(solution([14, 17, 15, 18, 19, 14, 13, 16, 28, 17],[[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]))