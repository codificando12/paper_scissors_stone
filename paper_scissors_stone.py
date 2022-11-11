import random

def choose_options():
    options = ('stone', 'papper', "scissors")
    user_option = input('paper, scissors, stone: ')
    user_option = user_option.lower()
    
    if not user_option in options:
        print(f'{user_option} is not valid option')
        # continue
        return None, None

    computer_option = random.choice(options)

    print(f'{computer_option} vs {user_option}')

    return user_option, computer_option

def check_rules(user_option, computer_option, user_wins, computer_wins):
    if computer_option == user_option:
        print('It is a tie')

    elif user_option == 'stone':
        if computer_option == "scissors":
            print('stone wins against scissors')
            print('You win')
            user_wins += 1
        else:
            print('paper wins against stone')
            print('computer wins')
            computer_wins +=1
    
    elif user_option == 'paper':
        if computer_option == 'stone':
            print('stone wins against scissors')
            print('You win')
            user_wins += 1
        else:
            print('paper wins against stone')
            print('computer wins')
            computer_wins +=1
    
    elif user_option == 'scissors':
        if computer_option == 'paper':
            print('stone wins against scissors')
            print('You win')
            user_wins += 1
        else:
            print('paper wins against stone')
            print('computer wins')
            computer_wins +=1

    return user_wins, computer_wins

def check_winner(user_wins, computer_wins):
    if computer_wins == 2:
        print(f'Computer got {computer_wins} points, it wins')
        exit()
    elif user_wins == 2:
        print(f'User got {user_wins} points, she/he wins')
        exit()

def run_game():
    computer_wins = 0
    user_wins = 0
    rounds = 1

    while True:

        print('*' * 10)
        print(f'ROUND {rounds}')
        print('*' * 10)

        print(f'Computer wins: {computer_wins}')
        print(f'User wins: {user_wins}')
        rounds += 1

        user_option, computer_option = choose_options()
        user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)
        check_winner(user_wins, computer_wins)
        

if __name__ == '__main__':
    run_game()

       