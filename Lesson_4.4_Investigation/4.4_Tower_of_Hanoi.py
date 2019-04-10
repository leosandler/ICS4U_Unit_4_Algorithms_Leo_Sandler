# STEP ONE:
# Top ring must be moved to column 3 if odd number of rings.
# Top ring must be moved to column 2 if even number of rings.

# STEP TWO:
# Next largest piece goes into the empty space. Either 2 or 3 depending on choice above.

# STEP THREE:
# Smallest piece is stacked on top of the second smallest.

# STEP FOUR:
# Third largest piece is moved into the third slot.

# STEP FIVE:
# Smallest piece is moved to the empty space(or space with the larger piece).
# Second smallest piece is moved onto larger piece
# Smallest piece is moved onto the top of tower.


# IF STATEMENT: If one column is empty and the smallest piece is is alone, move smallest piece to top
listy = []
listy2 = []
listy3 = []
tower_list = [listy] + [listy2] + [listy3]

while True:
    value = int(input("How many rings: "))
    if value >= 3:
        break
ordered_list = []

for x in range(1, value + 1):
    tower_list[0].insert(0, x)  # Creating a list of rings(according to height, decreasing)
    ordered_list.append(x)

if value % 2 == 0:  # Checking if number of rings is odd.
    print(tower_list)
    tower_list[1].insert(0, tower_list[0][int(len(tower_list[0]) - 1)])  # Moving to the second stack, according to
    # steps above.
    del tower_list[0][int(len(tower_list[0]) - 1)]
    tower_list[2].insert(0, tower_list[0][int(len(tower_list[0]) - 1)])
    del tower_list[0][int(len(tower_list[0]) - 1)]


if value % 2 != 0:  # Checking if even.
    print(tower_list)
    tower_list[2].insert(0, tower_list[0][int(len(tower_list[0]) - 1)])  # Moving to the third stack, according to the
    # steps above.
    del tower_list[0][int(len(tower_list[0]) - 1)]
    tower_list[1].insert(0, tower_list[0][int(len(tower_list[0]) - 1)])
    del tower_list[0][int(len(tower_list[0]) - 1)]
    print(tower_list)
    tower_list[2].insert(0, tower_list[1][0])
    del tower_list[1][0]
    print(tower_list)
    tower_list[1].insert(0, tower_list[0][0])
    del tower_list[0][0]
    print(tower_list)
    tower_list[0].insert(0, tower_list[2][0])
    del tower_list[2][0]
    print(tower_list)
    tower_list[0].insert(1, tower_list[2][0])
    del tower_list[2][0]
    print(tower_list)
    tower_list[2].insert(0, tower_list[1][0])
    del tower_list[1][0]
    print(tower_list)
    tower_list[1].insert(0, tower_list[0][1])
    del tower_list[0][1]
    print(tower_list)
    tower_list[2].insert(1, tower_list[0][0])
    del tower_list[0][0]
    print(tower_list)
    tower_list[2].insert(2, tower_list[1][0])
    del tower_list[1][0]
    print(tower_list)


