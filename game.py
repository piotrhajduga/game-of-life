import pygame
from pygame.locals import *


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
        self.dims = dims
        self.fps = fps
        self.caption = caption

        self._fps_clock = pygame.time.Clock()

    def start(self):
        pygame.init()
        pygame.display.set_caption(self.caption)

        self.window = pygame.display.set_mode(
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
                self.update()
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
        self.window = pygame.display.set_mode(
            self.dims, pygame.RESIZABLE | pygame.DOUBLEBUF
        )

    def on_quit(self, event):
        self.stop()

    def stop(self):
        raise StopGame()
