"""in main module we have main logic of the HangMan game, from where user is able to play.
"""

from random_number import generate_random_number
from pictures import GameArt

game_art = GameArt()
print(game_art.return_logo())

# Here user will define lowest and highest boundaries for random number.
# User must provide Integer number, in other case game won't go onto another stage.
boundaries_is_defined_correctly = False
while not boundaries_is_defined_correctly:
    try:
        lowest_number = int(input("Please define the lowest number: "))
        highest_number = int(input("Please define the highest number: "))
        random_number = generate_random_number(first=lowest_number, second=highest_number)
        boundaries_is_defined_correctly = True
    except ValueError:
        print("\nPLEASE ENTER ONLY INTEGER NUMBERS!\n")


# here we start playing game to guess - generated random number.
player_life = 7
game_is_ended = False
while not game_is_ended:
    user_guess = int(input(f"Guess the Correct Number between {lowest_number} and {highest_number}: "))
    # if player guess the correct number, then game ends immediately.
    if user_guess == random_number:
        print("Congratulations, You won the Game and save innocent life!")
        game_is_ended = True
    else:
        # here we dispay result of wrong answer and dicrease player_life by one.
        print(game_art.return_stage(stage_index=str(player_life)))
        player_life -= 1

        # here we should tell user if his/her answer is lower or higher than chosen random number:
        feedback = "Lower" if user_guess < random_number else "Higher"
        contrary = "Lower" if feedback == "Higher" else "Higher"
        print(f"Your answer ({user_guess}) is {feedback} than desired random number! Try {contrary}!")
    
        # here we print cross - border line between previous and next stages:
        print("----------------------------------------------------------\n")
    
    # here we will end the game, if player doesn't have lifes left to continue playing.
    if player_life == 0:
        game_is_ended = True
        print("Unfortunately, you lost the Game and kill innocent life!")
