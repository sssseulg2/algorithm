function solution(numbers) {
  const sortedNum = numbers.sort();
  console.log(sortedNum);

  let answer = 0;
  let number = 0;

  for (let i = 0; i < 10; i++) {
    if (sortedNum[number] !== i) {
      answer += i;
      number--;
    }
    number++;
  }

  return answer;
}

// console.log(solution([1, 2, 3, 4, 6, 7, 8, 0]));
console.log(solution([5, 8, 4, 0, 6, 7, 9]));
