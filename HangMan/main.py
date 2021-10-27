import random
from hangman_art import stages, logo
from hangman_words import word_list


def split(chose_word):
    return list(chose_word)


print(logo)
game_is_finished = False
lives = len(stages) - 1

chosen_word = word_list[random.randint(0, 2)]

# print(chosen_word)

# print(user_guess.lower())

letter_check = split(chosen_word)
fake_list = []

for _ in range(len(chosen_word)):
    fake_list += "_"

# print(letter_check)

end_of_game = False

while not end_of_game:
    user_guess = input("Guess a letter.\n").lower()

    if user_guess in fake_list:
        print(f"You've already guessed {user_guess}")

    for position in range(len(chosen_word)):
        letter = letter_check[position]
        if letter == user_guess:
            fake_list[position] = letter

    if user_guess not in letter_check:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")

    if "_" not in fake_list:
        end_of_game = True
        print("You win")

    print(stages[lives])
