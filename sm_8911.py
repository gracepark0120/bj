"""
거북이 좌표, 방향 을 넣은 큐?

q. 거북이가 지나간 영역을 모두 포함할 수 있는 가장 작은 직사각형의 넓이.
ㅎㅎg
처음 시작: (0,0,0) x,y,k

k는 dx,dy의 인덱스 넘버. 시계방향
k=0 : (x+1, y) : 전진
k=1 : (x, y-1) : 왼쪽으로 한칸
k=2 : (x-1, y) : 후진
k=3 : (x, y+1) : 오른쪽으로 한칸

주의) 인덱스 기준 x는 세로선, y는 가로선 임.

주어진 문제에서 L, R는 방향만 바꿈.
L 이나 R 이면 k만 늘고 실제로 반영 안됨.
"""
import sys
from collections import deque
tlist = []
T = int(input())
for t in range(T):
    tlist.append(sys.stdin.readline())
    
dx=[1, 0, -1, 0]
dy=[0, -1, 0, 1]    
answer = []
for t in tlist:
    visited = [(0,0)]
    turtle = deque([(0,0,0)]) # x, y, k 
    
    for i in t:
        x,y,k = turtle.popleft()
        if i == 'F':
            x = x+dx[k]
            y = y+dy[k]
                    
        elif i == 'B':
            nk = (k+2)%4 # 반대 방향은 인덱스 2 차이남, 후진이지 방향을 바꾸는 건 아니므로 새로운 변수로.
            x = x+dx[nk]
            y = y+dy[nk]
                        
        elif i == 'L':
            k = (k+1)%4
            
        else:
            k = (k-1)%4
        #print(visited)
        turtle.append((x,y,k))
        visited.append((x,y))
    
    maxx = max(visited, key=lambda t:t[0])[0]
    maxy = max(visited, key=lambda t:t[1])[1]
    minx = min(visited, key=lambda t:t[0])[0]
    miny = min(visited, key=lambda t:t[1])[1]
    try : 
        ans = abs(maxx-minx)*abs(maxy-miny)
    except:
        ans = 0
        
    answer.append(ans)

for ans in answer:
    print(ans)
    