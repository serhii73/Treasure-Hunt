"""Recursive treasure hunt squared 5x5."""


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


def create_list_with_paths(list_5x5):
    """Create a list with paths."""

    def recursion_treasure_search(list_5x5, pos=[0, 0], max_recursion=25):
        """Recursive treasure hunt squared 5x5, after each step update
        position."""
        if pos == [0, 0]:
            list_with_paths.append(11)
        if max_recursion == 0:
            list_with_paths.append("Treasure not exist")
            return False
        if (pos[0] + 1) * 10 + (pos[1] + 1) == list_5x5[pos[0]][pos[1]]:
            return True

        num = list_5x5[pos[0]][pos[1]]
        list_with_paths.append(num)
        position = [i - 1 for i in list(map(int, str(num)))]
        return recursion_treasure_search(
            list_5x5, pos=position, max_recursion=max_recursion - 1
        )

    list_with_paths = []
    recursion_treasure_search(list_5x5)
    return list_with_paths


if __name__ == "__main__":
    list_5x5 = create_list_5x5()
    list_with_paths = create_list_with_paths(list_5x5)
    if "Treasure not exist" in list_with_paths:
        print("Treasure not exist")
    else:
        print(*list_with_paths)
