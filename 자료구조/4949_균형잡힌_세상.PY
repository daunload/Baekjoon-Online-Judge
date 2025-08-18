import sys

input = sys.stdin.readline

def is_valid(text):
    stack = []

    for char in text:
        if char == '[':
            stack.append(char)
        
        elif char == ']':
            if not stack or stack[-1] != '[':
                return False
            else:
                stack.pop()
        
        elif char == '(':
            stack.append(char)
        elif char == ')':
            if not stack or stack[-1] != '(':
                return False
            else:
                stack.pop()
    return len(stack) == 0

result = []
while True:
    inputText = input()
    text = inputText.replace("\n", "")

    if text == '.':
        break

    result.append('yes' if is_valid(text) else 'no')

for value in result:
    print(value)