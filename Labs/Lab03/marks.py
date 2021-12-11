students = [
    {
        "name": "Matt",
        "homework": [90.0, 97.0, 75.0, 92.0],
        "quizzes": [88.0, 40.0, 94.0],
        "tests": [75.0, 90.0],
    },
    {
        "name": "Mich",
        "homework": [100.0, 92.0, 98.0, 100.0],
        "quizzes": [82.0, 83.0, 91.0],
        "tests": [89.0, 97.0],
    },
    {
        "name": "Mark",
        "homework": [0.0, 87.0, 75.0, 22.0],
        "quizzes": [0.0, 75.0, 78.0],
        "tests": [100.0, 100.0],
    },
]

if __name__ == '__main__':

    homework = []
    quizzes = []
    tests = []

    for student in students:
        homework += student['homework']
        quizzes += student['quizzes']
        tests += student['tests']

    print(f"Average homework mark: {sum(homework) / len(homework)}")
    print(f"Average quiz mark: {sum(quizzes) / len(quizzes)}")
    print(f"Average test mark: {sum(tests) / len(tests)}")
    print("\n")
