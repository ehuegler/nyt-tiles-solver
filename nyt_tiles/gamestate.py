import util
from random import Random
from dataclasses import dataclass

@dataclass
class Coord:
    x: int
    y: int

    def __eq__(self, value: object) -> bool:
        return type(value) is Coord \
            and self.x == value.x \
            and self.y == value.y
    
    def __hash__(self) -> int:
        return hash((self.x, self.y))

#TODO is it correct to store combo in the state if that is the reward?
@dataclass
class Gamestate:
    board: list[list[list[int]]]
    selection: Coord = None
    combo: int = 0
    
    def width(self):
        return len(self.board)
    
    def height(self):
        return len(self.board[0])

    def layers(self):
        return len(self.board[0][0])

def init_game(width: int, height: int, layers: list[int], seed: int = None ):
    rng: Random = Random(seed)

    layer_count: int = len(layers)

    game_board: list[list[list]] = [[[None for _ in range(layer_count)] for _ in range(height)] for _ in range(width)]

    for layer_idx, varieties in enumerate(layers):
        coordinates: list[Coord] = [ Coord(x, y) for x in range(width) for y in range(height)]
        while (len(coordinates) > 0):
            pattern = rng.randint(0, varieties - 1)
            for _ in range(2):
                tile: Coord = util.pop_random(coordinates, rng) 
                game_board[tile.x][tile.y][layer_idx] = pattern

    return Gamestate(game_board)

def new_default_board():
    return init_game(5, 6, [5, 5, 5])

def take_action(gamestate: Gamestate, action: Coord):
    #TODO check if action is valid?
    if gamestate.selection == action or is_empty(gamestate.board, action):
        print("1")
        return gamestate    
    elif gamestate.selection is None:
        print("2")
        return Gamestate(gamestate.board, action, gamestate.combo)
    else:
        print("3")
        new_board = copy_board(gamestate.board)
        from_tile = new_board[gamestate.selection.x][gamestate.selection.y]
        to_tile = new_board[action.x][action.y]

        simmilarity = 0
        for i, (a, b) in enumerate(zip(from_tile, to_tile)):
            if a == b:
                simmilarity += 1
                from_tile[i] = None
                to_tile[i] = None

        if simmilarity == 0:
            return None #TODO losing game state
        
        if is_empty(new_board, action):
            action = None

        return Gamestate(new_board, action, gamestate.combo + 1)
    
def is_empty(board, coord: Coord) -> bool:
    for layer in board[coord.x][coord.y]:
        if layer is not None:
            return False
    return True

def copy_board(board):
    x = len(board)
    y = len(board[0])
    l = len(board[0][0])
    return [[[board[i][j][k] for k in range(l)] for j in range(y)] for i in range(x)]