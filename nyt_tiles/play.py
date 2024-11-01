from nyt_tiles import NytTiles
import palette_renderer
import pygame
from pygame.locals import *

BOX_SIZE = 60
 
class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.palette_renderer = palette_renderer.DefaultPaletteRenderer(BOX_SIZE)
        self.game: NytTiles = NytTiles(palette = self.palette_renderer.get_palette())
        self.size = self.weight, self.height = self.game.size.x * BOX_SIZE + 200, self.game.size.y * BOX_SIZE + 200
 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
 
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
    def on_loop(self):
        pass
    def on_render(self):
        self.draw_game_board()
        pygame.display.flip()
        pass
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()
    
    def draw_game_board(self) -> None:
        for x in range(self.game.size.x):
            for y in range(self.game.size.y):
                tile_surface = self.palette_renderer.get_texture(self.game.game_board[x][y])
                self._display_surf.blit(tile_surface, (x * BOX_SIZE, y * BOX_SIZE))
                pygame.draw.rect( self._display_surf,
                                 (0, 255, 0),
                                 pygame.Rect( x * BOX_SIZE, y * BOX_SIZE, BOX_SIZE, BOX_SIZE ),
                                 2)
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()

