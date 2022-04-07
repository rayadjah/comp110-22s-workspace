from __future__ import annotations


class StaArray:
    items: list[str]

    def __init__(self, items):
        self.items = items

    def __repr__(self) -> str:
        return f"StrArray({self.items})"


first: StaArray = StaArray(["Armando", "Brady", "Caleb"])
last: StaArray = StaArray(["Bacot", "Manek", "Love"])