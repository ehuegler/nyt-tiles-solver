from random import Random
import util
from palette import Palette, default_palette
from dataclasses import dataclass

@dataclass
class Coord:
    x: int
    y: int

class NytTiles:
    def __init__(self, size: Coord = Coord(5, 6), layers: int = 3, seed: int = None, palette: Palette = default_palette) -> None:
        self.rng: Random = Random()
        if seed is not None:
            self.rng.seed(seed)
            
        self.size: Coord = size
        self.layers: int = layers
        self.palette: Palette = palette

        self.current_combo: int = 0
        self.longest_combo: int = 0
        self.current_selection: tuple[int, int] = None

        self.__initialize_gameboard()


    # Get this thang going
    def __initialize_gameboard(self):
        if hasattr(self, "game_board"):
            raise Exception("Game board can only be initialized once!")
        
        self.game_board: list[list[list]] = [[[None] * self.layers] * self.size.y] * self.size.x

        for layer in range(0, self.layers):
            coordinates = [ Coord(x, y) for x in range(self.size.x) for y in range(self.size.y)]
            while (len(coordinates) > 0):
                pattern = self.palette.get_rand_pattern_for_layer(layer, self.rng)
                self._set_tile(util.pop_random(coordinates, self.rng), layer, pattern)
                self._set_tile(util.pop_random(coordinates, self.rng), layer, pattern)


    def _set_tile(self, coord: Coord, layer: int, value: int):
        self.game_board[coord.x][coord.y][layer] = value
        