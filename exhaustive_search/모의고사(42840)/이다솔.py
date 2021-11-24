def solution(answers) :
    students = [[1, 2, 3, 4, 5],
                [2, 1, 2, 3, 2, 4, 2, 5],
                [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    grades = [0, 0, 0]
    for num_ans, answer in enumerate(answers) :
        for num_std, ans_std in enumerate(students) :
            if answer == ans_std[num_ans % len(ans_std)] :  # 정답이 해당 학생의 찍은 답이랑 같은지 확인
                grades[num_std] += 1
    winner = [idx + 1 for idx, grade in enumerate(grades) if grade == max(grades)] # 가장 많이 맞춘 학생 뽑기
    return winner
