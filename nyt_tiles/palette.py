import pygame
from dataclasses import dataclass

@dataclass
class Palette():
    texture_map: list[list[pygame.Surface]]

    def get_surface(self, tile: list) -> pygame.Surface:
        surface: pygame.Surface = pygame.Surface((60, 60))
        surface.fill((255, 255, 255))
        surface.set_colorkey((255, 255, 255))
        for layer_num, layer_idx  in enumerate(tile):
            if layer_idx is not None:
                # find a way to add self.texture_map[layer_num][layer_idx]
                layer_surface = self.texture_map[layer_num][layer_idx]
                if surface is None:
                    surface = layer_surface
                else:
                    layer_rect = layer_surface.get_rect(center=(30, 30))
                    surface.blit(layer_surface, layer_rect.topleft)
                
        return surface

def default_palette(box_size):
    return Palette(texture_map=default_texture_map(box_size))    

def default_texture_map(box_size: int) -> list[list[pygame.Surface]]:
    colors = [
            pygame.Color(0, 0, 0),
            pygame.Color(255, 0, 0),
            pygame.Color(0, 255, 0),
            pygame.Color(0, 0, 255),
            pygame.Color(240, 240, 240),
    ]
    return squares_texture_map(box_size, colors=[colors, colors, colors])

def squares_texture_map(box_size: int, colors: list[list[pygame.Color]]):
    return [[solid_rect(box_size / 2**i, color) for color in layer] for i, layer in enumerate(colors)]

def solid_rect(box_size: int, color: pygame.Color) -> pygame.Surface:
    surface = pygame.Surface((box_size, box_size))
    surface.fill(color)
    return surface