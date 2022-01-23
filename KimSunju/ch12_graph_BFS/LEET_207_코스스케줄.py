from collections import deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_dic = {}
        course = deque(range(numCourses))
        finish = []

        for next, pre in prerequisites:
            if pre in course_dic:
                course_dic[pre].append(next)
            else:
                course_dic[pre] = [next]

        while course:
            now = course.popleft()
            finish.append(now)
            if now in course_dic:
                for next in course_dic[now]:
                    finish.append(next)

        result = set(finish)
        if len(result) != numCourses:
            return False

        return True


s = Solution()
print(s.canFinish(2, [[1, 0]]))
print(s.canFinish(2, [[1,0],[0,1]]))
