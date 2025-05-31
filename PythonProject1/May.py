class Animal:
    def __init__(self, name):
        self.name = name

    def bring_destruction(self):
        print(f'{self.name} что-то сломал!')


class Dog(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)

    def make_sueta(self):
        print(f'{self.name} играет с диваном')


class Cat(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)

    def make_sueta(self):
        print(f'{self.name} тыгыдыкает в 5 утра по лицу')


dog = Dog('Барбос')
cat = Cat('Елкалаз')


class BattleshipGame:
    def __init__(self):
        self.size = 10
        self.ships = 15

    # Это функция расстановки кораблей, она уже полностью написана
    def place_ships_randomly(self, field, num_ships):
        for _ in range(num_ships):
            placed = False
            while not placed:
                coords = (random.randint(0, self.size - 1), random.randint(0, self.size - 1))
                if self.is_valid_ship_placement(field, coords):
                    field.grid[coords[0]][coords[1]] = "S"
                    placed = True

    # Это функция проверки расстановки кораблей, она уже полностью написана
    def is_valid_ship_placement(self, field, coords, ship_length=1, ):
        x, y = coords

        # Проверка на наличие соседних клеток по горизонтали и вертикали
        for i in range(ship_length + 2):
            for j in range(-1, 2):
                for k in range(-1, 2):
                    new_x, new_y = x + j, y + k
                    if 0 <= new_x < self.size and 0 <= new_y < self.size and field.grid[new_x][new_y] == "S":
                        return False

        return True

    def play(self):
        print("Расстановка кораблей компьютера:")

        print("Ваша расстановка кораблей:")