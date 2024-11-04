from gamestate import *
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

        # self.gamestate: gamestate.Gamestate = gamestate.new_default_board()
        self.palette: palette.Palette = palette.default_palette(BOX_SIZE)
        self.set_game_state(new_default_board())
 
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for tile, rect in self.tile_rects.items():
                if (rect.collidepoint(event.pos)):
                    print(f'Clicked {tile}')
                    self.set_game_state(take_action(self.gamestate, tile))
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

    def set_game_state(self, gamestate: Gamestate):
        if gamestate is None:
            return

        self.tile_rects = {}
        self.tile_surfs = {}
        for x in range(gamestate.width()):
            for y in range(gamestate.height()):
                tile_surface = self.palette.get_surface(gamestate.board[x][y])
                if tile_surface is not None:
                    self.tile_rects[Coord(x, y)] = tile_surface.get_rect(topleft=(x * BOX_SIZE, y * BOX_SIZE))
                    self.tile_surfs[Coord(x, y)] = tile_surface
        self.gamestate = gamestate
    
    def draw_game_board(self) -> None:
        # draw tiles
        for rect, surf in zip(self.tile_rects.values(), self.tile_surfs.values()):
            self._display_surf.blit(surf, rect)

        # draw current selection
        coord = self.gamestate.selection
        if coord is not None:
            pygame.draw.rect(self._display_surf, SELECTION_OUTLINE_COLOR, self.tile_rects[coord], 4)
            
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()

