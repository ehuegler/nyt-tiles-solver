import gamestate
import palette
import pygame
from pygame.locals import *

BOX_SIZE = 60
 
class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 800, 800
 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

        self.game_state: gamestate.Gamestate = gamestate.new_default_board()
        self.palette: palette.Palette = palette.default_palette(BOX_SIZE)
 
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
        for x in range(self.game_state.width()):
            for y in range(self.game_state.height()):
                tile_surface = self.palette.get_surface(self.game_state.board[x][y])
                self._display_surf.blit(tile_surface, (x * BOX_SIZE, y * BOX_SIZE))
                pass
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()

