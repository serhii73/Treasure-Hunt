"""Treasure hunt squared 5x5 with OOP."""


def create_list_5x5():
    """Create squared 5x5 - list of lists."""
    list_5x5 = [[] for i in range(5)]

    for i in range(5):
        input_string = input()
        input_split = input_string.split()
        input_split = [int(i) for i in input_split]
        for position in range(5):
            list_5x5[i].append(input_split[position])
    return list_5x5


class Solver:
    """Class for searching treasure hunt squared 5x5."""

    treasure_found = False
    path = [11]

    def __init__(self, list_5x5, position):
        """Initial Solver class."""
        self.list_5x5 = list_5x5
        self.position = position

    def done(self):
        """Found treasure hunt or not."""
        if (self.position[0] + 1) * 10 + (self.position[1] + 1) == self.list_5x5[
            self.position[0]
        ][self.position[1]]:
            self.treasure_found = True
            return True
        return False

    def jump(self):
        """Jump to new position on squared 5x5."""
        num = self.list_5x5[self.position[0]][self.position[1]]
        self.path.append(num)
        self.position = [i - 1 for i in list(map(int, str(num)))]


def main():
    """Create list of lists and search treasure there."""
    list_5x5 = create_list_5x5()
    solver = Solver(list_5x5, [0, 0])

    for i in range(25):
        if not solver.done():
            solver.jump()

    if solver.treasure_found:
        print(*solver.path)
    else:
        print("Treasure not exist")


if __name__ == "__main__":
    main()
