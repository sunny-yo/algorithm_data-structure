# https://programmers.co.kr/learn/courses/30/lessons/49994

def solution(dirs):
    discovered = []
    curr_x, curr_y = 0, 0

    for c in dirs:
        if c == 'U':
            curr = (curr_x, curr_y)
            if curr_y != 5:
                curr_y += 1
                next = (curr_x, curr_y)
                path = sorted([curr, next])
                if path not in discovered:
                    discovered.append(path)
        elif c == 'D':
            curr = (curr_x, curr_y)
            if curr_y != -5:
                curr_y -= 1
                next = (curr_x, curr_y)
                path = sorted([curr, next])
                if path not in discovered:
                    discovered.append(path)
        elif c == 'R':
            curr = (curr_x, curr_y)
            if curr_x != 5:
                curr_x += 1
                next = (curr_x, curr_y)
                path = sorted([curr, next])
                if path not in discovered:
                    discovered.append(path)
        elif c == 'L':
            curr = (curr_x, curr_y)
            if curr_x != -5:
                curr_x -= 1
                next = (curr_x, curr_y)
                path = sorted([curr, next])
                if path not in discovered:
                    discovered.append(path)

    return len(discovered)


print(solution("ULURRDLLU"))
print(solution("LULLLLLLU"))
