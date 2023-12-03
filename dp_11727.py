#dp
#11727
# n = 2 일때 전 문제와 다르게 경우의 수가 3
# 길이가 n 일때 n-1 일 때에 2*1 추가된 것, n-2 일 때 2*2 혹은 1*2 2개 추가되는 것으로 볼 수 있다.
num = int(input())
dplist= [0]*(num+1)

for i in range(1,num+1):
    if i == 1:
        dplist[1] = 1
    elif i == 2:
        dplist[2] = 3
    else:
        dplist[i] = dplist[i-1]+dplist[i-2]*2


print(dplist[num]%10007)