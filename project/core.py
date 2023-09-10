
from random import randint
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    BLACK = 4
    
class DiceResult():
    dice1: int
    dice2: int
    __init__():
        dice1 = randint(1,6)
        dice2 = randint(1,6)

class Step:
    number: int    
    land(self, Player p, dr: DiceResult):
        None 

class Asset(Step):
    name: str
    buying_value: int

class Industry(Asset):
    dice_multiplier: int
    land(self, Player p, dr: DiceResult):
        p.pay(dr.dice1 * dr.dice2)
    
class Property(Asset):
    ret_value: int
    house_rent_value: int
    shopping_rent_value: int
    land(self, Player p, dr: DiceResult):

    
    
class StepCollection:
    l: Step[]
    

class Player:
    color: Color
    cash: int
    __init__(self, player_color: Color, cash: int):
        self.color = player_color
        self.cash - cash
        
    pay(self, value: int):
        self.cash = self.cash - value
        
    receive(self, value: int):
        self.cash = self.cash + value
         
            