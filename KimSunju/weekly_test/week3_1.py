# https://programmers.co.kr/learn/courses/30/lessons/17686

def solution(files):
    answer = []

    for file in files:
        num_start, tail_start = None, None

        for i in range(len(file)):
            if file[i].isdigit():
                num_start = i
                break

        for i in range(num_start, len(file)):
            if not file[i].isdigit():
                tail_start = i
                break

        head = file[:num_start]
        number = file[num_start:(tail_start if tail_start else len(file))]
        answer.append((head, number, file))

    answer.sort(key=lambda x: (x[0].upper(), int(x[1])))

    return [file[2] for file in answer]

print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))

## 계속 에러 났던 이유 : tail이 없을 경우에 대한 조건을 넣지 않아서