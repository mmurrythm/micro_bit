def on_forever():
  basic.show_leds("""
    # . . . #
    # . . . #
    . # # # .
    . . # . .
    . . # . .
    """)
  basic.pause(400)
  basic.show_leds("""
    . # # # .
    # . . . #
    # # # # #
    # . . . #
    # . . . #
    """)
  basic.pause(400)
  basic.show_leds("""
    . # # # .
    # . . . #
    # . # # .
    # . . . #
    . # # # .
    """)
  basic.pause(400)
basic.forever(on_forever)
