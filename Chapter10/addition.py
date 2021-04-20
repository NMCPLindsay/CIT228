

isRunning=True

while isRunning == True:
    try:
        num1=int(input("Please enter a number."))
        num2=int(input("Please enter another number."))

        print(f"{num1}+{num2}={(num1)+(num2)}")
    except ValueError:
        print("One of your values is not a number. please try again.")
        # num1=int(input("Please enter a number."))
        # num2=int(input("Please enter another number."))

        # print(f"{num1}+{num2}={(num1)+(num2)}")
    answer= input("Press 'q' to quit or enter to continue.")
    if answer=="q":
        isRunning = False
    else:
        isRunning = True