from functools import reduce

def solution(numbers):

    numbers = [str(number) for number in numbers]
    numbers.sort(key=lambda x: x*3)

    answer = reduce(lambda x, y: y + x, numbers)
    if int(answer) == 0:
        return '0'
    return answer


solution([0,0,0])