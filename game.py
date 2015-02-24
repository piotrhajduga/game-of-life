import pygame
from pygame.locals import (
    MOUSEBUTTONDOWN,
    MOUSEBUTTONUP,
    MOUSEMOTION,
    QUIT,
    VIDEORESIZE,
    KEYDOWN,
)


class StopGame(Exception):
    pass


class PyGame(object):
    callbacks = {
        MOUSEBUTTONDOWN: 'on_mouse_down',
        MOUSEBUTTONUP: 'on_mouse_up',
        MOUSEMOTION: 'on_mouse_move',
        QUIT: 'on_quit',
        VIDEORESIZE: 'on_resize',
        KEYDOWN: 'on_key_down',
    }

    def __init__(self, dims, caption, fps=30):
        self._dims = dims
        self.fps = fps
        self.caption = caption
        self.screen = None
        self._fps_clock = pygame.time.Clock()

    @property
    def dims(self):
        try:
            return self.screen.get_size()
        except AttributeError:
            return self._dims

    def start(self):
        pygame.init()
        pygame.display.set_caption(self.caption)

        self.screen = pygame.display.set_mode(
            self.dims, pygame.RESIZABLE | pygame.DOUBLEBUF
        )

        try:
            self.init()
            while True:
                for event in pygame.event.get():
                    try:
                        callback = getattr(
                            self, self.callbacks[event.type], lambda e: None)
                        callback(event)
                    except KeyError:
                        pass
                self.surface = pygame.Surface(self.screen.get_size())
                self.update()
                self.screen.blit(self.surface, (0, 0))
                pygame.display.flip()
                self._fps_clock.tick(self.fps)
        except StopGame:
            pass

    def init(self):
        pass

    def update(self):
        pass

    def on_resize(self, event):
        self.dims = event.size
        self.screen = pygame.display.set_mode(
            self.dims, pygame.RESIZABLE | pygame.DOUBLEBUF
        )

    def on_quit(self, event):
        self.stop()

    def stop(self):
        raise StopGame()
