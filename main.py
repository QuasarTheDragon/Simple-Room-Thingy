cmd = ""

def next_room_finder(current_room):
    if current_room == 'a':
        next_room = 'b'
        visual = """
                                    -------
                                    |     |
                                    |  f  |
                                    -------
                    ------- ------- -------
                    |     | |     | |     |
                    |  c  | |  d  | |  e  |
                    ------- ------- -------
                    -------
                    |     |
                    | YOU |
                    -------
                    -------
                    |     |
                    |  a  |
                    -------
                    """
        return next_room, visual
    elif current_room == 'b':
        next_room = 'c'
        visual = """
                                    -------
                                    |     |
                                    |  f  |
                                    -------
                    ------- ------- -------
                    |     | |     | |     |
                    | YOU | |  d  | |  e  |
                    ------- ------- -------
                    -------
                    |     |
                    |  b  |
                    -------
                    -------
                    |     |
                    |  a  |
                    -------
                    """
        return next_room, visual
    elif current_room == 'c':
        next_room = 'd'
        visual = """
                                    -------
                                    |     |
                                    |  f  |
                                    -------
                    ------- ------- -------
                    |     | |     | |     |
                    |  c  | | YOU | |  e  |
                    ------- ------- -------
                    -------
                    |     |
                    |  b  |
                    -------
                    -------
                    |     |
                    |  a  |
                    -------
                    """
        return next_room, visual
    elif current_room == 'd':
        next_room = 'e'
        visual = """
                                    -------
                                    |     |
                                    |  f  |
                                    -------
                    ------- ------- -------
                    |     | |     | |     |
                    |  c  | |  d  | | YOU |
                    ------- ------- -------
                    -------
                    |     |
                    |  b  |
                    -------
                    -------
                    |     |
                    |  a  |
                    -------
                    """
        return next_room, visual
    elif current_room == 'e':
        next_room = 'f'
        visual = """
                                    -------
                                    |     |
                                    | YOU |
                                    -------
                    ------- ------- -------
                    |     | |     | |     |
                    |  c  | |  d  | |  e  |
                    ------- ------- -------
                    -------
                    |     |
                    |  b  |
                    -------
                    -------
                    |     |
                    |  a  |
                    -------
                    """
        return next_room, visual
    else:
        print('Not a valid room')

def previous_room_finder(current_room):
    if current_room == 'f':
        previous_room = 'e'
        visual = """
                                            -------
                                            |     |
                                            |  f  |
                                            -------
                            ------- ------- -------
                            |     | |     | |     |
                            |  c  | |  d  | | YOU |
                            ------- ------- -------
                            -------
                            |     |
                            |  b  |
                            -------
                            -------
                            |     |
                            |  a  |
                            -------
                            """
        return previous_room, visual
    elif current_room == 'e':
        previous_room = 'd'
        visual = """
                                            -------
                                            |     |
                                            |  f  |
                                            -------
                            ------- ------- -------
                            |     | |     | |     |
                            |  c  | | YOU | |  e  |
                            ------- ------- -------
                            -------
                            |     |
                            |  b  |
                            -------
                            -------
                            |     |
                            |  a  |
                            -------
                            """
        return previous_room, visual
    elif current_room == 'd':
        previous_room = 'c'
        visual = """
                                            -------
                                            |     |
                                            |  f  |
                                            -------
                            ------- ------- -------
                            |     | |     | |     |
                            | YOU | |  d  | |  e  |
                            ------- ------- -------
                            -------
                            |     |
                            |  b  |
                            -------
                            -------
                            |     |
                            |  a  |
                            -------
                            """
        return previous_room, visual
    elif current_room == 'c':
        previous_room = 'b'
        visual = """
                                            -------
                                            |     |
                                            |  f  |
                                            -------
                            ------- ------- -------
                            |     | |     | |     |
                            |  c  | |  d  | |  e  |
                            ------- ------- -------
                            -------
                            |     |
                            | YOU |
                            -------
                            -------
                            |     |
                            |  a  |
                            -------
                            """
        return previous_room, visual
    elif current_room == 'b':
        previous_room = 'a'
        visual = """
                                            -------
                                            |     |
                                            |  f  |
                                            -------
                            ------- ------- -------
                            |     | |     | |     |
                            |  c  | |  d  | |  e  |
                            ------- ------- -------
                            -------
                            |     |
                            |  b  |
                            -------
                            -------
                            |     |
                            | YOU |
                            -------
                            """
        return previous_room, visual
    else:
        print('Not a valid room')

room = {
    'a': {
        'up': True,
        'down': False,
        'right': False,
        'left': False
    },
    'b': {
        'up': True,
        'down': True,
        'right': False,
        'left': False
    },
    'c': {
        'up': False,
        'down': True,
        'right': True,
        'left': False
    },
    'd': {
        'up': False,
        'down': False,
        'right': True,
        'left': True
    },
    'e': {
        'up': True,
        'down': False,
        'right': False,
        'left': True
    },
    'f': {
        'up': False,
        'down': True,
        'right': False,
        'left': False
    }
}

current_room = 'a'

print("""
                                -------
                                |     |
                                |  f  |
                                -------
                ------- ------- -------
                |     | |     | |     |
                |  c  | |  d  | |  e  |
                ------- ------- -------
                -------
                |     |
                |  b  |
                -------
                -------
                |     |
                | YOU |
                -------
                """)

while True:

    up = room.get(current_room)['up']
    down = room.get(current_room)['down']
    left = room.get(current_room)['left']
    right = room.get(current_room)['right']



    cmd = input("> ")
    if 'end' in cmd:
        print('thanks for playing c:')
        break
    elif 'up' in cmd:
        if up:
            print('Went up one tile!')
            plus, visual = next_room_finder(current_room)
            print(visual)
            current_room = plus
        else:
            print("There's a wall blocking the way!")
    elif 'down' in cmd:
        if down:
            print('Went down one tile!')
            minus, visual = previous_room_finder(current_room)
            print(visual)
            current_room = minus
        else:
            print("There's a wall blocking the way!")
    elif 'right' in cmd:
        if right:
            print('Went right one tile!')
            plus, visual = next_room_finder(current_room)
            print(visual)
            current_room = plus
        else:
            print("There's a wall blocking the way!")
    elif 'left' in cmd:
        if left:
            print('Went left one tile!')
            minus, visual = previous_room_finder(current_room)
            print(visual)
            current_room = minus
        else:
            print("There's a wall blocking the way!")
    elif 'check':
        print(f"You're currently on room {current_room}")
    else:
        print("I don't understand.")