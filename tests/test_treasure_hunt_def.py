import pytest
from src.treasure_hunt_def import create_list_with_paths


@pytest.mark.parametrize(
    "list_5x5,expected",
    [
        (
            [
                [34, 21, 32, 41, 25],
                [14, 42, 43, 14, 31],
                [54, 45, 52, 42, 23],
                [33, 15, 51, 31, 35],
                [21, 52, 33, 13, 23],
            ],
            [
                11,
                34,
                42,
                15,
                25,
                31,
                54,
                13,
                32,
                45,
                35,
                23,
                43,
                51,
                21,
                14,
                41,
                33,
                52,
            ],
        ),
        (
            [
                [55, 14, 25, 52, 21],
                [44, 31, 11, 53, 43],
                [24, 13, 45, 12, 34],
                [42, 22, 43, 32, 41],
                [51, 23, 33, 54, 15],
            ],
            [11, 55, 15, 21, 44, 32, 13, 25, 43],
        ),
        (
            [
                [11, 14, 25, 52, 21],
                [44, 31, 11, 53, 43],
                [24, 13, 45, 12, 34],
                [42, 22, 43, 32, 41],
                [51, 23, 33, 54, 15],
            ],
            [11],
        ),
    ],
)
def test_solver_done(list_5x5, expected):
    """Test if treasure exist."""
    assert create_list_with_paths(list_5x5) == expected


@pytest.mark.parametrize(
    "list_5x5,expected",
    [
        (
            [
                [42, 33, 22, 54, 34],
                [35, 31, 43, 13, 51],
                [53, 12, 32, 52, 55],
                [25, 44, 41, 11, 45],
                [21, 15, 24, 14, 23],
            ],
            "Treasure not exist",
        ),
        (
            [
                [42, 33, 22, 54, 34],
                [35, 31, 43, 13, 51],
                [53, 12, 32, 52, 55],
                [25, 11, 41, 11, 45],
                [21, 15, 24, 14, 23],
            ],
            "Treasure not exist",
        ),
    ],
)
def test_treasure_not_exist(list_5x5, expected):
    """Test if treasure not exist."""
    assert expected in create_list_with_paths(list_5x5)


@pytest.mark.parametrize(
    "strings", [("a"), ("B"),],
)
def test_valueerror(strings):
    """Test ValueError."""
    with pytest.raises(ValueError):
        create_list_with_paths(strings)


@pytest.mark.parametrize(
    "strings", [(1), (22),],
)
def test_typeerror(strings):
    """Test TypeError."""
    with pytest.raises(TypeError):
        create_list_with_paths(strings)
