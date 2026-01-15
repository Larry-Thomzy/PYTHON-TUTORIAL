students = {
    "selim": 30,
    "sanni": 45,
    "bala": 50
}
for name,score in students.items():
    if score >=50:
        print(f"{name} passed")
    else:
        print(f"{name}failed")