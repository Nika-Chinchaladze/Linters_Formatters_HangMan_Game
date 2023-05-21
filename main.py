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
boundaries_is_defined_correctly = False
while not boundaries_is_defined_correctly:
    try:
        low_num = int(input("Please define the lowest number: "))
        high_num = int(input("Please define the highest number: "))
        random_number = generate_random_number(num1=low_num, num2=high_num)
        boundaries_is_defined_correctly = True
    except ValueError:
        print("\nPLEASE ENTER ONLY INTEGER NUMBERS!\n")


# Here we start playing game to guess - generated random number.
player_life = 7
game_is_ended = False
while not game_is_ended:
    # Here we check, if player provides number.
    # If user provides string that can't be converted into number,
    # Then we will repeat the asking process.
    try:
        user_guess = int(input(f"Guess the Number between {low_num} and {high_num}: "))
        # If player guess the correct number, then game ends immediately.
        if user_guess == random_number:
            print(f"You won the Game and saved innocent person! life - ({player_life})")
            game_is_ended = True
        else:
            # Here we dispay result of wrong answer and dicrease player_life by one.
            print(game_art.return_stage(stage_index=str(player_life)))
            player_life -= 1

            # Here we should tell user if his/her answer is lower
            # Or higher than chosen random number:
            feedback = "Lower" if user_guess < random_number else "Higher"
            contrary = "Lower" if feedback == "Higher" else "Higher"
            print(
                f"Your answer ({user_guess}) is {feedback} than desired random number!"
            )
            print(f"Try {contrary}! life - ({player_life})")

            # Here we print cross - border line between previous and next stages:
            print("----------------------------------------------------------\n")

        # Here we will end the game,
        # If player doesn't have lifes left to continue playing.
        if player_life == 0:
            game_is_ended = True
            print("You lost the Game and killed innocent person! life - (0)")
    except ValueError:
        print("\nPLEASE ENTER ONLY INTEGER NUMBERS!\n")
