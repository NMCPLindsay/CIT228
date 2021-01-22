littleFarm=['pig','chicken','goat','cow','dog','cat']
bigFarm=littleFarm[:]
bigFarm.append('horse')
bigFarm.append('duck')
bigFarm.append('sheep')
bigFarm.append('turkey')
print("----------Little Farm-------------")
for a in littleFarm:
    print(a)
print("----------Big Farm----------------")
for a in bigFarm:
    print(a)
print("The first 3 items are: ", bigFarm[:3])
print("The middle 3 items are: ", bigFarm[4:7])
print("The last 3 items are: ", bigFarm[7:])

