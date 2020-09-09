# 1
def show_messages(messages):
    """Takes a list of messages and displays each message."""
    print(f"Here is a list with the messages:")
    for message in messages:
        print(message)


def send_messages(messages, messages_sent):
    """Each sent message is print and move to a new list"""
    print("\nList with messages sent.")
    while messages:
        current_message = messages.pop()
        print(f"Sending message: {current_message}")
        messages_sent.append(current_message)


messages_list = ["Hello World", "I am learning Python", "I want to be a"
                 " machine learning engineer"]
sent_messages = []
show_messages(messages_list)
send_messages(messages_list[:], sent_messages)
# We sent a copy, here is the original.
print(f"\n{messages_list}")

