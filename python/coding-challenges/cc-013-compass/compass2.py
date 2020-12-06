def final_direction(start, directions):
    compass = ["N", "E", "S", "W"]
    print(compass[(compass.index(start) + (directions.count("R") - directions.count("L")))%4])

final_direction("N", ["L", "L", "L"])
final_direction("N", ["R", "R", "R", "L"])
final_direction("N", ["R", "R", "R", "R"])
final_direction("N", ["R", "L"])