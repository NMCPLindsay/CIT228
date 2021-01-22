print("----------Hands on 2-----------")
import random
number=random.randrange(10,100)
numList=list(range(number))
print(numList)
print("The largest number: ",len(numList)-1)
print("The smallest number: ",min(numList))
print("The sum of all numbers: ",sum(numList))
print("The average number: ",sum(numList)/len(numList))
