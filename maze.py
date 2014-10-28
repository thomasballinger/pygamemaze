from random import choice


def make_maze(width, height):
    return [[choice([True, False, True, True]) for _ in range(width)] for _ in range(height)]


def display_maze(maze):
    for row in maze:
        print ''.join('  ' if x else 'XX' for x in row)


class Solver(object):
    def __init__(self, maze, start, stop):
        self.current = start
        self.maze = maze
        self.stop = stop
        self.visited = set([start])
        self.need_to_visit = []

    @property
    def width(self):
        return len(self.maze[0])

    @property
    def height(self):
        return len(self.maze)

    def update(self):
        self.need_to_visit.extend([spot
            for spot in self.accessible_neighbors(*self.current)
            if spot not in self.visited])
        print 'current need to visit list:', self.need_to_visit
        print 'visited:', self.visited
        while self.current in self.visited:
            self.current = self.need_to_visit.pop(0)
        self.visited.add(self.current)

    def accessible_neighbors(self, x, y):
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        return [(newx, newy) for newx, newy in
                [(x + dx, y + dy) for dx, dy in directions]
                if 0 <= newy < len(self.maze) and 0 <= newx < len(self.maze[0])
                    and self.maze[newy][newx]]

    def __str__(self):
        copy = [['  ' if x else 'XX' for x in row] for row in self.maze]
        copy[self.current[1]][self.current[0]] = 'ME'
        return '\n'.join(''.join(row) for row in copy)

