function solution(new_id) {    
    let recommend = level7(level6(level5(level3(level4(level2(level1(new_id)))))))
    
    return recommend.join("");
}

function level1(id) {
    let recommend = id.toLowerCase().split('');
    return recommend;
}
function level2(id) {
    const letterForm = ["-","_","."];
    for (let i = 97; i < 123; i++){
        letterForm.push(String.fromCharCode(i));
    }
    for (let i = 0; i < 10; i++) {
        letterForm.push(i.toString());
    }
    let recommend = id.filter(letter => letterForm.includes(letter));
    return recommend
}
function level3(id) {

    let before = false;
    let index = 0;
    while (index < id.length) {
        if (id[index] === ".") {
            if (before === true) {
                id.splice(index, 1);
                index --;
            }
            before = true;
        }
        else {before=false;}
        index ++;
    }
    return id;
}
function level4(id) {
    let start = 0;
    let end = id.length;
    for (let i = 0; i < id.length; i++) {
        if (id[i] === ".") { 
            start ++;
        }
        else {break;}
    }
    for (let i = id.length-1; i >= 0; i--) {
        if (id[i] === ".") {
            end --;
        }
        else {break;}
    }
    return id.slice(start, end);
}
function level5(id) {
    if (id.length === 0) {
        return ["a"];
    }
    return id;
}
function level6(id) {
    if (id.length >= 16) {
        let end = 15;
        for (let i = 14; i >= 0; i--) {
            if (id[i] === ".") {
                end --;
            }
            else {break;}
        }
        return id.slice(0, end);
    }
    return id;
}
function level7(id) {
    if (id.length === 1) {
        id.push(id[0]);
    }
    if (id.length === 2) {
        id.push(id[1]);
    }
    return id;
}
// console.log(solution("...!@BaT#*..y.abcdefghijklm"));
console.log(solution("123_.def"));