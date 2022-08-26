function solution(strings, n) {
    strings.sort(function(a, b){
       return a[n] < b[n] ? -1 : a[n] > b[n] ? 1 : (a < b ? -1 : a > b ? 1 : 0);
    });
    return strings;
}