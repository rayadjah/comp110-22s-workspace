"""Tests for the sum fuction."""


from lessons.sum import sum


def test_sum_empty() -> None:
    xs: list[float] = []
    assert sum(xs) == 0.0


def test_sum_single_item() -> None:
    xs: list[float] = [220.0]
    assert sum(xs) == 220.0


def test_sum_many_items() -> None:
    xs: list[float] = [1.0, 3.0, 5.0]
    assert sum(xs) == 9.0