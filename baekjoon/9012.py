import sys
input = sys.stdin.readline

T = int(input())

answer = ['YES'] * T

for i in range(T):
    stack = []
    ps = list(input())
    for j in ps:
        if j == '(':
            stack.append(1)
        elif j == ')':
            if len(stack) == 0:
                answer[i] = 'NO'
            elif stack.pop() != 1:
                answer[i] = 'NO'
        elif stack:
            answer[i] = 'NO'
    
for i in answer:
    print(i)