import sys
input = sys.stdin.readline

K = int(input())

stack = []
answer = 0

for i in range(K):
    recent = int(input())
    if recent != 0:
        stack.append(recent)
    else:
        stack.pop()

for i in stack:
    answer += i 

print(answer) 
