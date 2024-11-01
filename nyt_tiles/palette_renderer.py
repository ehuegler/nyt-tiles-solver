import palette
import pygame
from abc import ABC, abstractmethod

class PaletteRenderer(ABC):
    @abstractmethod
    def get_texture(self, tile:list) -> pygame.Surface:
        pass

    @abstractmethod
    def get_palette(self) -> palette.Palette:
        pass

class DefaultPaletteRenderer(PaletteRenderer):
    def __init__(self, box_size: int) -> None:
        self.box_size: int = box_size
        self.background_colors = [
            pygame.Color(0, 0, 0),
            pygame.Color(255, 0, 0),
            pygame.Color(0, 255, 0),
            pygame.Color(0, 0, 255),
            pygame.Color(255, 255, 255),
        ]
        self.texture_map: list[list[pygame.Surface]] = self.init_texture_map()
        super().__init__()

    def get_palette(self) -> palette.Palette:
        return palette.default_palette

    def get_texture(self, tile: list) -> pygame.Surface:
        surface = pygame.Surface((self.box_size, self.box_size))
        for layer_num, layer_idx  in enumerate(tile):
            if layer_idx is not None:
                # find a way to add self.texture_map[layer_num][layer_idx]
                layer_surface = self.texture_map[layer_num][layer_idx]
                layer_rect = layer_surface.get_rect(center=(self.box_size / 2, self.box_size / 2))
                surface.blit(layer_surface, layer_rect.topleft)
                
        return surface

    def init_texture_map(self) -> list[list[pygame.Surface]]:
        return [
            [solid_rect(self.box_size, color) for color in self.background_colors],
            [solid_rect(self.box_size / 2, color) for color in self.background_colors],
            [solid_rect(self.box_size / 4, color) for color in self.background_colors],
        ]

def solid_rect(box_size: int, color: pygame.Color) -> pygame.Surface:
    surface = pygame.Surface((box_size, box_size))
    surface.fill(color)
    return surface