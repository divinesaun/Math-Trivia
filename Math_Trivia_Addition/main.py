from game_logic import addition_edition


def run_addition():
    level_dif = input('Welcome To Math Trivia (Addition Edition)\n'
                      '(E) - For Easy, (M) - For Medium, (H) - For Hard\n\nEnter Difficulty: ')

    level_dif = level_dif.lower()

    if level_dif == 'e':
        addition_edition(10, 10, 49, 5)
    elif level_dif == 'm':
        addition_edition(20, 100, 300, 4)
    elif level_dif == 'h':
        addition_edition(25, 200, 499, 4)
    else:
        print('Invalid Input ---: Please Rerun The Program')


run_addition()
