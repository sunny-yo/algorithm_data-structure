# import sys
# num = int(sys.stdin.readline())
# nums = [sys.stdin.readline().strip() for i in range(num)]
#
# stack = []
# answer = []
# count = 1
#
# for num in range(nums):
#     if num == count:
#         stack.append(count)
#         answer.append('+')
#     elif num > count:
#         t = num - count
#         while t > 0:
#             answer.append('+')
#             t -= 1
#         t = num - count
#         while t > 0:
#             answer.append('-')
#             t -= 1
#         t = num - count
#         count = count + t + 1
#     else:
#         print("NO")
#
#     for i in answer:
#         print(i)


def stack_series(nums):
    answer = []
    stack = []
    count = 1

    if nums is None:
        return False

    for i in range(len(nums)):
        if nums[i] == count:
            stack.append(count)
            answer.append('+')
            count += 1
        elif nums[i] > count:
            t = nums[i] - nums[i - 1] - 1
            while nums[i] > count:
                stack.append(count)
                answer.append('+')
                count += 1
            while t > 0:
                stack.pop()
                answer.append('-')
                t -= 1
        else:
            return False
    return answer


assert stack_series([1, 2, 5, 7, 8])
assert stack_series([1, 3, 6, 7, 8, 9])

assert not stack_series([1, 3, 5, 3, 6, 7, 1])
assert not stack_series([1, 2, 5, 7, 8, 9, 11, 7, 8, 9])
