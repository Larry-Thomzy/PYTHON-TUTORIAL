with open("students.txt", "r") as file:
    for line in file:
        parts = line.strip().split(",")
        print(parts)