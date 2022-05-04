// https://programmers.co.kr/learn/courses/30/lessons/42746

function solution(numbers) {
  const sorted = [...numbers]
    .map(num => `${num}`)
    .sort((a, b) => b + a - (a + b))
    .join('');
  return sorted[0] === '0' ? '0' : sorted;
}

console.assert(solution([6, 10, 2]) === '6210');
console.assert(solution([3, 30, 34, 5, 9]) === '9534330');
