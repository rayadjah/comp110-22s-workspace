"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730397634"
x = input("Enter a 5-character word: ")
p = input("Enter a single character: ")
if len(x) != 5:
    print("Error: Word must contain 5 characters")
    exit()
if len(p) != 1:
    print("Error: Character must be a single character")
    exit()
else:
    print("Searching for " + p + " in " + x)
count: int = 0
if x[0] == p:
    count += 1
    print(p + " found at index 0")
if x[1] == p:
    count += 1
    print(p + " found at index 1")
if x[2] == p:
    count += 1
    print(p + " found at index 2")
if x[3] == p:
    count += 1
    print(p + " found at index 3")
if x[4] == p:
    count += 1
    print(p + " found at index 4")
if count > 1:
    print(str(count) + " instances of " + p + " found in " + x)
elif count == 0:
    print("No instances of " + p + " found in " + x)
else:
    print(str(count) + " instance of " + p + " found in " + x)