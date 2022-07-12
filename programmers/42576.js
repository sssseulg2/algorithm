function solution(participant, completion) {
    const all = {};

    for (let p of participant){
        all[p] = all[p] ? all[p]+1 : 1;
    }
    for (let c of completion){
        all[c]--;
    }
    for (let key in all){
        if(all[key]===1){
            return key;
        }
    }
}

console.log(solution(["leo", "kiki", "eden"],["eden", "kiki"]))