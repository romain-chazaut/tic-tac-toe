import random

def choose_random_move(buttons):
    empty_buttons = [button for button in buttons if button["text"] == ""]

    if empty_buttons:
        return random.choice(empty_buttons)
    return None
