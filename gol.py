from itertools import product
from functools import lru_cache


class GameOfLife(object):
    ruleset = {
        'stay_alive': (2, 3),
        'breed': (3,),
    }

    generations_count = 0

    def __init__(self, state=[]):
        self.set_state(state)

    def set_state(self, state):
        self.current_state = set(state)

    def get_neighbour_count(self, x, y):
        count = 0
        for neighbour in self.get_neighbours(x, y):
            if neighbour == (x, y):
                continue
            if neighbour in self.current_state:
                count += 1
        return count

    def is_alive(self, x, y):
        return (x, y) in self.current_state

    @lru_cache(maxsize=64)
    def get_new_state(self, x, y):
        count = self.get_neighbour_count(x, y)
        alive = (x, y) in self.current_state
        return (
            alive and count in self.ruleset['stay_alive']
            or not alive and count in self.ruleset['breed']
        )

    def get_neighbours(self, x, y):
        return (
            point for point in product(
                range(x - 1, x + 2),
                range(y - 1, y + 2)
            ) if point != (x, y)
        )

    def next_state(self):
        self.get_new_state.cache_clear()
        state = set()
        for point in self.current_state:
            if self.get_new_state(*point):
                state.add(point)
            for neighbour in self.get_neighbours(*point):
                if self.get_new_state(*neighbour):
                    state.add(neighbour)
        self.current_state = state
        self.generations_count += 1
        return state


def print_state(gol, start, end):
    for i in range(start[0], end[0] + 1):
        line = ""
        for j in range(start[1], end[1] + 1):
            if (i, j) in gol.current_state:
                line += '#'
            else:
                line += ' '
        print(line)

if __name__ == '__main__':
    START, END = (-1, -1), (5, 5)
    gol = GameOfLife(set([
        (0, 2),
        (1, 2),
        (1, 3),
        (2, 3),
        (1, 1)
    ]))
    print('-1:')
    print_state(gol, START, END)
    for i in range(5):
        print('%d:' % i)
        gol.next_state()
        print_state(gol, START, END)
