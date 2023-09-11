
from random import randint
from enum import Enum


SALARY_VALUE = 200000
INTIAL_CASH_VALUE = 200000


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    BLACK = 4
    WHITE = 5
    YELLOW = 6
    
class DiceResult():
    dice1: int
    dice2: int
    def __init__(self):
        self.dice1 = randint(1,6)
        self.dice2 = randint(1,6)
    
    def sum(self) -> int:
        return self.dice1 + self.dice2


# Chance and Community
# pt: Sorte ou revez 

class ChanceAndCommunityType(Enum):
    CHANCE = 1
    COMMUNITY = 2
    HABEAS_CORPUS = 3
    
class ChanceAndCommunityCard:
    type: ChanceAndCommunityType
    value: int
    text: str
    
class ChanceAndCommunityDeck:
    cards: list
    
    def append(self, card: ChanceAndCommunityCard):
      self.cards.append(card)
    
    # draw a card from the pile  
    def draw(self, card: ChanceAndCommunityCard):
      return self.cards.pop(0)
  

class Player:
    
    def __init__(self, 
                 player_name: str, 
                 player_color: Color, 
                 cash: int = INTIAL_CASH_VALUE):
        self.color = player_color
        self.name = player_name
        self.cash = cash
        self.assets = []
        self.position = 0
        

    def pay(self, value: int) -> int:
        self.cash = self.cash - value
        
        return self.cash 
        
    def receive(self, value: int) -> int:
        self.cash = self.cash + value
        return self.cash
    
    def get_position(self) -> int:
        return self.position 
    
    def set_position(self, p: int):
        self.position = p
    
    def get_salary(self):
        self.receive(SALARY_VALUE)
        
    def __eq__(self, other) -> bool:
         if not isinstance(other, Player):
             return False
         return (self.name == other.name) | (self.color == other.color)
        
        
        
class PlayerCollection():
    items: list
    
    def __init__(self):
        self.items = []
    
    def append(self, p: Player):
        for item in self.items:
            if item == p:
                raise ValueError("players must be unique")
        self.items.append(p)
        
    def get_list(self):
        return(self.items)

# Porperties

class Asset():
    name: str
    buying_value: int
    owner: Player
    
    def get_owner(self):
        return self.owner
    
    def set_owner(self, p: Player):
        self.owner = p

    # set as avaliable to buy
    def clear_owner(self, p: Player):
        self.owner = None
        
    def get_buying_value(self):
        return self.buying_value
    
    def __init__(self):
        self.clear_owner()
        
    

class Property(Asset):
    rent_value: int
    house_rent_value: int
    hotel_ret_value: int
    shopping_rent_value: int
    house_contruct_cost: int
    hotel_contruct_cost: int
    shopping_contruct_cost: int
    
class Industry(Asset):
    dice_multiplier: int


            
class SpecialStep(Enum):
    START = 1
    CHANCE_COMMUNITY = 2
    JAIL = 3
    GOTO_JAIL = 4
    FORCE_CONSTRUCTION = 5
    FREE_PARKING = 6

class StepCollection:
    items: list
    
    def __init__(self):
        self.items = []

    # Append a asset        
    def append(self, item: Asset):
        self.items.append(item)
    
    # Append a special step 
    def append(self, item: SpecialStep):
        self.items.append(item)
    
    def advance(self, p: Player):
        dr = DiceResult()
        position = p.get_position() + dr.sum()
        while (position > self.items.count):
            position = position - self.items.count
            p.get_salary()
        
        current_step = self.items(position)
        
        if isinstance(current_step, Asset):
            pass
            # TODO
        
        if isinstance(current_step, SpecialStep):
            if current_step in SpecialStep.START:
                # Nothing to do the salary logic is implemented above
                pass
            elif current_step in SpecialStep.CHANCE_COMMUNITY:
                pass
                # TODO
            elif current_step in SpecialStep.JAIL:
                pass
            elif current_step in SpecialStep.GOTO_JAIL:
                pass
                # TODO
            elif current_step in SpecialStep.FORCE_CONSTRUCTION:
                pass
                # TODO
            elif current_step in SpecialStep.FREE_PARKING:
                # do nothing
                pass
            else:
                raise ValueError("Special step undefined")   

        
        p.set_position(position)
        
        

# Interface - implementação rudimentar


class PlayerInterface:
    def message(self, player_name: str, m: str):
        pass
    
    def create_player() ->Player:
        pass
    
class PlayerInterfaceTerminal(PlayerInterface):
    
    def __init__(self):
        pass
    
    def message(self, m: str):
        print(m)
        
    
    def create_player(self) ->Player:
        confirm = False
        while (not confirm):
            player_color = None
            player_name = ""
            while(not player_name):
                player_name = input("Nome do jogador: ")
            cores = {'1': ['Vermelho', Color.RED], 
                    '2': ['Azul', Color.BLUE],
                    '3': ['Preto', Color.BLACK],
                    '4': ['Amarelo', Color.YELLOW],
                    '5': ['Branco', Color.WHITE],
                    }
            for k,v in cores.items():
                print (f'{k} - {v[0]}')
            
            while(not player_color):
                choice = input("Escolha a cor: ")
                if choice in cores:
                    player_color = cores[choice][1]
                else:
                    print("Digite apenas o numero")
            conf = input ("Confirma?").upper()
            if conf[0] in ('S', 'Y'):
                confirm = True
        return Player(player_name, player_color)
    
class PlayerSession:    
    def __init__(self, pcol: PlayerCollection, i: PlayerInterface, player: Player = None):
        current_player = player
        while(True):
            try:
                if (current_player == None):
                    self.player = i.create_player()
                else:
                    self.player = p
                self.interface = i
                pcol.append(self.player)
                break
            except ValueError:
                current_player = None
                i.message("Jogador inválido, favor entrar novamente")
            
            
    def get_player(self)->Player:
        return self.player
    
    

   
            
            
if __name__ == "__main__":
    
    interface = PlayerInterfaceTerminal()
    p_col = PlayerCollection()
    
    s1 = PlayerSession(p_col, interface)
    s2 = PlayerSession(p_col, interface)
    
        
