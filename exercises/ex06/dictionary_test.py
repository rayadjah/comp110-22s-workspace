"""Testing the dictionary."""

__author__ = "730397634"

from dictionary import invert, favorite_color, count


def test_invert_use1() -> None:
    """Tests invert to see if it works on a normal dictionary."""
    xs: dict[str, str] = {'Jordan': 'bulls', 'Kobe': 'lakers', 'Steph': 'warriors'}
    assert invert(xs) == {'bulls': 'Jordan', 'lakers': 'Kobe', 'warriors': 'Steph'}


def test_invert_use2() -> None:
    """Tests invert to see if it works on another normal dictionary."""
    xs: dict[str, str] = {'Messi': 'PSG', 'Goal': 'Net'}
    assert invert(xs) == {'PSG': 'Messi', 'Net': 'Goal'}


def test_invert_edge() -> None:
    """Tests invert to see if it works on an empty dictionary."""
    xs: dict[str, str] = {}
    assert invert(xs) == {}


def test_favorite_color_use1() -> None:
    """Tests favorite_color according to write-up example."""
    xs: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(xs) == "blue"


def test_favorite_color_use2() -> None:
    """Tests favorite_color against a larger dictionary."""
    xs: dict[str, str] = {"Ray": "blue", "Kenny": "green", "Eman": "blue", "Blake": "black"}
    assert favorite_color(xs) == "blue"


def test_favorite_color_edge() -> None:
    """Tests favorite_color for edge case."""
    xs: dict[str, str] = {"Ray": "blue", "Kenny": "green", "Eman": "blue", "Blake": "green"}
    assert favorite_color(xs) == "blue"


def test_count_use1() -> None:
    """Tests count on a small list."""
    xs: list[str] = ['Duke', 'UNC', 'Duke', 'UNC', 'UNC']
    assert count(xs) == {'Duke': 2, 'UNC': 3}


def test_count_use2() -> None:
    """Tests count on a longer list."""
    xs: list[str] = ['Duke', 'UNC', 'Duke', 'UNC', 'UNC', 'UNCG', 'UNCAT', 'State', 'State']
    assert count(xs) == {'Duke': 2, 'UNC': 3, 'UNCG': 1, 'UNCAT': 1, 'State': 2}


def test_count_edge() -> None:
    """Tests count on an empty list."""
    xs: list[str] = []
    assert count(xs) == {}