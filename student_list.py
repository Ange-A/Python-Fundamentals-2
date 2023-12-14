if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    def calculate_average_marks(student_marks, query_name):
        if query_name in student_marks:
            marks = student_marks[query_name]
            average_score = sum(marks) / len(marks)
            print("{:.2f}".format(average_score))
        else:
            print("Student not found in records.")

    # Call the function with the provided data
    calculate_average_marks(student_marks, query_name)
  