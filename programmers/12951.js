function solution(s) {
    let arr = s.split("");
    let before = true;

    for (let i = 0; i < arr.length; i++) {
        if (arr[i] === " ") {
            before = true;
            continue;
        }

        let ascii = arr[i].charCodeAt(0);
        if (before === true) {
            if (ascii > 96 && ascii <123) {
                arr[i] = String.fromCharCode(ascii-32);
            }
        }
        else {
            if (ascii > 64 && ascii < 91) {
                arr[i] = String.fromCharCode(ascii+32);
            }
        }
        before = false;
    }
    return arr.join("");
}

console.log(solution("3people unFollowed me"));
console.log(solution("for the last week "));