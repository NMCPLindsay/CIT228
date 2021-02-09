print("=================6-3================")
dictionary={
    "Term":"Dictionary",
    "Definition":"Python dictionaries are used to store data in key:value pairs."
}
keyValuePair={
    "Term":"Key:Value Pair",
    "Definition":"The defining elements in a dictionary."
}
key={
    "Term":"Key",
    "Definition":"The unique identifier that holds a value in a dictionary."
}
value={
    "Term":"Value",
    "Definition":"The variable held by the key in a dictionary."
}
syntax={
    "Term":"Syntax",
    "Definition":"The format in which the code is written to function properly."
}
function={
    "Term":"Function",
    "Definition":"A call to a method that returns a value after operations are performed."
}
listDef={
    "Term":"List",
    "Definition":"A set of variables that can be used to loop through and return all or specific values."
}
tupleDef={
    "Term":"Tuple",
    "Definition":"Like a List but cannot be altered."
}
forLoop={
    "Term":"For-Loop",
    "Definition":"A way to run through a loop with a list value to display or perform searches through list items."
}
integer={
    "Term":"Integer",
    "Definition":"A whole positive or negative number that operations can be performed on."
}
List=[dictionary,keyValuePair,key,value,syntax,function,listDef,tupleDef,forLoop,integer]

for l in List:
    print(f"{l['Term']}: \n\t -{l['Definition']}")