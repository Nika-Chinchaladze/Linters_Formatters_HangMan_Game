"""pictures module represents Hang-man game stages graphically. It contains GameArt class, that is able to 
return concrete stage based on 'stage_index' parameter with 'return_stage' method and 
game logo by using 'return-logo' method.
"""

GAME_STAGES = {
"7": """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
""",
"6": """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
"5": """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
"4": """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
"3": """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
"2": """
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
"1": """
  +---+
  |   |
      |
      |
      |
      |
=========
""",
"logo": """ 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/
""",
}


class GameArt:
    """class object has access to HangMan game-stages."""

    def __init__(self):
        # Here we are using private attribute, because this attribute must be accessed only
        # Inside this class, and mustn't be available from outside or not from child class.
        self.__game_stage = GAME_STAGES
    
    def return_stage(self, stage_index: str):
        """returns HangMan game's concrete stage by using 'stage_index' parameter,
        that must be provided as a string.
        """
        allowed_indexes = ["1", "2", "3", "4", "5", "6", "7"]
        # here we are trying to avoid IndexError Exception without using try-except clause.
        if stage_index in allowed_indexes:
            return self.__game_stage[stage_index]
        return "Empty String"
    
    def return_logo(self):
        """returns HangMan game logo."""
        return self.__game_stage["logo"]