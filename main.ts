let tempp = 0
loops.everyInterval(60000, function on_every_interval() {
    basic.showString("Nah!")
})
basic.forever(function on_forever() {
    
    tempp = 30
    pins.digitalWritePin(DigitalPin.P1, 2)
    servos.P0.setAngle(90)
})
basic.forever(function on_forever2() {
    music.play(music.stringPlayable("C5 A C C F D A E ", 122), music.PlaybackMode.UntilDone)
})
basic.forever(function on_forever3() {
    if (input.temperature() > tempp) {
        basic.showLeds(`
            . . . . .
            # . . . #
            . . . . .
            # # # # #
            # . . . #
            `)
    } else if (input.temperature() < tempp) {
        basic.showLeds(`
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
    } else {
        
    }
    
})
