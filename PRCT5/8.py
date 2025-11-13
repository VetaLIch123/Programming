players = [
    {"name": "Юрій", "rank": 5},
    {"name": "Сергій", "rank": 3},
    {"name": "Максим", "rank": 4}
]

by_name = sorted(players, key=lambda x: x["name"])
by_rank = sorted(players, key=lambda x: x["rank"])

print("За ім’ям:", by_name)
print("За місцем:", by_rank)
