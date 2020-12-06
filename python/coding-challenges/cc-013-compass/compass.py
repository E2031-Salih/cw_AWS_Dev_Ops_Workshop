def final_direction(start, directions):
    compass = ["N", "E", "S", "W"]
    first = compass.index(start)
    total_turn = 0
    for i in directions:
        if i == "R":
            total_turn += 1
        else:
            total_turn -= 1
    print(compass[(first + total_turn)%4])

final_direction("N", ["L", "L", "L"])
final_direction("N", ["R", "R", "R", "L"])
final_direction("N", ["R", "R", "R", "R"])
final_direction("N", ["R", "L"])