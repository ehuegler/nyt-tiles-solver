import gamestate
import palette
import pygame
from pygame.locals import *

BOX_SIZE = 60
SELECTION_OUTLINE_COLOR = pygame.Color(50, 50, 50)
 
class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 800, 800
 
    def on_init(self):
        pygame.init()
        pygame.display.set_caption("NYT Tiles")
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

        self.gamestate: gamestate.Gamestate = gamestate.new_default_board()
        self.palette: palette.Palette = palette.default_palette(BOX_SIZE)
        self.tile_rects: dict = {}
 
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for tile, rect in self.tile_rects.items():
                if (rect.collidepoint(event.pos)):
                    print(f'Clicked {tile}')
                    self.gamestate = gamestate.take_action(self.gamestate, tile)
    def on_loop(self):
        pass
    def on_render(self):
        pygame.Surface.fill(self._display_surf, pygame.Color(200, 200, 200))
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
        # draw all tiles as is
        self.tile_rects = {} #TODO do something more effecient here. Only need to redraw on clicks
        for x in range(self.gamestate.width()):
            for y in range(self.gamestate.height()):
                tile_surface = self.palette.get_surface(self.gamestate.board[x][y])
                if tile_surface is not None:
                    yyy = y * BOX_SIZE
                    xxx = x * BOX_SIZE
                    self.tile_rects[gamestate.Coord(x, y)] = tile_surface.get_rect(topleft=(xxx, yyy))
                    self._display_surf.blit(tile_surface, (xxx, yyy))

        # draw current selection
        if self.gamestate.selection is not None:
            coord = self.gamestate.selection
            pygame.draw.rect(self._display_surf, 
                             SELECTION_OUTLINE_COLOR, 
                             (coord.x * BOX_SIZE, coord.y * BOX_SIZE, BOX_SIZE, BOX_SIZE),
                             4)
            pass
            
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()

