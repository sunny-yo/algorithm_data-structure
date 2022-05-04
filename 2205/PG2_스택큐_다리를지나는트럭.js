// https://programmers.co.kr/learn/courses/30/lessons/42583?language=javascript

function solution(bridge_length, weight, truck_weights) {
  let sec = 0;
  let bridgeQ = [];
  bridgeQ.length = bridge_length;
  bridgeQ.fill(0);

  const leftTruck = [...truck_weights];

  while (leftTruck.length > 0) {
    bridgeQ.shift();
    bridgeQ.reduce((sum, curr) => sum + curr, 0) + leftTruck[0] > weight
      ? bridgeQ.push(0)
      : bridgeQ.push(leftTruck.shift());
    sec += 1;
  }

  while (bridgeQ.reduce((sum, curr) => sum + curr, 0) > 0) {
    bridgeQ.shift();
    sec += 1;
  }

  return sec;
}

console.assert(solution(2, 10, [7, 4, 5, 6]) === 8);
console.assert(solution(100, 100, [10]) === 101);
console.assert(
  solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) === 110
);
