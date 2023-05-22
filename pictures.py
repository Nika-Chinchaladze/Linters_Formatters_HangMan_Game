"""Pictures module represents Hang-man game stages graphically. 
It contains GameArt class, that is able to return concrete stage 
based on 'stage_index' parameter with 'return_stage'
method and game logo by using 'return-logo' method.
"""

# pylint: disable=anomalous-backslash-in-string

FIRST = """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
"""

SECOND = """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
"""

THIRD = """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
"""

FOURTH = """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
"""

FIFTH = """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
"""

SIXTH = """
  +---+
  |   |
  O   |
      |
      |
      |
=========
"""

SEVENTH = """
  +---+
  |   |
      |
      |
      |
      |
=========
"""

LOGO = """
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/
"""

GAME_STAGES = {
    "1": FIRST,
    "2": SECOND,
    "3": THIRD,
    "4": FOURTH,
    "5": FIFTH,
    "6": SIXTH,
    "7": SEVENTH,
    "logo": LOGO,
}


class GameArt:
    """class object has access to HangMan game-stages."""

    def __init__(self):
        # Here we are using private attribute,
        # Because this attribute must be available only
        # Inside this class, and mustn't be available
        # From outside or not from any child class.
        self.__game_stage = GAME_STAGES

    def return_stage(self, stage_index: str):
        """returns HangMan game's concrete stage by using 'stage_index'
        parameter, that must be provided as a string.
        """
        allowed_indexes = ["1", "2", "3", "4", "5", "6", "7"]
        # Here we are trying to avoid IndexError Exception
        # With if-else condition, without using try-except clause.
        if stage_index in allowed_indexes:
            return self.__game_stage[stage_index]
        return "Empty String"

    def return_logo(self):
        """returns HangMan game logo."""
        return self.__game_stage["logo"]
