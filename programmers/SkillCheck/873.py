def solution(n):
    count = 1
    for i in range(1,n//2+1):
        temp = 0
        for j in range(i, n//2+2):
            temp += j
            if temp == n :
                count += 1
                break
            elif temp > n:
                break
                
    return count