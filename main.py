class LabirintTurtle:
    def __init__(self):
        self.map = []
        self.exit = None
        self.turtle = None
        self.path = []

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
                    print(self.map[i][j], end='\t')
                print()

        # if turtle is false
        else:
            for i in range(len(self.map)):
                for j in range(len(self.map[i])):
                    if self.map[i][j] != chr(128034):
                        print(self.map[i][j], end='\t')
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
                        self.exit = [i, j]
                if self.map[i][j] != ' ' and self.map[i][j] != '*' and self.map[i][j] != chr(128034):
                    return None

        # check if turtle is in a wall
        if self.map[pos_x][pos_y] == '*':
            return None

        # check if there is an exit
        if self.exit is None:
            return None
        # check if turtle can get to the exit
        while pos_x != self.exit[0] or pos_y != self.exit[1]:
            self.path.append([pos_x, pos_y])
            if pos_x > self.exit[0] and self.map[pos_x - 1][pos_y] == ' ':
                pos_x -= 1
            elif pos_x < self.exit[0] and self.map[pos_x + 1][pos_y] == ' ':
                pos_x += 1
            elif pos_y > self.exit[1] and self.map[pos_x][pos_y - 1] == ' ':
                pos_y -= 1
            elif pos_y < self.exit[1] and self.map[pos_x][pos_y + 1] == ' ':
                pos_y += 1
            else:
                break
        # check if turtle is in the exit
        if pos_x != self.exit[0] or pos_y != self.exit[1]:
            self.path = []
            return None
        self.path.append(self.exit)
        return 'OK'

    def exit_count_step(self):
        count = 1
        pos_x = self.turtle[0]
        pos_y = self.turtle[1]
        # move position of turtle until it is in the exit
        while pos_x != self.exit[0] or pos_y != self.exit[1]:
            if pos_x > self.exit[0] and self.map[pos_x - 1][pos_y] == ' ':
                pos_x -= 1
                count += 1
            if pos_x < self.exit[0] and self.map[pos_x + 1][pos_y] == ' ':
                pos_x += 1
                count += 1
            if pos_y > self.exit[1] and self.map[pos_x][pos_y - 1] == ' ':
                pos_y -= 1
                count += 1
            if pos_y < self.exit[1] and self.map[pos_x][pos_y + 1] == ' ':
                pos_y += 1
                count += 1
        return count

    def exit_show_step(self):
        # make steps
        for positions in self.path:
            self.map[positions[0]][positions[1]] = chr(128062)
        self.show_map()


lab = LabirintTurtle()
lab.load_map('2.txt')
lab.show_map(turtle=True)
print(lab.exit_count_step())
lab.exit_show_step()
