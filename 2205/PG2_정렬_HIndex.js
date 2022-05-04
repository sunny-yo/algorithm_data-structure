// https://programmers.co.kr/learn/courses/30/lessons/42747

function solution(citations) {
  let maxH = 0;
  citations.sort((a, b) => b - a);

  while (maxH + 1 <= citations[maxH]) {
    maxH += 1;
  }

  return maxH;
}

console.assert(solution([3, 0, 6, 1, 5]) === 3);
