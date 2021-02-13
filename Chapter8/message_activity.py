def show_messages(message_list):
    for m in message_list:
        print(m)
def send_message(message):
    sent_messages=[]
    sent_messages.append(message)
    
    
    print(f"Messages sent:\n {sent_messages}")
def send_message2(message, archive):
    sent_messages=[]
    sent_messages.append(message)
    archive.remove(message)
    
    print(f"Messages sent:\n {sent_messages}")