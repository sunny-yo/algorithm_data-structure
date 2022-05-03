// https://programmers.co.kr/learn/courses/30/lessons/42576

function solution(participant, completion) {
  const map = {};
  const answerList = [];

  participant.forEach(person => {
    if (map[person]) {
      map[person] += 1;
    } else {
      map[person] = 1;
    }
  });

  completion.forEach(person => {
    map[person] -= 1;
  });

  Object.keys(map).forEach(person => {
    map[person] > 0 && answerList.push(person);
  });

  return answerList.join(' ');
}

console.log(solution(['leo', 'kiki', 'eden'], ['eden', 'kiki']));
console.log(
  solution(
    ['marina', 'josipa', 'nikola', 'vinko', 'filipa'],
    ['josipa', 'filipa', 'marina', 'nikola']
  )
);
console.log(
  solution(['mislav', 'stanko', 'mislav', 'ana'], ['stanko', 'ana', 'mislav'])
);
