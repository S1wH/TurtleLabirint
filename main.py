class LabirintTurtle:
    def __init__(self):
        self.map = []

    def load_map(self, file_name):
        file = open(file_name, 'r')
        line = file.readline()
        while line.find('*') != -1 or line.find(' ') != - 1:
            self.map.append(list(line[:-1]))
            line = file.readline()
        pos_x = int(line)
        pos_y = int(file.readline())
        self.map[pos_x][pos_y] = 'A'

    def show_map(self, turtle=None):
        if turtle is True:
            for i in range(len(self.map)):
                for j in range(len(self.map[i])):
                    print(self.map[i][j], end=' ')
                print()
        else:
            for i in range(len(self.map)):
                for j in range(len(self.map[i])):
                    if self.map[i][j] != 'A':
                        print(self.map[i][j], end=' ')
                    else:
                        print(' ', end=' ')
                print()

    def check_map(self):
        pass


lab = LabirintTurtle()
lab.load_map('1.txt')
print(lab.show_map())
print(lab.map)
