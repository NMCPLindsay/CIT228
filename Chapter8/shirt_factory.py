def make_shirt(size, message):
    if size=="Large":
        message="I love Python."
    
    print(f"You ordered a {size} shirt with the message '{message}' printed on it.")

make_shirt('XXL','PC>Console')
make_shirt(size='Small',message='Console>PC')
make_shirt('Large', 'I hate Python.')