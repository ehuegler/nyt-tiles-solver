from random import Random

class Palette:
    def __init__(self, layer_sizes: tuple) -> None:
        for item in layer_sizes:
            if item <= 0:
                raise Exception("Layer sizes must all be positive")

        self.layers = layer_sizes.count
        self.layer_sizes = layer_sizes

    def get_rand_pattern_for_layer(self, layer:int, rng: Random) -> int:
        return rng.randint(0, self.layer_sizes[layer])

default_palette = Palette((5, 5, 5))
    