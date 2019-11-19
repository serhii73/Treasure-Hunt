import pytest
from src.treasure_hunt_class import Solver


def test_initial_solver():
    """Test initial class."""
    list_5x5 = [
        [11, 22, 33, 44, 55],
        [11, 22, 33, 44, 55],
        [11, 22, 33, 44, 55],
        [11, 22, 33, 44, 55],
        [11, 22, 33, 44, 55],
    ]
    solver = Solver(list_5x5)
    assert solver.treasure_found == False
    assert solver.path == [11]
    assert solver.list_5x5 == list_5x5
    assert solver.position == [0, 0]


@pytest.mark.parametrize(
    "list_5x5,expected",
    [
        (
            [
                [11, 22, 33, 44, 55],
                [11, 22, 33, 44, 55],
                [11, 22, 33, 44, 55],
                [11, 22, 33, 44, 55],
                [11, 22, 33, 44, 55],
            ],
            True,
        ),
        (
            [
                [55, 14, 25, 52, 21],
                [44, 31, 11, 53, 43],
                [24, 13, 45, 12, 34],
                [42, 22, 43, 32, 41],
                [51, 23, 33, 54, 15],
            ],
            False,
        ),
    ],
)
def test_solver_done(list_5x5, expected):
    """Test solver has done or not."""
    solver = Solver(list_5x5)
    assert solver.done() == expected


def test_solver_jump():
    """Test jump to a new position."""
    list_5x5 = [
        [55, 14, 25, 52, 15],
        [44, 31, 11, 53, 43],
        [24, 13, 45, 12, 34],
        [42, 22, 43, 32, 41],
        [51, 23, 33, 54, 15],
    ]
    solver = Solver(list_5x5)
    assert solver.position == [0, 0]
    assert solver.path == [11]
    assert solver.done() == False

    solver.jump()

    assert solver.position == [4, 4]
    assert solver.path == [11, 55]
    assert solver.treasure_found == False
    assert solver.done() == False

    solver.jump()

    assert solver.position == [0, 4]
    assert solver.path == [11, 55, 15]
    assert solver.done() == True


def test_not_exist_treasure():
    """Test not exist treasure."""
    list_5x5 = [
        [42, 33, 22, 54, 34],
        [35, 31, 43, 13, 51],
        [53, 12, 32, 52, 55],
        [25, 44, 41, 11, 45],
        [21, 15, 24, 14, 23],
    ]
    solver = Solver(list_5x5)
    for i in range(25):
        if not solver.done():
            solver.jump()
    assert solver.treasure_found == False
