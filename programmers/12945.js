function solution(n) {
    const fibonacci = [0, 1];
    for (let i=2; i<n+1; i++){
        fibonacci.push((fibonacci[i-2] + fibonacci[i-1])%1234567);
    }

    return fibonacci[fibonacci.length-1];

}

console.log(solution(5));