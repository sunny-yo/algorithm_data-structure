// https://programmers.co.kr/learn/courses/30/lessons/42586

function solution(progresses, speeds) {
  const answer = [];
  let works = [...progresses];

  while (works.length > 0) {
    let count = 0;
    let days = parseInt((100 - works[0]) / speeds[0]);
    (100 - works[0]) % speeds[0] > 0 && days++;

    works = works.map((done, idx) => done + speeds[idx] * days);

    while (works[0] >= 100) {
      works.shift();
      speeds.shift();
      count += 1;
    }

    answer.push(count);
  }

  return answer;
}

console.log(solution([93, 30, 55], [1, 30, 5]));
console.log(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]));
