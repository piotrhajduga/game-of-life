from itertools import product
from functools import lru_cache


class GameOfLife(object):
    ruleset = {
        'last': (2, 3),
        'breed': (3,),
    }

    def __init__(self, state):
        self.current_state = state

    @lru_cache(maxsize=8)
    def get_neighbour_count(self, x, y):
        count = 0
        for neighbour in self.get_neighbours(x, y):
            if neighbour == (x, y):
                continue
            if neighbour in self.current_state:
                count += 1
        return count

    def get_new_state(self, x, y):
        count = self.get_neighbour_count(x, y)
        alive = (x, y) in self.current_state
        return (
            alive and count in self.ruleset['last']
            or not alive and count in self.ruleset['breed']
        )

    def get_neighbours(self, x, y):
        for point in product(
            range(x - 1, x + 2),
            range(y - 1, y + 2)
        ):
            if point != (x, y):
                yield point

    def next_state(self):
        self.get_neighbour_count.cache_clear()
        result = set()
        for point in self.current_state:
            if self.get_new_state(*point):
                result.add(point)
            for neighbour in self.get_neighbours(*point):
                if neighbour in self.current_state:
                    continue
                if self.get_new_state(*neighbour):
                    result.add(neighbour)
        self.current_state = result
        return result


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
    print('-1:\n')
    print_state(gol, START, END)
    for i in range(5):
        print('%d:\n' % i)
        gol.next_state()
        print_state(gol, START, END)
