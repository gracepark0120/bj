"""
bfs 로 풀이
queue에 달팽이의 다음 경로를 넣고 queue가 비어지면 끝

- cx cy 는 k 가 그대로 일때(방향 바꾸지 않을 때)
- ccx ccy 는 방향을 바꿀 때

경우의 수는 다음과 같다.
1. 달팽이가 경로를 벗어남
 1.1 방향을 바꾸었을 때는 경로를 벗어나지 않음 -> 바꾼 경로로 큐 추가
 1.2 방향을 바꾸면 이미 들린 장소 -> 끝
2. 달팽이가 경로를 벗어나지 않음 -> 큐 추가
3. 달팽이가 이미 들린 장소로 감
 3.1 방향을 바꾸었을 때는 들리지 않은 장소 -> 바꾼 경로로 큐 추가
 3.2 방향을 바꾸어도 이미 들린 장소 -> 끝

"""

from collections import deque
m,n = map(int, input().split())
dx = [0,1,0,-1]
dy = [1,0,-1,0]
queue = deque([(1,1,0)]) # x,y,cnt
#visited
visited = []
for i in range(m+1):
    visited.append([0]*(n+1))

while queue:
    #print(queue)
    x,y,k = queue.popleft() 
    visited[x][y] = 1 # 다녀감
    
    cx = x + dx[k%4]
    cy = y + dy[k%4]
    
    ck = k+1
    ccx = x + dx[ck%4] # 올바른 방향으로 이동
    ccy = y + dy[ck%4]
    
    if cx <= 0 or cx>m or cy<=0 or cy>n: # 표를 빠져나감
        if visited[ccx][ccy] == 1:
            # 끝
            print(k)
            break
        else: 
            queue.append((ccx,ccy,ck))
 
            
    elif visited[cx][cy]==1:
        if visited[ccx][ccy]!=1:
            queue.append((ccx,ccy,ck))
        else:
            print(k)
            break
    else:
        queue.append((cx,cy,k))
    
    