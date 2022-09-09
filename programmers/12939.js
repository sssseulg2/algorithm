function solution(s) {
    let arr = s.split(" ");
    arr.map((element, index)=>{
        arr[index] = Number(element);
    })
    let min = arr[0]; 
    let max = arr[0];
    for (let i = 1; i < arr.length; i++) {
        if (min > arr[i]) {
            min = arr[i]
        }
        if (max < arr[i]) {
            max = arr[i]
        }
    }
    
    
    return min.toString() + " " + max.toString();
}