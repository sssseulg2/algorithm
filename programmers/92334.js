function solution(id_list, report, k) {
    const reportSet = new Set(report);
    report = Array.from(reportSet);
    const answer = new Array(id_list.length).fill(0);
    const reportCount = new Array(id_list.length).fill(0);

    report.map((element)=> {
        reportCount[id_list.indexOf(element.split(' ')[1])]++;
    })
    report.map((element)=>{
        let fromTo = element.split(' ');
        reportCount[id_list.indexOf(fromTo[1])] >= k && answer[id_list.indexOf(fromTo[0])]++;
    })

    return answer;
}

console.log(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
console.log(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))
