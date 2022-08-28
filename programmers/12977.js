function solution(nums) {
    const len = nums.length;
    let count = 0;

    for (let i=0; i<len-2; i++) {
        for (let j=i+1; j<len-1; j++) {
            for (let k=j+1; k<len; k++) {
                primeNumber(nums[i] + nums[j] + nums[k]) && count++;
            } 
        }
    }
    
    return count;
}

function primeNumber(sum) {
    for (let i=2; i<sum; i++){
        if (sum % i === 0) {
            return false
        } 
    }
    return true;
}