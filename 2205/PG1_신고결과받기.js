// https://programmers.co.kr/learn/courses/30/lessons/92334

function solution(id_list, report, k) {
  const answer = [];

  const userInfo = {};
  const notifiedUser = [];
  const notified = [];

  id_list.forEach(user => {
    userInfo[user] = [];
  });

  new Set(report).forEach(user => {
    const [user1, user2] = user.split(' ');
    userInfo[user1].push(user2);
    notifiedUser.push(user2);
  });

  id_list.forEach(user => {
    const length = notifiedUser.filter(notiUser => notiUser === user).length;
    length >= k && notified.push(user);
  });

  id_list.forEach((user, idx) => {
    answer.length < idx + 1 && answer.push(0);
    notified.forEach(noti => {
      userInfo[user].includes(noti) && answer[idx]++;
    });
  });

  return answer;
}

console.log(
  solution(
    ['muzi', 'frodo', 'apeach', 'neo'],
    ['muzi frodo', 'apeach frodo', 'frodo neo', 'muzi neo', 'apeach muzi'],
    2
  )
);

console.log(
  solution(['con', 'ryan'], ['ryan con', 'ryan con', 'ryan con', 'ryan con'], 3)
);
