import sys
input = sys.stdin.readline

length = int(input());

stack = [];
for _ in range(length):
    command = input().split();
    
    if command[0] == "push":
        x = int(command[1]);
        stack.append(x);
        
    elif command[0] == "pop":
        if len(stack) == 0:
            print(-1);
        else:
            print(stack.pop());
    elif command[0] == "size":
        print(len(stack));
    elif command[0] == "empty":
        if len(stack) == 0:
            print(1);
        else:
            print(0);
    elif command[0] == "top":
        if len(stack) == 0:
            print(-1);
        else:
            print(stack[-1]);