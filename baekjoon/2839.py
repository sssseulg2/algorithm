def solution(N):
    answer = -1
    max_five = N//5
    n = N%5
    while True:
        if n % 3 == 0:
            answer = max_five + n//3
            break
        else:
            if max_five > 0:
                max_five -= 1
                n += 5
            else: 
                break

    return answer


print(solution(int(input())))


