n = int(input())

stack = []
answer = []
count = 1
flag = 0

for i in range(n):
    result = int(input())

    while count <= result:
        stack.append(count)
        answer.append('+')
        count += 1

    
    if stack and stack[-1] == result:
        stack.pop()
        answer.append('-')
    else:
        print("NO")
        flag = 1
        break

if flag == 0:
    for i in answer:
        print(i)