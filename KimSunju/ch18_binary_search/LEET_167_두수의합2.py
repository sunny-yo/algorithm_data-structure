# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
import bisect
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = set()

        # 같은 인덱스의 숫자를 사용한 것을 제외할 수 없음
        # for num in numbers:
        #     wanted = target - num
        #     idx = bisect.bisect_left(numbers, wanted)
        #     if idx < len(numbers) and numbers[idx] == wanted:
        #         result += [idx+1]

        for i in range(len(numbers)):
            wanted = target - numbers[i]
            idx = bisect.bisect_left(numbers, wanted)
            if idx < len(numbers) and numbers[idx] == wanted and i != idx:
                result.add(i+1)
                result.add(idx+1)

        return sorted(list(result))


s = Solution()
print(s.twoSum(numbers=[2, 7, 11, 15], target=9))
print(s.twoSum(numbers=[2, 3, 4], target=6))
print(s.twoSum(numbers=[-1, 0], target=-1))
