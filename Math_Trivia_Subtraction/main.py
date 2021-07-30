from game_logic import subtraction_edition


def run_subtraction():
    level_dif = input('Welcome To Math Trivia (Subtraction Edition)\n'
                      '(E) - For Easy, (M) - For Medium, (H) - For Hard\n\nEnter Difficulty: ')

    level_dif = level_dif.lower()

    if level_dif == 'e':
        subtraction_edition(10, 60, 99, 50, 89, 5)
    elif level_dif == 'm':
        subtraction_edition(20, 350, 500, 120, 490, 4)
    elif level_dif == 'h':
        subtraction_edition(25, 700, 999, 300, 989, 4)
    else:
        print('Invalid Input ---: Please Rerun The Program')


run_subtraction()
