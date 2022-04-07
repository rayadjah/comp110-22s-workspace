"""A place to implement the fuctions skeletons."""

__author__ = "730397634"


def invert(firstDict: dict[str, str]) -> dict[str, str]:
    """Reverses the keys and values of a dictionary."""
    inverted = {}

    for key in firstDict:
        if firstDict[key] in inverted:
            raise KeyError("That key already exists")
        else:
            inverted[firstDict[key]] = key

    return inverted


def favorite_color(colors: dict[str, str]) -> str:
    """Identifies the most popular color."""
    counter: dict[str, int] = {}
    maxCount = 0
    mostPopular = ''
    for name in colors:
        if colors[name] in counter:
            counter[colors[name]] += 1
        else:
            counter[colors[name]] = 1

    for color in counter:
        maxCount = max(maxCount, counter[color])
    
    for color in counter:
        if counter[color] == maxCount:
            mostPopular = color
            break
    
    return mostPopular


def count(values: list[str]) -> dict[str, int]:
    """Counts all the times that each value occurs in a list."""
    counter: dict[str, int] = {}

    for value in values:
        if value in counter:
            counter[value] += 1
        else:
            counter[value] = 1
    
    return counter
    