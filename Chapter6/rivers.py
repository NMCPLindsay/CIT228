print("===============6-5==============")
boardman={
    "River":"Boardman River",
    "State":"Michigan"
}
rioGrande={
    "River":"Rio Grande",
    "State":"Texas"
}
republican={
    "River":"Republican River",
    "State":"Kansas"
}
Rivers=[boardman, rioGrande, republican]
print("*****Rivers and States*****")
for r in Rivers:
    print(f"The {r['River']} flows through {r['State']}.")
print("****States****")
for r in Rivers:
    print(f"{r['State']}")
print("****Rivers****")
for r in Rivers:
    print(f"{r['River']}")