def stack_series(nums):
    answer = []     # 답으로 return할 list
    stack = []      # 입력으로 받는 수들과 똑같이 만들어보기 위한 리스트
    count = 1

    # nums가 비어있을 때
    if nums is None:
        return False

    for i in range(len(nums)):
        # 1. 입력 숫자 == count
        if nums[i] == count:
            stack.append(count)
            answer.append('+')
            count += 1
        # 2. 입력 숫자 > count
        elif nums[i] > count:
            t = nums[i] - nums[i - 1] - 1   # 2, 5 // 2, 3, 4 - 4 - 3 -> 2, 5
            while nums[i] > count:
                stack.append(count)
                answer.append('+')
                count += 1
            while t > 0:
                stack.pop()
                answer.append('-')
                t -= 1
        # 3. 입력 숫자 < count
        else:
            return False
    return answer


print(stack_series([1, 2, 5, 7, 8]))
assert stack_series([1, 3, 6, 7, 8, 9])

assert not stack_series([1, 3, 5, 3, 6, 7, 1])
assert not stack_series([1, 2, 5, 7, 8, 9, 11, 7, 8, 9])
