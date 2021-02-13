import random


numberCorrect=0
keepPlaying= True
anotherRound=""
while keepPlaying and anotherRound != 'q':
    probs=10
    counter=0
    while counter<probs:
        randNum1=random.randrange(1,1000)
        randNum2=random.randrange(1,1000)
        correctAns=int(randNum1+randNum2)
        yourAns=int(input(f"what is the answer to {randNum1}+{randNum2}?"))
        if correctAns==yourAns:
            print("Yay! you did it!")
            numberCorrect+=1
        
        else:
            print("Nope! WRONG! BEEEEEP! It's ", correctAns)
        
        counter+=1
        incorrect=(counter-numberCorrect)
        if incorrect >5:
            print(f"You answered {incorrect} of the last {counter} incorrect. Please review.")
            break
    print(f"You answered {numberCorrect} right.")
    if keepPlaying:
        anotherRound= input("Do you want to try again? Press 'q' to quit.")
print("Thanks for playing!")