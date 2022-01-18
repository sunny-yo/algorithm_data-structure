# s "[]()"
from collections import deque


def is_valid(s):
    pair = {
        '}': "{",
        ')': "(",
        ']': "[",
    }
    opener = "{[("
    stack = []

    for char in s:
        if char in opener:
            stack.append(char)
        else:
            top = stack.pop()
            if pair[char] != top:
                return False

        return not stack

def get_card(num):
    # 1. 제일 위 카드를 버린다.
    # 2. 그 다음 카드를 제일 뒤로 옮긴다.
    # 3. 한 장 남은 카드를 반환한다.
    queue = deque([n for n in range(1, num + 1)])
    while len(queue) >1:
        queue.popleft()
        queue.append(queue.popleft())

    return queue.popleft()


# assert is_valid("{}()[]")
# assert is_valid("{[]}")
# assert is_valid("({[]}")
#
# assert not is_valid("{}]")
# assert not is_valid("{{{{{{{{{{}}}}}}")

assert get_card(6) == 4