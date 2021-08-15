dir2 = 0

def on_forever():
    global dir2
    dir2 = input.compass_heading()
    if dir2 < 5 or dir2 > 355:
        basic.show_string("N")
        music.ring_tone(784)
    elif input.button_is_pressed(Button.A):
        basic.show_number(dir2)
    else:
        basic.clear_screen()
        music.ring_tone(0)
basic.forever(on_forever)
