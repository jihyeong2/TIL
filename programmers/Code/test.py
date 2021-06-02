# from collections import deque
#
# def solution(places):
#     def bfs(a, b, board):
#         dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
#         q = deque()
#         q.append((a, b, 0))
#         visit = [[0] * 5 for _ in range(5)]
#         visit[a][b] = 1
#         while q:
#             x, y, dist = q.popleft()
#             for dir in range(4):
#                 nx, ny = x + dx[dir], y + dy[dir]
#                 if 0 <= nx < 5 and 0 <= ny < 5 and not visit[nx][ny]:
#                     if board[nx][ny] == 'P':
#                         return False
#                     elif board[nx][ny] == 'O':
#                         if dist + 1 < 3:
#                             visit[nx][ny] = 1
#                             q.append((nx, ny, dist + 1))
#         return True
#
#     answer = []
#     for board in places:
#         p_list = []
#         for i in range(5):
#             for j in range(5):
#                 if (board[i][j] == 'P'):
#                     p_list.append((i, j))
#         for x, y in p_list:
#             if not bfs(x, y, board):
#                 answer.append(0)
#                 break
#         else:
#             answer.append(1)
#     print(answer)
#     return answer
#
# solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])

from copy import deepcopy
# def solution(n, k, cmd):
#     answer = ''
#     table=[i for i in range(n)]
#     z_list=[]
#     curr_idx,curr_val=k,k
#     for command in cmd:
#         command_list=command.split(' ')
#         if len(command_list)==2:
#             mode,cnt=command_list[0],int(command_list[1])
#             if mode=='U':
#                 # 위로
#                 curr_idx-=cnt
#                 curr_val=table[curr_idx]
#             else:
#                 # 아래로
#                 curr_idx+=cnt
#                 curr_val = table[curr_idx]
#         else:
#             # 삭제 or 되돌리기
#             mode=command_list[0]
#             if mode=='C':
#                 # 삭제
#                 z_list.append(table[:])
#                 table=table[0:curr_idx]+table[curr_idx+1:]
#                 if curr_idx>=len(table):
#                     curr_idx=len(table)-1
#                 curr_val = table[curr_idx]
#             else:
#                 # 되돌리기
#                 table=z_list.pop()
#                 curr_idx=table.index(curr_val)
#         print(command)
#         print(curr_idx)
#         print(table)
#         if len(z_list) : print(z_list[-1])
#         print('--------------------------')
#
#     i,j=0,0
#     while i<n:
#         if i==table[j]:
#             answer+='O'
#             j+=1
#         else:
#             answer+='X'
#         i+=1
#     print(table)
#     print(answer)
#     return answer


# solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"])
# solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"])
import sys

def solution(n, start, end, roads, traps):
    def dfs(curr, end, time, graph, visit, trap):
        if time > answer[0]: return
        if curr == end:
            answer[0] = min(answer[0], time)
        else:
            for next in graph[curr][1].keys():
                if visit[next]: continue
                if graph[curr][1][next][1]==False: continue
                visit[next] = 1
                dfs(next, end, time + graph[curr][1][next][0], graph, visit, trap)
            for next in graph[curr][0].keys():
                for key2 in graph[next][0].keys():
                    graph[next][0][key2][1] = True
                    graph[key2][0][next][1] = False
                for key2 in graph[next][1].keys():
                    graph[next][1][key2][1] = True
                    graph[key2][1][next][1] = False
                dfs(next, end, time + graph[curr][0][next][0], graph, visit, trap)
                for key2 in graph[next][0].keys():
                    graph[next][0][key2][1] = False
                    graph[key2][0][next][1] = True
                for key2 in graph[next][1].keys():
                    graph[next][1][key2][1] = False
                    graph[key2][1][next][1] = True

    answer = [sys.maxsize]
    trap = [0] * (n + 1)
    for t in traps: trap[t] = 1
    graph = [[dict(),dict()] for _ in range(n + 1)]
    visit = [0] * (n + 1)
    for s, e, dist in roads:
        if trap[e]:
            graph[s][0][e] = [dist, True]
            graph[e][0][s] = [dist, False]
        else:
            graph[s][1][e] = [dist, True]
            graph[e][1][s] = [dist, False]
    visit[start] = 1
    print(graph)
    dfs(start, end, 0, graph, visit, trap)
    print(answer[0])
    return answer[0]

# solution(3,1,3,	[[1, 2, 2], [3, 2, 3]],[2])
solution(4,1,4,	[[1, 2, 1], [3, 2, 1], [2, 4, 1]],[2,3])