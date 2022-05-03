// https://programmers.co.kr/learn/courses/30/lessons/42578

function solution(clothes) {
  const clothesMap = {};
  let answer = 1;

  clothes.forEach(clothList => {
    const [cloth, kinds] = clothList;
    if (clothesMap[kinds]) {
      clothesMap[kinds] += 1;
    } else {
      clothesMap[kinds] = 1;
    }
  });

  for (let key in clothesMap) {
    answer *= clothesMap[key] + 1;
  }

  return answer - 1;
}

console.log(
  solution([
    ['yellowhat', 'headgear'],
    ['bluesunglasses', 'eyewear'],
    ['green_turban', 'headgear'],
  ])
);
console.log(
  solution([
    ['crowmask', 'face'],
    ['bluesunglasses', 'face'],
    ['smoky_makeup', 'face'],
  ])
);
