import sys
N = int(input())
stack = []
commands = []
for n in range(N):
    command = sys.stdin.readline()
    """commands.append(sys.stdin.readline())
for command in commands:"""
    if command[:4] == "push":
        stack.append(int(command[5:]))
    elif command[:3] == "pop":
        try: 
            print(stack.pop())
        except:
            print(-1)
    elif command[:4]=="size":
        print(len(stack))
    elif command[:3] == "top" :
        try: 
            print(stack[-1])
        except:
            print(-1)
    else:
        if len(stack) == 0: print(1)
        else: print(0)

        
    