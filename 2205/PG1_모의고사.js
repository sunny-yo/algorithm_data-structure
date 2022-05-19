// https://programmers.co.kr/learn/courses/30/parts/12230

function solution(answers) {
  const answer = [];
  const score = [null, 0, 0, 0];
  const patterns = [
    null,
    [1, 2, 3, 4, 5],
    [2, 1, 2, 3, 2, 4, 2, 5],
    [3, 3, 1, 1, 2, 2, 4, 4, 5, 5],
  ];

  answers.forEach((answer, idx) => {
    patterns[1][idx % patterns[1].length] === answer && score[1]++;
    patterns[2][idx % patterns[2].length] === answer && score[2]++;
    patterns[3][idx % patterns[3].length] === answer && score[3]++;
  });

  const maxScore = Math.max(...score);
  score.forEach((num, idx) => {
    num === maxScore && answer.push(idx);
  });

  return answer;
}
