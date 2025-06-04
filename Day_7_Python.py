#Hangman Project Day 7 Python
import random
##My hangman Solution (Not quite perfect, in a list instead of string)
# print("Welcome to the hangman game!")
# def hangman():
#     lives_remaining = 6
#     hangman_string = ""
#     random_words = ["fifth"]
#     hangman_word = random.choice(random_words)
#     hangman_word_list = []
#     for i in hangman_word:
#         hangman_word_list.append("_ ")
#     print("Guess the word: " + hangman_string)
#     while hangman_string != hangman_word:
#         print(hangman_word_list)
#         user_guess = input("Which letter would you like to guess for the word?\n")
#         if user_guess == hangman_word[0]:
#             hangman_word_list.pop(0)
#             hangman_word_list.insert(0, user_guess)
#             print("Good Job! Try to guess the next letter!\n")
#         if user_guess == hangman_word[1]:
#             hangman_word_list.pop(1)
#             hangman_word_list.insert(1, user_guess)
#             print("Good Job! Try to guess the next letter!\n")
#         if user_guess == hangman_word[2]:
#             hangman_word_list.pop(2)
#             hangman_word_list.insert(2, user_guess)
#             print("Good Job! Try to guess the next letter!\n") 
#         if user_guess == hangman_word[3]:
#             hangman_word_list.pop(3)
#             hangman_word_list.insert(3, user_guess)   
#             print("Good Job! Try to guess the next letter!\n")
#         if user_guess == hangman_word[4]:
#             hangman_word_list.pop(4)
#             hangman_word_list.insert(4, user_guess)   
#             print("Good Job! Try to guess the next letter!\n")
#         elif user_guess != hangman_word[0] or user_guess != hangman_word [1] or user_guess != hangman_word [2] or user_guess != hangman_word [3] or user_guess != hangman_word [4]:
#             lives_remaining -= 1
#             print(f"Wrong guess! You have {lives_remaining}/6 lives remaining\n")    
# hangman()        
## Teacher hangman solution
# word_list = ["aardvark", "baboon", "camel", "eliot"]
# chosen_word = random.choice(word_list)
# word_length = len(chosen_word)
# print(chosen_word)
# lives = 6
# game_over = False
# placeholder = ""
# for char in range(word_length):
#     placeholder += "_"
# print(placeholder)
# display = ""
# correct_letters = []
# while not game_over:
#     guess_a_letter = input("Guess a letter: ").lower()
#     print(display)
#     for letter in chosen_word:
#         if letter == guess_a_letter:
#             display += letter
#             correct_letters.append(letter)
#         elif letter in correct_letters:
#             display += letter
#         else:
#             display += "_"
#     if "_" not in display:
#         game_over = True
#         print("You win!")
# lives -= 1
# print(f"You guessed wrong! You have {lives}/6 remaining.")
# if lives < 1:
#     print("You have lost the game!")
#CHATGPT Solution
# import random

def choose_word():
    words = ['python', 'hangman', 'developer', 'computer', 'keyboard', 'program']
    return random.choice(words)

def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman():
    word = choose_word()
    guessed_letters = set()
    attempts = 6  # Traditional Hangman gives 6 tries
    print("Welcome to Hangman!")

    while attempts > 0:
        print("\nWord:", display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Correct!")
        else:
            attempts -= 1
            print(f"Wrong! You have {attempts} {'attempt' if attempts == 1 else 'attempts'} left.")

        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You guessed the word:", word)
            break
    else:
        print("\nGame over! The word was:", word)

if __name__ == "__main__":
    hangman()        

