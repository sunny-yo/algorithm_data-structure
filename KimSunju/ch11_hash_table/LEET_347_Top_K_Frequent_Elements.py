import collections

class Solution:
    def topKFrequent(self, nums, k):
        result = []
        count_dic = collections.Counter(nums)
        sorted_items = sorted(count_dic.items(), key=lambda x:x[1], reverse=True)
        for i in range(k):
            result.append(sorted_items[i][0])
        return result


s = Solution()
print(s.topKFrequent([1,1,1,2,2,3], 2))