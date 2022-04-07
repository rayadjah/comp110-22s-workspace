"""A list utility functions."""

__author__ = "730397634."


def only_evens(integers: list[int]) -> list[int]:
    """Returns a list of integers containing only even elements."""
    guess: list[int] = list()
    for item in integers:
        if item % 2 == 0:
            guess.append(item)
    return guess


def sub(name_of_integers: list[int], start_index: int, end_index: int) -> list[int]:
    """Returns a subset of the given list."""
    given_list: list[int] = list()

    if start_index < 0:
        start_index = 0
    if end_index > len(name_of_integers):
        end_index = len(name_of_integers)
    if len(name_of_integers) == 0 or start_index > len(name_of_integers) or end_index <= 0:
        return given_list

    while start_index < end_index:
        given_list.append(name_of_integers[start_index])
        start_index += 1
    return given_list


def concat(first_list: list[int], second_list: list[int]) -> list[int]:
    """Generates a new list that contains all the elements of the first two lists."""
    combined_list: list[int] = list()
    for item in first_list:
        # print(item)
        combined_list.append(item)
    for item in second_list:
        combined_list.append(item)
    return combined_list
