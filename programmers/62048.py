# 최단 메모리 10.1MB 최장 메모리 10.3MB
# 최단 시간 0.00ms, 최장 시간 0.01ms
from math import gcd

def solution(w,h):
    gcdNumber = gcd(w,h)
    if gcdNumber == 1:
        return w*h - (w+h-1)
    else :
        return w*h - (w/gcdNumber + h/gcdNumber - 1)*gcdNumber
    
# print(solution(8,12))
