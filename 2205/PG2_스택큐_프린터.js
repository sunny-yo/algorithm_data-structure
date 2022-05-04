// https://programmers.co.kr/learn/courses/30/lessons/42587

function solution(priorities, location) {
  let count = 0;
  let state = true;
  const q = priorities.map((priority, idx) => [priority, idx]);

  while (state) {
    let re = true;
    const now = q.shift();

    for (let i = 0; i < q.length; i++) {
      if (q[i][0] > now[0]) {
        re = false;
        break;
      }
    }

    if (!re) {
      q.push(now);
    } else {
      count += 1;
      now[1] === location && (state = false);
    }
  }

  return count;
}

console.assert(solution([2, 1, 3, 2], 2) === 1);
console.assert(solution([1, 1, 9, 1, 1, 1], 0) === 5);
