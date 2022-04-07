"""A list utility functions."""

__author__ = "730397634."

from utils import only_evens, sub, concat


def test_only_evens_some_odds() -> None:
    """Tests against a list containing odd integers."""
    xs: list[int] = [1, 2, 3, 4, 5, 6]
    assert only_evens(xs) == [2, 4, 6]


def test_only_evens_all_odds() -> None:
    """Tests against a list of only odd integers."""
    xs: list[int] = [1, 3, 5, 7]
    assert only_evens(xs) == []


def test_only_evens_empty() -> None:
    """Tests against an empty list."""
    xs: list[int] = []
    assert only_evens(xs) == []


def test_sub_whole_list() -> None:
    """Subsets the whole list."""
    xs: list[int] = [1, 2, 3, 4, 5]
    assert sub(xs, 0, 5) == [1, 2, 3, 4, 5]


def test_sub_three() -> None:
    """Subsets the first three values."""
    xs: list[int] = [1, 2, 3, 4, 5]
    assert sub(xs, 0, 3) == [1, 2, 3]


def test_sub_invalid_start_end() -> None:
    """Given invalid starting and ending inputs, subset the whole list."""
    xs: list[int] = [1, 2, 3, 4, 5]
    assert sub(xs, -1, 8) == [1, 2, 3, 4, 5]


def test_concat_same_length() -> None:
    """Concatenates two lists of the same length."""
    xs: list[int] = [1, 2, 3]
    xl: list[int] = [4, 5, 6]
    assert concat(xs, xl) == [1, 2, 3, 4, 5, 6]


def test_concat_diff_length() -> None:
    """Concatenates two lists of different lengths."""
    xs: list[int] = [1]
    xl: list[int] = [2, 3, 4]
    assert concat(xs, xl) == [1, 2, 3, 4]


def test_concat_empty_list() -> None:
    """Concatenates an empty list onto a non-empty list."""
    xs: list[int] = []
    xl: list[int] = [1, 2, 3]
    assert concat(xs, xl) == [1, 2, 3]
