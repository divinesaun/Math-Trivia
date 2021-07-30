from game_logic import division_edition


def run_division():
    level_dif = input('Welcome To Math Trivia (Division Edition)\n'
                      '(E) - For Easy, (M) - For Medium, (H) - For Hard\n\nEnter Difficulty: ')

    level_dif = level_dif.lower()

    if level_dif == 'e':
        division_edition(10, 9, 50, 2, 25, 5)
    elif level_dif == 'm':
        division_edition(20, 18, 72, 7, 25, 4)
    elif level_dif == 'h':
        division_edition(25, 27, 250, 12, 25, 4)
    else:
        print('Invalid Input ---: Please Rerun The Program')


run_division()
