class LabirintTurtle:
    def __init__(self):
        self.map = []
        self.exit = None

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
            self.map[pos_x][pos_y] = 'A'
            result = self.check_map(pos_x, pos_y)
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
                    print(self.map[i][j], end=' ')
                print()

        # if turtle is false
        else:
            for i in range(len(self.map)):
                for j in range(len(self.map[i])):
                    if self.map[i][j] != 'A':
                        print(self.map[i][j], end=' ')
                    else:
                        print(' ', end=' ')
                print()

    def check_map(self, pos_x, pos_y):
        # check if there is an exit and if there any other symbols except for * and ' '
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if i == 0 or i == -1 or j == 0 or j == -1:
                    if self.map[i][j] == ' ':
                        self.exit = [i, j]
                if self.map[i][j] != ' ' and self.map[i][j] != '*' and self.map[i][j] != 'A':
                    return None

        # check if turtle is in a wall
        if self.map[pos_x][pos_y] == '*':
            return None

        # check if there is an exit
        if self.exit is None:
            return None
        # check if turtle can get to the exit
        while pos_x != self.exit[0] or pos_y != self.exit[1]:
            if pos_x > self.exit[0] and self.map[pos_x - 1][pos_y] == ' ':
                pos_x -= 1
            if pos_x < self.exit[0] and self.map[pos_x + 1][pos_y] == ' ':
                pos_x += 1
            if pos_y > self.exit[1] and self.map[pos_x][pos_y - 1] == ' ':
                pos_y -= 1
            if pos_y < self.exit[1] and self.map[pos_x][pos_y + 1] == ' ':
                pos_y += 1
            else:
                break
        if pos_x != self.exit[0] or pos_y != self.exit[1]:
            return None
        return 'OK'


lab = LabirintTurtle()
lab.load_map('1.txt')
lab.show_map(turtle=True)
