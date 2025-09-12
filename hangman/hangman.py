from words import words
import random
import string
from lives_visual_dist import lives_visual_dist
def get_valid_words(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    
    return word.upper()

def hangman():
    word = get_valid_words(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 7
    
    while len(word_letters) > 0 and lives > 0:
        print(f'You have {lives} lives left and you have used these letters: {used_letters}')
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dist[lives])
        print(f'Current word: {word_list}')
    
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')
            else:
                lives -= 1
                print(f'\n Your Letter {user_letter} is not in the word.')
        elif user_letter in used_letters:
            print(f'You\'ve already used this letter. Guess another letter.')
        else:
            print('\n That is not valid letter.')
        
    if lives == 0:
        print(lives_visual_dist[lives])
        print('You died, sorry. The word was', word)
    else:
        print(f'YAY! You guessed the word {word}!!!')
            
hangman()
