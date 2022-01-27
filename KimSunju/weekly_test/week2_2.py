# https://programmers.co.kr/learn/courses/30/lessons/43165

# 제출한 답
def solution(numbers, target):
    pm = ['+', '-']
    answer = 0

    def dfs(i, sum):
        nonlocal answer
        if i >= len(numbers) and sum == target:
            answer += 1
            return
        elif i >= len(numbers) and (sum < target or sum > target):
            return


        for x in pm:
            if x == '+':
                dfs(i + 1, sum + numbers[i])
            elif x == '-':
                dfs(i + 1, sum - numbers[i])

    dfs(0, 0)

    return answer


print(solution([1, 1, 1, 1, 1], 3))


'''
# 하던 중
# [1, 1, 1, 1, 1, -1, -1, -1, -1, -1]에서 5개 뽑아서 target 찾기
# 문제점 : 1111이후에 뒤에 -1 -1 -1이 계속 들어오면 같은 답이 반복된다
def solution(numbers, target):
    flipped = list(map(lambda x: -x, numbers[:]))
    nums_list = numbers + flipped
    answer = 0

    def dfs(index, sum, n):
        nonlocal answer
        if n <= 0 and sum == target:
            answer += 1
            return
        elif n <= 0 and sum != target:
            return

        for i in range(index, len(nums_list) - n + 1):
            dfs(i + 1, sum + nums_list[i], n - 1)

    dfs(0, 0, len(numbers))

    return answer


print(solution([1, 1, 1, 1, 1], 3))
'''