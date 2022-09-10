function solution(s) {
    let convert = 0;
    let zero = 0;
    while (s !== "1") {
        let noZero = s.replace(/0/g, "");
        zero += s.length - noZero.length;
        s = noZero.length.toString(2);
        convert += 1;
    }


    return [convert, zero];
}

console.log(solution("110010101001"));
console.log(solution("01110"));
console.log(solution("1111111"));
