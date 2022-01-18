class Solution:
    def dailyTemperatures(self, temperatures):
        emp = []
        result = []
        for i in range(len(temperatures)):
            if emp == []:
                emp.append(temperatures[i])
                continue


        return emp

s = Solution()
print(s.dailyTemperatures([73,74,75,71,69,72,76,73]))