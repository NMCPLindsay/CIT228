print("-------------------------------")
print("Exercise 1")
name="phil lindsay"
print(name.title())
print(name.upper())
print(name.lower())
print("My first initial is: ", name[0].upper())

print("-------------------------------")
print("Exercise 2")
noun="driver"
adj="angry"
verb="yelled"
end="at pedestrians"
sentence1="the " + adj +" " + noun + " " + verb + " " + end
sentence2=f"the {adj} {noun} {verb} {end}"
print(sentence1.upper())
print(sentence2.lower())

print("-------------------------------")
print("Exercise 3")
longString= """Hey diddle diddle,
the cat and the fiddle,
the cow jumped over the moon."""
print(longString)

print("-------------------------------")
print("Exercise 4")
title1="Darkside"
title2="Lightside"
string1="Darth Vader"
string2="Luke Skywalker"
string3="Revan"
string4="Ahsoka Tano"
print(title1,"\t\t\t",title2,"\n")
print(string1,"\t\t\t",string2)
print(string3,"\t\t\t\t",string4,"\n")

print("-------------------------------")
print("Exercise 5")
import random
number1=random.randrange(1,100)
number2=random.randrange(1,100)
print("number 1 = ",number1,"\tnumber 2 = ",number2)
print(number1,"/",number2,"=",float(number1/number2))
print(number1,"//",number2,"=",float(number1//number2))
print(number1,"%",number2,"=",float(number1%number2))
print(number1,"+",number2,"=",float(number1+number2))
print(number1,"-",number2,"=",float(number1-number2))
print(number1,"*",number2,"=",float(number1*number2))
NUMBER2=25
number2=NUMBER2
print("number 1 = ",number1,"\tnumber 2 = ",number2)
print(number1,"/",number2,"=",float(number1/number2))
print(number1,"//",number2,"=",float(number1//number2))
print(number1,"%",number2,"=",float(number1%number2))
print(number1,"+",number2,"=",float(number1+number2))
print(number1,"-",number2,"=",float(number1-number2))
print(number1,"*",number2,"=",float(number1*number2))