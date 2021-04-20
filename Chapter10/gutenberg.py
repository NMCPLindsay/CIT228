filenames=['Chapter10/gutenberg.txt','Chapter10/gutenberg2.txt','Chapter10/gutenberg3.txt']
# searchWord=input("What common word do you want to search for in these files?")

def find_words(filename, searchWord):
    count=0
    count2=0
    try:
        with open(filename, encoding="utf-8") as f:
            contents= f.read()
       
    except FileNotFoundError:
        print("File not found.")
    else:
        words = contents.split()
        count2 = len(words)
        count = int(contents.lower().count(searchWord.lower()))
        
        print(f"'{searchWord}' appears {count} times in the text.")
def count_words(filename):
    count=0
    count2=0
    try:
        with open(filename, encoding="utf-8") as f:
            contents= f.read()
       
    except FileNotFoundError:
        print("File not found.")
    else:
        words = contents.split()
        count2 = len(words)
      
        
        print(f"The file, {fileName} contains {count2} words.")






searchWord=input("What common word do you want to search for in these files?")
for fileName in filenames:
    count_words(fileName)
    find_words(fileName, searchWord)