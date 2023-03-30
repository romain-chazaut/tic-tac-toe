import random

def choose_random_move(button_list, window):
    empty_buttons = [button for button in button_list if button.cget("text") == "" and window.winfo_exists()]

    if empty_buttons:
        return random.choice(empty_buttons)
    return None
