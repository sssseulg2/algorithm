# 메모리 30840 시간 820
import sys
input = sys.stdin.readline

n = int(input())

integer = 665
count = 0

while count != n:
    integer += 1
    if '666' in str(integer):
        count += 1

print(integer) 
