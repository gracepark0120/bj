"""
1. 
dfs 재귀로?

"""

import sys
from collections import deque
n,m = list(map(int, input().split()))
r,c,d = list(map(int, input().split()))

graph=[]
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))
    
print(graph)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
queue = deque([(r,c,d)])
clean = 0
while queue:
    print(queue)
    r,c,d = queue.popleft()
    
    if graph[r][c] == 0: # 청소 안됨
        graph[r][c] = 1
        clean += 1

    cnt = 0
    for i in range(4):
        cr = r + dx[(d - i) % 4]
        cc = c + dy[(d - i) % 4]
        d = (d - i) % 4
        if cr < 0 or cr > n or cc <0 or cc >m:
            continue
        if graph[cr][cc] == 0: # 청소되지 않은 빈 칸 존재
            queue.append((cr,cc,d))
            cnt += 1
            break
    if cnt == 0: # 모두 청소됨
        if graph[r-dx[d%4]][c-dy[d%4]] == 1:
            print(clean)
            break
            
        else:
            queue.append((r-dx[d%4], c-dy[d%4], d%4))