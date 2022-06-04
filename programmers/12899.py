# 평균 메모리 10.2MB 평균 시간 0.01ms
def solution(n):
    tenerary = []

    while n > 0:
        if n % 3 == 0:
            tenerary.append(4)
            n -= 3
        else:
            tenerary.append(n%3)
        n = n//3

    tenerary.reverse()
    answer = int(''.join(map(str,tenerary)))


    return answer

# print(solution(12))
