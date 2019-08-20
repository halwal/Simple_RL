import tcod as libtcod

def handle_keys(key):
    key_char = chr(key.c)
    # movement keys
    if key.vk == libtcod.KEY_UP or key.vk == libtcod.KEY_KP8 or key_char == 'k':
        return {'move' : (0, -1)}
    elif key.vk == libtcod.KEY_DOWN or key.vk == libtcod.KEY_KP2 or key_char == 'j':
        return {'move' : (0, 1)}
    elif key.vk == libtcod.KEY_LEFT or key.vk == libtcod.KEY_KP4 or key_char == 'h':
        return {'move' : (-1, 0)}
    elif key.vk == libtcod.KEY_RIGHT or key.vk == libtcod.KEY_KP6 or key_char == 'l':
        return {'move' : (1, 0)}
    elif (key.vk == libtcod.KEY_UP and key.vk == libtcod.KEY_RIGHT) or key.vk == libtcod.KEY_KP9 or key_char == 'u':
        return {'move' : (1, -1)}
    elif (key.vk == libtcod.KEY_DOWN and key.vk == libtcod.KEY_RIGHT) or key.vk == libtcod.KEY_KP3 or key_char == 'n':
        return {'move' : (1, 1)}
    elif (key.vk == libtcod.KEY_UP and key.vk == libtcod.KEY_LEFT) or key.vk == libtcod.KEY_KP7 or key_char == 'y':
        return {'move' : (-1, -1)}
    elif (key.vk == libtcod.KEY_DOWN and key.vk == libtcod.KEY_LEFT) or key.vk == libtcod.KEY_KP1 or key_char == 'b':
        return {'move' : (-1, 1)}


    if key.vk == libtcod.KEY_ENTER and key.lalt:
        #Alt+Enter: toggle fullscreen
        return {'fullscreen' : True}

    elif key.vk == libtcod.KEY_ESCAPE:
        #exit the game
        return {'exit' : True}

    #no key pressed
    return {}