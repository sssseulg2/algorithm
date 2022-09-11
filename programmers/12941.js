function solution(A,B){
    A.sort((a, b) => a - b);
    B.sort((a, b) => b - a);
    
    let sum = 0;
    A.map((value, index)=>{
        sum += (value*B[index]);
    })

    return sum;
}