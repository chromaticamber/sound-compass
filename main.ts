let dir2 = 0
basic.forever(function () {
    dir2 = input.compassHeading()
    if (dir2 < 5 || dir2 > 355) {
        basic.showString("N")
        music.ringTone(784)
    } else if (input.buttonIsPressed(Button.A)) {
        basic.showNumber(dir2)
    } else {
        basic.clearScreen()
        music.ringTone(0)
    }
})
