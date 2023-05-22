"""in main module we have main logic of the HangMan game,
from where user is able to play.
"""

from random_number import generate_random_number
from pictures import GameArt

game_art = GameArt()
print(game_art.return_logo())

# Here user will define lowest and highest
# Boundaries for random number.
# User must provide Integer number,
# In other case game won't go on next stage.
BORDERS_ARE_CORRECTS = False
while not BORDERS_ARE_CORRECTS:
    try:
        low_num = int(input("Please define the lowest number: "))
        high_num = int(input("Please define the highest number: "))
        random_number = generate_random_number(num1=low_num, num2=high_num)
        BORDERS_ARE_CORRECTS = True
    except ValueError:
        print("\nPLEASE ENTER ONLY INTEGER NUMBERS!\n")


# Here we start playing game to guess - generated random number.
PLAYER_LIFE = 7
GAME_IS_ENDED = False
while not GAME_IS_ENDED:
    # Here we check, if player provides number.
    # If user provides string that can't be converted into number,
    # Then we will repeat the asking process.
    try:
        user_guess = int(input(f"Guess the Number between {low_num} and {high_num}: "))
        # If player guess the correct number, then game ends immediately.
        if user_guess == random_number:
            print(f"You won the Game and saved innocent person! life - ({PLAYER_LIFE})")
            GAME_IS_ENDED = True
        else:
            # Here we dispay result of wrong answer and dicrease PLAYER_LIFE by one.
            print(game_art.return_stage(stage_index=str(PLAYER_LIFE)))
            PLAYER_LIFE -= 1

            # Here we should tell user if his/her answer is lower
            # Or higher than chosen random number:
            FEEDBACK = "Lower" if user_guess < random_number else "Higher"
            CONTRARY = "Lower" if FEEDBACK == "Higher" else "Higher"
            print(
                f"Your answer ({user_guess}) is {FEEDBACK} than desired random number!"
            )
            print(f"Try {CONTRARY}! life - ({PLAYER_LIFE})")

            # Here we print cross - border line between previous and next stages:
            print("----------------------------------------------------------\n")

        # Here we will end the game,
        # If player doesn't have lifes left to continue playing.
        if PLAYER_LIFE == 0:
            GAME_IS_ENDED = True
            print("You lost the Game and killed innocent person! life - (0)")
    except ValueError:
        print("\nPLEASE ENTER ONLY INTEGER NUMBERS!\n")
