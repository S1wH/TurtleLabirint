from collections import defaultdict
from termcolor import colored


def find_the_way(graph, start, goal):
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
        self.map = []
        self.exit = []
        self.turtle = None
        self.path = []

    def find_edges(self):
        edges = []
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if self.map[i][j] != '*':
                    if self.map[i][j + 1] == ' ':
                        edges.append([str(i) + ',' + str(j), str(i) + ',' + str(j + 1)])
                    if self.map[i][j - 1] == ' ':
                        edges.append([str(i) + ',' + str(j), str(i) + ',' + str(j - 1)])
                    if self.map[i + 1][j] == ' ':
                        edges.append([str(i) + ',' + str(j), str(i + 1) + ',' + str(j)])
                    if self.map[i - 1][j] == ' ':
                        edges.append([str(i) + ',' + str(j), str(i - 1) + ',' + str(j + 1)])
        graph = defaultdict(list)
        for edge in edges:
            first, second = edge[0], edge[1]
            graph[first].append(second)
            graph[second].append(first)
        for value in graph.values():
            for j in range(len(value) - 1, 0, -1):
                if value.count(value[j]) > 1:
                    value.pop(j)
        return graph

    def load_map(self, file_name):
        file = open(file_name, 'r')
        line = file.readline()
        while line.find('*') != -1 or line.find(' ') != - 1:
            self.map.append(list(line[:-1]))
            line = file.readline()

        # check if there are coordinates of turtle and check the map
        try:
            pos_x = int(line)
            pos_y = int(file.readline())
            self.map[pos_x][pos_y] = chr(128034)
            self.turtle = [pos_x, pos_y]
            result = self.check_map()
            if result is None:
                print('Введите название файла')
                file_name = input()
                self.load_map(file_name)
        except ValueError:
            print('Введите название файла')
            file_name = input()
            self.load_map(file_name)

    def show_map(self, turtle=None):
        # if turtle is True
        if turtle is True:
            for i in range(len(self.map)):
                for j in range(len(self.map[i])):
                    if self.map[i][j] != chr(128034):
                        print(colored(self.map[i][j], 'green'), end='\t')
                    else:
                        print(self.map[i][j], end='\t')
                print()

        # if turtle is false
        else:
            for i in range(len(self.map)):
                for j in range(len(self.map[i])):
                    if self.map[i][j] != chr(128034):
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
                if i == 0 or i == -1 or j == 0 or j == -1:
                    if self.map[i][j] == ' ':
                        self.exit.append([i, j])
                if self.map[i][j] != ' ' and self.map[i][j] != '*' and self.map[i][j] != chr(128034):
                    return None

        # check if turtle is in a wall
        if self.map[pos_x][pos_y] == '*':
            return None

        # check if there is an exit
        if self.exit is []:
            return None
        # check if turtle can get to the exit
        graph = self.find_edges()
        turtle = str(self.turtle[0]) + ',' + str(self.turtle[1])
        way = str(self.exit[0][0]) + ',' + str(self.exit[0][1])
        result = find_the_way(graph, turtle, way)
        if not result:
            return None
        self.path = result
        return 'OK'

    def exit_count_step(self):
        print(len(self.path))

    def exit_show_step(self):
        # make steps
        for positions in self.path:
            x, y = positions.split(',')
            self.map[int(x)][int(y)] = chr(128062)
        self.show_map()
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if self.map[i][j] == chr(128062):
                    self.map[i][j] = ' '


lab = LabirintTurtle()
lab.load_map('3.txt')
lab.show_map(turtle=True)
lab.exit_count_step()
lab.exit_show_step()
lab.show_map()
