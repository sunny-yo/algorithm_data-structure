// https://programmers.co.kr/learn/courses/30/lessons/77484

function solution(lottos, win_nums) {
  const winMap = { 6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6 };
  // const winMap = [6, 6, 5, 4, 3, 2, 1];

  let numMatched = 0;
  let numZero = lottos.filter(num => num === 0).length;

  win_nums.forEach(num => {
    lottos.includes(num) && numMatched++;
  });

  return [winMap[numMatched + numZero], winMap[numMatched]];
}

console.log(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]));

console.log(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]));

console.log(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]));
