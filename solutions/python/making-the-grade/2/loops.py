def round_scores(student_scores):
    rounded_scores = [round(score) for score in student_scores]
    return rounded_scores

def count_failed_students(student_scores):
    failed_students = [score for score in student_scores if score <= 40 ]
    if failed_students:
         return len(failed_students)
    return 0

def above_threshold(student_scores, threshold):
    best_scores = [score for score in student_scores if score >= threshold ]
    return best_scores

def letter_grades(highest):
    increase = (highest - 40) / 4
    D, C, B, A = 41, int(41 + increase) , int(41 + 2*increase), int(41 + 3*increase)
    return [D, C, B, A]

def student_ranking(student_scores, student_names):
    student_scores_and_names = [f"{index + 1}. {name}: {student_scores[index]}" for index, name in enumerate(student_names)]
    return student_scores_and_names

def perfect_score(student_info):
    student_info = [student_and_score for student_and_score in student_info if student_and_score[1] == 100 ]
    if student_info:
        return student_info[0]
    return student_info
