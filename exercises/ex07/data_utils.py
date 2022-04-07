"""Dictionary related utility functions."""

__author__ = "730397634"

from csv import DictReader

# Define your functions below


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read CSV rows in."""
    result: list[dict[str, str]] = []

    file_handle = open(filename, "r", encoding="utf8")

    csv_reader = DictReader(file_handle)

    for row in csv_reader:
        result.append(row)

    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Return all values of a particular column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Make a row-oriented table column-oriented."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]

    for column in first_row:
        result[column] = column_values(row_table, column)
    
    return result


def head(nonMutate: dict[str, list[str]], size: int) -> dict[str, list[str]]:
    """Returns only a certain number of rows."""
    result: dict[str, list[str]] = {}
    
    for column in nonMutate:
        temp: list[str] = []
        i: int = 0

        if size > len(nonMutate[column]):
            size = len(nonMutate[column])

        while i < size:
            temp.append(nonMutate[column][i])
            i += 1
        
        result[column] = temp
    
    return result


def select(nonMutate: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Produces a column based table with only a specific subset of the original column."""
    newdict: dict[str, list[str]] = {}

    for column in names:
        for column2 in nonMutate:
            if column == column2:
                newdict[column2] = nonMutate[column]
    return newdict


def concat(table1: dict[str, list[str]], table2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produces a column based table with two column based tables combined."""
    newdict: dict[str, list[str]] = {}

    for column in table1:
        newdict[column] = table1[column]

    for column2 in table2:
        if column2 in newdict:
            newdict[column2] += table2[column2]
        else:
            newdict[column2] = table2[column2]
 
    return newdict