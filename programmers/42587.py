def solution(priorities, location):
    answer = 1
    while True:
        J = priorities.pop(0)
        if any(J < priority for priority in priorities):
            priorities.append(J)
        else:
            if location == 0:
                return answer
            answer += 1
        
        if location == 0: 
            location = len(priorities)-1
        else: location -= 1
            

print(solution([2,1,3,2],2))
# print(solution([1,1,9,1,1,1],0))