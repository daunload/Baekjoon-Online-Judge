size = int(input())
    
def isValid(text):
    count = 0

    for char in text:
        if char == '(':
            count += 1
        else:
            count -= 1
            
            if count < 0:
                return False
    return count == 0

for _ in range(size):
    text = input()
    
    if isValid(text):
        print("YES")
    else:
        print("NO")