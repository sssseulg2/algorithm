def solution(nums):
    ponkemon = dict()
    for i in nums:
        if i in ponkemon:
            ponkemon[i] += 1
        else:
            ponkemon[i] = 1
            
    
    return min(len(nums)/2, len(ponkemon))
    
