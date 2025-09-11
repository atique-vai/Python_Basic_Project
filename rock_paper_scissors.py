import random
def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r')\
        or (player == 's' and opponent == 'p'):
        return True
    
    return False

def play():
    user = input("Welcome!  Choose \n1. 'r' for rock,\n2. 'p' for paper,\n3. 's' for scissors. \n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It\'s a tie'
    
    if is_win(user, computer):
        return 'You won!'
    return 'You lost!'

print(play())