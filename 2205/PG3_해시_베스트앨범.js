// https://programmers.co.kr/learn/courses/30/lessons/42579

function solution(genres, plays) {
  const answer = [];
  const mapPlay = {};
  const map = {};

  genres.forEach((genre, idx) => {
    map[genre]
      ? map[genre].push([plays[idx], idx])
      : (map[genre] = [[plays[idx], idx]]);

    mapPlay[genre]
      ? (mapPlay[genre] += plays[idx])
      : (mapPlay[genre] = plays[idx]);
  });

  const sortedPlay = Object.keys(mapPlay).sort(
    (a, b) => mapPlay[b] - mapPlay[a]
  );

  sortedPlay.map(genre => {
    const sortedList = map[genre].sort((a, b) => b[0] - a[0]);
    sortedList.forEach((li, idx) => {
      idx < 2 && answer.push(li[1]);
    });
  });

  return answer;
}

console.log(
  solution(
    ['classic', 'pop', 'classic', 'classic', 'pop'],
    [500, 600, 150, 800, 2500]
  )
);
