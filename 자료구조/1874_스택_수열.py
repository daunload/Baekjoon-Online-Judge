import sys
input = sys.stdin.readline

def print_operations(numbers):
    stack = []
    operations = []
    current = 1

    for number in numbers:
        while current <= number:
            stack.append(current)
            operations.append('+')
            current += 1

        if not stack or stack[-1] != number:
            print('NO')
            return

        stack.pop()
        operations.append('-')

    print('\n'.join(operations))


n = int(input())

numbers = []
for _ in range(n):
    numbers.append(int(input()))
print_operations(numbers)
