from game_logic import multiplication_edition


def run_multiplication():
    level_dif = input('Welcome To Math Trivia (Multiplication Edition)\n'
                      '(E) - For Easy, (M) - For Medium, (H) - For Hard\n\nEnter Difficulty: ')

    level_dif = level_dif.lower()

    if level_dif == 'e':
        multiplication_edition(10, 2, 12, 5)
    elif level_dif == 'm':
        multiplication_edition(20, 10, 18, 4)
    elif level_dif == 'h':
        multiplication_edition(25, 12, 24, 4)
    else:
        print('Invalid Input ---: Please Rerun The Program')


run_multiplication()
