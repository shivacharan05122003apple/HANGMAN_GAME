

from django.db import models


class game:
    name: str
    error:bool
    clue:str
    answer: str
    guess:str
    limit:int
    count : int
    display: str
    word: str
    win:bool
    already_guessed:str
    length: int
    play_game: str