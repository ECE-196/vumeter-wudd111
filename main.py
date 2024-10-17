import board
from digitalio import DigitalInOut, Direction
from analogio import AnalogIn
from time import sleep, time

def light_on(volume):
    val = volume // 4800
    for i in range(val+1):
        leds[i].value = 1

        

def light_off():
    for j in reversed(leds):
        if (j.value == 1):
            j.value = 0
            break
# setup pins
microphone = AnalogIn(board.IO1)

status = DigitalInOut(board.IO17)
status.direction = Direction.OUTPUT

led_pins = [
    board.IO21,
    board.IO26, # type: ignore
    board.IO47,
    board.IO33, # type: ignore
    board.IO34, # type: ignore
    board.IO48,
    board.IO35,
    board.IO36,
    board.IO37,
    board.IO38,
    board.IO39,
]

leds = [DigitalInOut(pin) for pin in led_pins]

for led in leds:
    led.direction = Direction.OUTPUT

#light off after time of reverse(leds[i]) == 1+0.5i
#so need to keep track of time once the light is on
#each light has its own timer
#the only way to time it is to use sleep function, so if all lights need to sleep to time that will cause a lot of delay
#so consider using global timer

# main loop
time = 0
while True:
    volume = microphone.value
    print(volume)
    light_on(volume)
    sleep(0.05)
    time += 1
    #print(time)
    if time == 10:
        light_off()
        time = 0

    # instead of blinking,
    # how can you make the LEDs
    # turn on like a volume meter?


