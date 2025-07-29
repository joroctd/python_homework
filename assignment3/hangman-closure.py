def make_hangman(secret_word):
    # set works better here than array
    guesses = set()
    def hangman_closure(letter):
        guesses.add(letter)
        current = ''.join([char if char in guesses else '_' for char in secret_word])
        print(current)
        return not '_' in current
    return hangman_closure

def main():
    try:
        secret_word = input('Please enter the word for Hangman: ')
        game = make_hangman(secret_word)
        done = False
        count = 0
        while not done:
            done = game(input('Enter a letter to guess: ')[0])
            count += 1
        print(f'You won in {count} guesses!')
    except:
        print('An error occurred.')
main()
