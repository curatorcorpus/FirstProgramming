def middle(x, y, z):
    maximum = max(x, y, z)
    minimum = min(x, y, z)
    total = x + y + z - maximum - minimum
    return total

def island(town):
    if town == 1 or town == 2:
        return "South Island"
    elif town == 3 or town == 4:
        return "South Island"
    elif town == 5 or town == 6:
        return "North Island"
    elif town == 7 or town == 8:
        return "North Island"

#variables
christchurch = 1
Christchurch = 2
dunedin = 3
Dunedin = 4
wellington = 5
Wellington = 6
auckland = 7
Auckland = 8


