import sys

input = sys.stdin.readline

N = int(input())

commands = []
for _ in range(N):
    commands.append(input().split())

queue = []
for command in commands:
    if command[0] == 'push':
        queue.append(command[1])
    elif command[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop(0))
    elif command[0] == 'size':
        print(len(queue))
    elif command[0] == 'empty':
        print(1 if len(queue) == 0 else 0)
    elif command[0] == 'front':
        print(queue[0] if len(queue) > 0 else -1)
    elif command[0] == 'back':
        print(queue[-1] if len(queue) > 0 else -1)
