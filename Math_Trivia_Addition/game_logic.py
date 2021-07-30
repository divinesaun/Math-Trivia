import random


def addition_edition(num_quests, one, two, ident):
    score = 0

    for attempts in range(1, num_quests + 1):
        a = random.randint(one, two)
        b = random.randint(one, two)
        try:
            if ident == 5:
                if attempts == 10:
                    quest = int(input('{}. {:>3d}\n  +{:>4d}\n{:>5s}'.format(attempts, a, b, '')))
                else:
                    quest = int(input('{}. {:>4d}\n  +{:>4d}\n{:>5s}'.format(attempts, a, b, '')))
            elif attempts >= 10:
                quest = int(input('{}. {:>4d}\n  +{:>5d}\n{:>5s}'.format(attempts, a, b, '')))
            else:
                quest = int(input('{}. {:>4d}\n  +{:>4d}\n{:>4s}'.format(attempts, a, b, '')))
            # Just decorating how the code will look in the terminal

            if quest == (a + b):
                print('\nYour Answer Is Correct\n')
                score += 1
            else:
                print(f'\nYour Answer Is Wrong\nThe Correct Answer Is {a + b}\n')
        except SyntaxError:
            print('Invalid Input ---: Please Enter A Number\n')
        except ValueError:
            print('Invalid Input ---: Please Enter A Number\n')

    print(f'\nYou Got {score}/{num_quests}')
