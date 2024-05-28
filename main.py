tempp = 0

def on_every_interval():
    basic.show_string("Nah!")
loops.every_interval(60000, on_every_interval)

def on_forever():
    global tempp
    tempp = 30
    pins.digital_write_pin(DigitalPin.P1, 2)
    servos.P0.set_angle(90)
basic.forever(on_forever)

def on_forever2():
    music.play(music.string_playable("C5 A C C F D A E ", 122),
        music.PlaybackMode.UNTIL_DONE)
basic.forever(on_forever2)

def on_forever3():
    if input.temperature() > tempp:
        basic.show_leds("""
            . . . . .
            # . . . #
            . . . . .
            # # # # #
            # . . . #
            """)
    elif input.temperature() < tempp:
        basic.show_leds("""
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
    else:
        pass
basic.forever(on_forever3)
