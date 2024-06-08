class Chess:
    num = 0

    def __init__(self):  # y⇒
        self.desk = [[8, 2, 7, 6, 5, 7, 2, 8],  # x⇓
                     [1, 1, 1, 1, 1, 1, 1, 1],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [-1, -1, -1, -1, -1, -1, -1, -1],
                     [-8, -2, -7, -6, -5, -7, -2, -8]]

    def __repr__(self):
        result = ""
        for i in range(len(self.desk)):
            for elem in self.desk[i]:
                result += f"{str(elem)} "
            result += "\n"
        return result

    def definition(self):
        self.num
        self.num += 1
        print(f'<<<{self.num}>>>')
        if self.num % 2 == 0:
            return True
        else:
            return False

    def move(self, x1, y1, x2, y2):
        if abs(self.desk[x1][y1]) == 1:
            self.pawn(x1, y1, x2, y2)
        elif abs(self.desk[x1][y1]) == 2:
            self.horse(x1, y1, x2, y2)
        elif abs(self.desk[x1][y1]) == 5:
            self.king(x1, y1, x2, y2)
        elif abs(self.desk[x1][y1]) == 6:
            self.queen(x1, y1, x2, y2)
        elif abs(self.desk[x1][y1]) == 7:
            self.elephant(x1, y1, x2, y2)
        elif abs(self.desk[x1][y1]) == 8:
            self.rook(x1, y1, x2, y2)
        else:
            print("тут пусто")

    # Проверка наличия помехи по диагоналям
    def exam45(self, x1, y1, x2, y2):
        if x1 < x2 and y1 < y2:
            while x1 < x2 and y1 < y2:
                x1 += 1
                y1 += 1
                if self.desk[x1][y1] != 0:
                    return False
            return True
        elif x1 > x2 and y1 > y2:
            while x1 > x2 and y1 > y2:
                x1 -= 1
                y1 -= 1
                if self.desk[x1][y1] != 0:
                    return False
            return True
        elif x1 > x2 and y1 < y2:
            while x1 > x2 and y1 < y2:
                x1 -= 1
                y1 += 1
                if self.desk[x1][y1] != 0:
                    return False
            return True
        elif x1 < x2 and y1 > y2:
            while x1 < x2 and y1 > y2:
                x1 += 1
                y1 -= 1
                if self.desk[x1][y1] != 0:
                    return False
            return True

    # Проверка наличия помехи по вертикали и горизонтали
    def exam90(self, x1, y1, x2, y2):
        if x1 == x2 and y1 < y2:
            while y1 < y2:
                y1 += 1
                if self.desk[x1][y1] != 0:
                    return False
            return True
        elif x1 == x2 and y1 > y2:
            while y1 > y2:
                y1 -= 1
                if self.desk[x1][y1] != 0:
                    return False
            return True
        elif x1 < x2 and y1 == y2:
            while x1 < x2:
                x1 += 1
                if self.desk[x1][y1] != 0:
                    return False
            return True
        elif x1 > x2 and y1 == y2:
            while x1 > x2:
                x1 -= 1
                if self.desk[x1][y1] != 0:
                    return False
            return True

    # ЛОШАДЬ 2
    def horse(self, x1, y1, x2, y2):
        player_move = self.definition()
        side = self.desk[x1][y1]
        if side > 0:
            sd = 1
        elif side < 0:
            sd = -1
        if ((self.desk[x2][y2] >= 0 and sd == -1 and player_move in True)
           or (self.desk[x2][y2] <= 0 and sd == 1 and player_move in False)):
            if ((abs((x1-x2) * sd) == 1 and abs((y1-y2) * sd) == 2)
               or (abs((x1-x2) * sd) == 2 and abs((y1-y2) * sd) == 1)):
                self.desk[x2][y2] = self.desk[x1][y1]
                self.desk[x1][y1] = 0

    # КОРОЛЬ 5
    def king(self, x1, y1, x2, y2):
        player_move = self.definition()
        side = self.desk[x1][y1]
        if side > 0:
            sd = 1
        elif side < 0:
            sd = -1
        if ((self.desk[x2][y2] >= 0 and sd == -1 and player_move in True)
           or (self.desk[x2][y2] <= 0 and sd == 1 and player_move in False)):
            if abs((x1-x2) * sd) <= 1 and abs((y1-y2) * sd) <= 1:
                self.desk[x2][y2] = self.desk[x1][y1]
                self.desk[x1][y1] = 0

    # ФЕРЗЬ 6
    def queen(self, x1, y1, x2, y2):
        player_move = self.definition()
        if x1 == x2 or y1 == y2:
            move = self.exam90(x1, y1, x2, y2)
        else:
            move = self.exam45(x1, y1, x2, y2)
        if move in True:
            side = self.desk[x1][y1]
            if side > 0:
                sd = 1
            elif side < 0:
                sd = -1
            if ((self.desk[x2][y2] >= 0 and sd == -1 and player_move in True)
               or (self.desk[x2][y2] <= 0 and sd == 1 and player_move in False)):
                if (abs((x1-x2) * sd) == abs((y1-y2) * sd)
                   or x1 == x2 or y1 == y2):
                    self.desk[x2][y2] = self.desk[x1][y1]
                    self.desk[x1][y1] = 0
        else:
            print("Есть преграда на пути")

    # ЛАДЬЯ 8
    def rook(self, x1, y1, x2, y2):
        player_move = self.definition()
        if self.exam90(x1, y1, x2, y2) in True:
            side = self.desk[x1][y1]
            if side > 0:
                sd = 1
            elif side < 0:
                sd = -1
            if ((self.desk[x2][y2] >= 0 and sd == -1 and player_move in True)
               or (self.desk[x2][y2] <= 0 and sd == 1 and player_move in False)):
                if x1 == x2 or y1 == y2:
                    self.desk[x2][y2] = self.desk[x1][y1]
                    self.desk[x1][y1] = 0
        else:
            print("Есть преграда на пути")

    # СЛОН 7
    def elephant(self, x1, y1, x2, y2):
        player_move = self.definition()
        if self.exam45(x1, y1, x2, y2) in True:
            side = self.desk[x1][y1]
            if side > 0:
                sd = 1
            elif side < 0:
                sd = -1
            if ((self.desk[x2][y2] >= 0 and sd == -1 and player_move in True)
               or (self.desk[x2][y2] <= 0 and sd == 1 and player_move in False)):
                if abs((x1 - x2) * sd) == abs((y1 - y2) * sd):
                    self.desk[x2][y2] = self.desk[x1][y1]
                    self.desk[x1][y1] = 0
        else:
            print("Есть преграда на пути")

    # ПЕШКА 1
    def pawn(self, x1, y1, x2, y2):
        player_move = self.definition()
        side = self.desk[x1][y1]
        if ((self.desk[x2][y2] > 0 and side == -1 and player_move in True)
           or (self.desk[x2][y2] < 0 and side == 1 and player_move in False)):
            if y1 + 1 == y2 or y1 - 1 == y2:
                self.desk[x2][y2] = self.desk[x1][y1]
                self.desk[x1][y1] = 0
                if x2 == 7 or x2 == 0:
                    upgrade = int(input('2 or 7 or 8: '))
                    self.desk[x2][y2] = upgrade * side
        if ((x1 == 1 and side == 1 and player_move in True)
           or (x1 == 6 and side == -1 and player_move in False)):
            if x1 + (2 * side) == x2:
                self.desk[x2][y2] = self.desk[x1][y1]
                self.desk[x1][y1] = 0
            if x1 + (1 * side) == x2 and y1 == y2 and self.desk[x2][y2] == 0:
                self.desk[x2][y2] = self.desk[x1][y1]
                self.desk[x1][y1] = 0
                if x2 == 7 or x2 == 0:
                    upgrade = int(input('2 or 7 or 8: '))
                    if upgrade == 2 or upgrade == 7 or upgrade == 8:
                        self.desk[x2][y2] = upgrade * side
                    else:
                        print("Авиоматически выбор")
                        self.desk[x2][y2] = 8 * side


a = Chess()
print(a.definition())
print(a)
while True:
    qord = input("Введите ход: ").split()
    print(' ')
    if len(qord) == 0:
        break
    elif len(qord) != 4:
        print("неправильное количество символов ")
    else:
        a.move(int(qord[0]), int(qord[1]), int(qord[2]), int(qord[3]))
        print(a)
