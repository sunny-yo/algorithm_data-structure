class Solution:
    def threeSum(self, nums):
        result = []
        # 예외처리 : nums가 3개가 안될 때
        if len(nums) < 3:
            return result

        nums.sort() # nums를 숫자 순서대로 제자리 정렬
        for i in range(len(nums) - 2): # i = 0 ~ len(nums) -2
            if i > 0 and nums[i] == nums[i - 1]:
            # 기준되는 값이 중복될 경우 같은 케이스가 되니까 그걸 건너뛴다
            # nums[i]값이 이미 했던 값이면 다음 조건을 수행하러 간다
                continue

            # 기준값인 i를 두고 left, right 포인터 설정
            left = i + 1
            right = len(nums) -1
            while left < right: # left < right 이면
                sum = nums[i] + nums[left] + nums[right] # 각 인덱스에 해당하는 값을 더한다
                if sum < 0: # 0보다 작으면 left 포인터를 올린다 = 값을 큰값으로 변경한다
                    left += 1
                elif sum > 0: # 0보다 크면 right 포인터를 내린다 = 값을 작은값으로 변경한다
                    right -= 1
                else: # sum이 0이면
                    # 해당하는 값들을 result에 리스트 형태로 append
                    result.append([nums[i], nums[left], nums[right]])

                    # 인덱스가 left < right이면 = 포인터가 아직 안쪽까지 확인하지 못했고
                    while left < right and nums[left] == nums[left+1]:
                    # 왼쪽 포인터의 값이 다음에 가리킬 값과 같다면 +1 이동
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                    # 오른쪽 포인터의 값이 다음에 가리킬 값과 같다면 -1 이동
                        right -= 1

                    # 포인터가 가리키고 있는 값은 이미 확인한 값이므로 한칸씩 안쪽으로 이동
                    # 한쪽만 움직이지 않는 이유는
                    # 기준점인 i의 값과 움직이지 않은 포인터의 값이 그대로이기 때문에
                    # 한 쪽만 움직여도 해당 케이스는 나오지 않는다.
                    left += 1
                    right -= 1
        return result


s = Solution()
print(s.threeSum([-1, 0, 1, 2, -1, -4]))

# from typing import List
#
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         results = []
#         nums.sort()
#
#         for i in range(len(nums) - 2):
#             # 중복된 값 건너뛰기
#             # 기준되는 값이 중복될 경우 같은 케이스가 되니까 그걸 건너뛴다
#             if i > 0 and nums[i] == nums[i - 1]:
#                 continue
#
#             # 간격을 좁혀가며 합 `sum` 계산
#             left, right = i + 1, len(nums) - 1
#             while left < right:
#                 sum = nums[i] + nums[left] + nums[right]
#                 if sum < 0:
#                     left += 1
#                 elif sum > 0:
#                     right -= 1
#                 else:
#                     # `sum = 0`인 경우이므로 정답 및 스킵 처리
#                     results.append([nums[i], nums[left], nums[right]])
#
#                     while left < right and nums[left] == nums[left + 1]:
#                         left += 1
#                     while left < right and nums[right] == nums[right - 1]:
#                         right -= 1
#                     left += 1
#                     right -= 1
#
#         return
