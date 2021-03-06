import random


def division_edition(num_quests, one, two, three, four, ident):
    score = 0
    attempts = 1
    while attempts < (num_quests + 1):
        a = random.randint(one, two)
        b = random.randint(three, four)

        if (a > b) and (a % b == 0):
            try:
                if ident == 5:
                    if attempts == 10:
                        quest = int(input('\n{}. {:>3d}\n{:>8s}\n{:>7d}\n\n= {:>2s}'.format(attempts,
                                                                                            a,
                                                                                            '----',
                                                                                            b,
                                                                                            '')))
                    else:
                        quest = int(input('\n{}. {:>4d}\n{:>8s}\n{:>7d}\n\n= {:>2s}'.format(attempts,
                                                                                            a,
                                                                                            '----',
                                                                                            b,
                                                                                            '')))
                elif attempts >= 10:
                    quest = int(input('\n{}. {:>4d}\n{:>8s}\n{:>7d}\n\n= {:>2s}'.format(attempts,
                                                                                        a,
                                                                                        '----',
                                                                                        b,
                                                                                        '')))
                else:
                    quest = int(input('\n{}. {:>4d}\n{:>8s}\n{:>7d}\n\n= {:>2s}'.format(attempts,
                                                                                        a,
                                                                                        '-----',
                                                                                        b,
                                                                                        '')))
                # Just decorating how the code will look in the terminal

                if quest == (a / b):
                    print('\nYour Answer Is Correct\n')
                    score += 1
                else:
                    print(f'\nYour Answer Is Wrong\nThe Correct Answer Is {a / b}\n')
            except SyntaxError:
                print('Invalid Input ---: Please Enter A Number\n')
            except ValueError:
                print('Invalid Input ---: Please Enter A Number\n')

            attempts += 1
        else:
            attempts += 0

    print(f'\nYou Got {score}/{num_quests}')
