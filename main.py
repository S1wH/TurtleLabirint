from termcolor import colored
import random


def find_the_way(graph, start, goal):
    # finding the way out
    explored = []
    queue = [[start]]
    if start == goal:
        return []
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in explored:
            neighbours = graph[node]
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                if neighbour == goal:
                    return new_path
            explored.append(node)
    return None


class LabirintTurtle:
    def __init__(self):
        self.graph = None
        self.map = []
        self.exits = []
        self.turtle = None
        self.paths = []
        self.side = 'N'

    def find_edges(self):
        edges = {}
        # making graph of all ways
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if self.map[i][j] != '*':
                    pos = str(i) + ',' + str(j)
                    if i == len(self.map) - 1:
                        edges[pos] = [str(i - 1) + ',' + str(j)]
                    elif i == 0:
                        edges[pos] = [str(i + 1) + ',' + str(j)]
                    elif j == len(self.map[i]) - 1:
                        edges[pos] = [str(i) + ',' + str(j - 1)]
                    elif j == 0:
                        edges[pos] = [str(i) + ',' + str(j + 1)]
                    else:
                        if self.map[i + 1][j] == ' ':
                            if pos not in edges.keys():
                                edges[pos] = [str(i + 1) + ',' + str(j)]
                            else:
                                mass = edges[pos].copy()
                                mass.append(str(i + 1) + ',' + str(j))
                                edges[pos] = mass
                        if self.map[i - 1][j] == ' ':
                            if pos not in edges.keys():
                                edges[pos] = [str(i - 1) + ',' + str(j)]
                            else:
                                mass = edges[pos].copy()
                                mass.append(str(i - 1) + ',' + str(j))
                                edges[pos] = mass
                        if self.map[i][j + 1] == ' ':
                            if pos not in edges.keys():
                                edges[pos] = [str(i) + ',' + str(j + 1)]
                            else:
                                mass = edges[pos].copy()
                                mass.append(str(i) + ',' + str(j + 1))
                                edges[pos] = mass
                        if self.map[i][j - 1] == ' ':
                            if pos not in edges.keys():
                                edges[pos] = [str(i) + ',' + str(j - 1)]
                            else:
                                mass = edges[pos].copy()
                                mass.append(str(i) + ',' + str(j - 1))
                                edges[pos] = mass
        self.graph = edges

    def load_map(self, file_name):
        file = open(file_name, 'r')
        line = file.readline()
        length = len(line) - 1
        while line.find('*') != -1 or line.find(' ') != - 1:
            self.map.append(list(line[:-1]) + (length - len(line[:-1])) * [" "])
            line = file.readline()

        # check if there are coordinates of turtle and check the map
        try:
            pos_x = int(line)
            pos_y = int(file.readline())
            self.turtle = [pos_x, pos_y]
            result = self.check_map()
            if result is None:
                file_name = input()
                self.load_map(file_name)
        except ValueError:
            print('Нет данных о месте черепахи')
            file_name = input()
            self.load_map(file_name)

    def show_map(self, turtle=None):
        # if turtle is True
        if turtle is True:
            for i in range(len(self.map)):
                for j in range(len(self.map[i])):
                    if i == self.turtle[0] and j == self.turtle[1]:
                        print(chr(128034), end='\t')
                    elif self.map[i][j] != chr(128034):
                        print(colored(self.map[i][j], 'green'), end='\t')
                    else:
                        print(self.map[i][j], end='\t')
                print()

        # if turtle is false
        else:
            for i in range(len(self.map)):
                for j in range(len(self.map[i])):
                    if self.map[i][j] == chr(128062):
                        print(self.map[i][j], end='\t')
                    elif self.map[i][j] != chr(128034):
                        print(colored(self.map[i][j], 'green'), end='\t')
                    else:
                        print(' ', end='\t')
                print()

    def check_map(self):
        pos_x = self.turtle[0]
        pos_y = self.turtle[1]

        # check if there is an exit and if there any other symbols except for * and ' '
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if i == 0 or i == len(self.map) - 1 or j == 0 or j == len(self.map[i]) - 1:
                    if self.map[i][j] == ' ':
                        self.exits.append([i, j])
                if self.map[i][j] != ' ' and self.map[i][j] != '*' and self.map[i][j] != chr(128034):
                    print('другие сиволы на карте')
                    return None

        # check if turtle is in a wall
        if self.map[pos_x][pos_y] == '*':
            print('черепаха в стене')
            return None

        # check if there is an exit
        if not self.exits:
            print('нет выхода')
            return None

        # check if turtle can get to the exit
        result = self.add_all_paths()
        if not result:
            print('черепаха не может выбраться')
            return None
        return 'OK'

    def exit_count_step(self):
        print(len(self.paths[0]))

    def exit_show_step(self, way=None):
        if way is None:
            number = random.randint(0, len(self.exits) - 1)
        else:
            number = way
        # make steps
        for positions in self.paths[number]:
            x, y = positions.split(',')
            self.map[int(x)][int(y)] = chr(128062)
        self.show_map()
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if self.map[i][j] == chr(128062):
                    self.map[i][j] = ' '

    def add_all_paths(self):
        turtle = str(self.turtle[0]) + ',' + str(self.turtle[1])
        self.find_edges()
        for way in self.exits:
            goal = str(way[0]) + ',' + str(way[1])
            path = find_the_way(self.graph, turtle, goal)
            self.paths.append(path)
        if self.paths == [None]:
            return None
        return 'OK'

    def find_the_shortest_way(self):
        length = len(self.paths[0])
        way = 0
        for i in range(len(self.paths)):
            if len(self.paths[i]) < length:
                length = len(self.paths[i])
                way = i
        print(length)
        self.exit_show_step(way)
        self.word_description(way)

    def word_description(self, way):
        way = self.paths[way]
        pos_x0, pos_y0 = self.turtle[0], self.turtle[1]
        for position in way:
            pos_x, pos_y = position.split(',')
            pos_x = int(pos_x)
            pos_y = int(pos_y)
            if pos_x > pos_x0:
                if self.side == 'N':
                    print(colored('Поворот на 180', 'magenta'))
                elif self.side == 'W':
                    print(colored('Поворот налево', 'magenta'))
                elif self.side == 'E':
                    print(colored('Поворот направо', 'magenta'))
                print(colored('Вперед', 'magenta'))
                self.side = 'S'
            elif pos_x < pos_x0:
                if self.side == 'S':
                    print(colored('Поворот на 180', 'magenta'))
                elif self.side == 'W':
                    print(colored('Поворот направо', 'magenta'))
                elif self.side == 'E':
                    print(colored('Поворот налево', 'magenta'))
                print(colored('Вперед', 'magenta'))
                self.side = 'N'
            elif pos_y > pos_y0:
                if self.side == 'W':
                    print(colored('Поворот на 180', 'magenta'))
                elif self.side == 'N':
                    print(colored('Поворот направо', 'magenta'))
                elif self.side == 'S':
                    print(colored('Поворот налево', 'magenta'))
                print(colored('Вперед', 'magenta'))
                self.side = 'E'
            elif pos_y < pos_y0:
                if self.side == 'E':
                    print(colored('Поворот на 180', 'magenta'))
                elif self.side == 'N':
                    print(colored('Поворот налево', 'magenta'))
                elif self.side == 'S':
                    print(colored('Поворт направо', 'magenta'))
                print(colored('Вперед', 'magenta'))
                self.side = 'W'
            pos_x0, pos_y0 = pos_x, pos_y


lab = LabirintTurtle()
lab.load_map('3.txt')
lab.find_the_shortest_way()
