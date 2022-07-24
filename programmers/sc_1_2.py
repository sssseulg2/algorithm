def solution(s):
    letter = list(s)
    letter.sort(reverse=True)

    answer = ''.join(letter)
    return answer

print(solution("Zbcdefg"))