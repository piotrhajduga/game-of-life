from gol import GameOfLife
import cProfile

gol = GameOfLife([
    (1, 1), (1, 2), (1, -2), (2, 1), (2, 0), (1, 0), (0, 0),
    (4, 5), (4, 4), (5, 5),
    (100, -15), (101, -16), (103, -15), (100, -16),
])


def next_state():
    for _ in range(200):
        gol.next_state()

cProfile.run('next_state()')

print(gol.get_new_state.cache_info())
