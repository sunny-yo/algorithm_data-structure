import collections
import heapq

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tracker = collections.defaultdict(int)
        for c in s:
            tracker[c] += 1
        for c in t:
            tracker[c] -= 1
        return all(c == 0 for c in tracker.values())

s = Solution()
print(s.isAnagram("anagram", "nagaram"))
print(s.isAnagram(s = "rat", t = "car"))


'''
# defaultdict 사용 (48ms, faster than 80.64%)
    def isAnagram(self, s: str, t: str) -> bool:
        tracker = collections.defaultdict(int)
        for c in s:
            tracker[c] += 1
        for c in t:
            tracker[c] -= 1
        return all(c == 0 for c in tracker.values())
'''

'''
# Counter 사용 (90ms, faster than 18.41%)
    def isAnagram(self, s: str, t: str) -> bool:
        return collections.Counter(s) == collections.Counter(t)
'''

'''
# heapq 사용 (149ms, faster than 5.05%)
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        heap_s = []
        heap_t = []

        for char_s in s:
            heapq.heappush(heap_s, char_s)
        for char_t in t:
            heapq.heappush(heap_t, char_t)

        for _ in range(len(s)):
            if heapq.heappop(heap_s) != heapq.heappop(heap_t):
                return False

        return True
'''

'''
# sorted 사용(71ms, faster tan 38.48%)
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
'''