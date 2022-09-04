function solution(numbers, hand) {
  const answer = [];

  let leftHand = [0, 3];
  let rightHand = [2, 3];
  const middle = [2, 5, 8, 0];

  numbers.map((element) => {
    if ([1, 4, 7].includes(element)) {
      leftHand = [0, [1, 4, 7].indexOf(element)];
      answer.push("L");
    } else if ([3, 6, 9].includes(element)) {
      rightHand = [2, [3, 6, 9].indexOf(element)];
      answer.push("R");
    } else {
      let idx = [2, 5, 8, 0].indexOf(element);
      let leftDistance = Math.abs(idx - leftHand[1]) + 1 - leftHand[0];
      let rightDistance = Math.abs(idx - rightHand[1]) + rightHand[0] - 1;

      if (leftDistance < rightDistance) {
        leftHand = [1, idx];
        answer.push("L");
      } else if (rightDistance < leftDistance) {
        rightHand = [1, idx];
        answer.push("R");
      } else {
        if (hand === "left") {
          leftHand = [1, idx];
          answer.push("L");
        } else {
          rightHand = [1, idx];
          answer.push("R");
        }
      }
    }
  });

  return answer.join("");
}

console.log(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"));
