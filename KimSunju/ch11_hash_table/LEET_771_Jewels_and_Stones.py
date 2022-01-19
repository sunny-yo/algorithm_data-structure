import collections

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        result = 0
        stone_counter = collections.Counter(stones)

        for i in jewels:
            result = result + stone_counter[i]

        return result

s = Solution()
print(s.numJewelsInStones("aA", "aAAbbbb"))