def pour_water(jug1_capacity, jug2_capacity, target):
    jug1_current = 0
    jug2_current = 0
    jug1 = jug1_capacity
    jug2 = jug2_capacity
    path = []
    while (jug1_current != target) and (jug2_current != target):
        if jug1_current == 0:
            jug1_current = jug1
            path.append((jug1_current, jug2_current))
        elif jug1_current > 0 and jug2_current < jug2:
            pour = min(jug1_current, jug2 - jug2_current)
            jug1_current -= pour
            jug2_current += pour
            path.append((jug1_current, jug2_current))
        elif jug2_current == jug2:
            jug2_current = 0
            path.append((jug1_current, jug2_current))
        elif jug2_current > 0 and jug1_current < jug1:
            pour = min(jug2_current, jug1 - jug1_current)
            jug2_current -= pour
            jug1_current += pour
            path.append((jug1_current, jug2_current))
    return path
def main():
    jug1_capacity = int(input("Enter the capacity of Jug 1: "))
    jug2_capacity = int(input("Enter the capacity of Jug 2: "))
    target = int(input("Enter the target amount of water: "))
    print("Steps to measure {} liters of water:".format(target))
    steps = pour_water(jug1_capacity, jug2_capacity, target)
    for step in steps:
        print("Jug 1: {} liters, Jug 2: {} liters".format(step[0], step[1]))
if __name__ == "__main__":
    main()
