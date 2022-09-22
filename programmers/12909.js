function solution(s){
    let s_list = s.split("");
    let stack = 0;
    let answer = true;
    
    s_list.map ((value) => {
        if (value === "(") {
            stack += 1;
        }
        else if (value === ")") {
            if (stack > 0) {
                stack -= 1;
            }
            else {
                answer = false;
                return false;
            }
        }
    })
    return answer === false ? false 
    : (
        stack === 0 ? true : false
    );
}


console.log(solution(")"))
// console.log(solution("()()"))