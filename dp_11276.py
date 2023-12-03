#dp
#11726
num = int(input())
dplist = [0]*(num+1) # 메모이제이션

def dp(n):
    if n == 1: return 1
    elif n==2: return 2
    else:
        return dplist[n-1]+dplist[n-2]
    
for i in range(1,num+1): # 이전 값을 다시 계산하지 않고 리스트에서 가져옴
    dplist[i] = dp(i)

print(dplist[num]%10007)