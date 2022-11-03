def solution(n, works):
    if sum(works) < n:
        return 0
    works.sort()
    index = len(works)-1

    while n != 0:
        n-=1
        if works[index] > 0:
            works[index] -= 1
        if index > 0 and works[index] < works[index-1]:
            index -= 1
        else: 
            index = len(works)-1
        


    return sum(list(map(lambda x: x**2, works)))


print(solution(4, [4,3,3]))
print(solution(1, [2,1,2]))