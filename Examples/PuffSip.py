import time
import board
from digitalio import DigitalInOut, Direction
import time
import board
import busio
import adafruit_lps35hw
import adafruit_midi
import usb_midi
import math
from adafruit_midi.note_off import NoteOff
from adafruit_midi.note_on import NoteOn
from adafruit_midi.control_change import ControlChange


#set MIDI ports
print(usb_midi.ports)
midi = adafruit_midi.MIDI(
    midi_in=usb_midi.ports[0], in_channel=0, midi_out=usb_midi.ports[1], out_channel=0
)

print(board.SCL)
print(board.SDA)
i2c = busio.I2C(board.SCL, board.SDA)

lps35hw = adafruit_lps35hw.LPS35HW(i2c)

led = DigitalInOut(board.IO15)    #reference to pin GPIO15 in S2 mini
led.direction = Direction.OUTPUT  #use it as output
lps = adafruit_lps35hw.LPS35HW(i2c)

# simple range mapper, like Arduino map()
def map_range(s, a1, a2, b1, b2):
    return  b1 + ((s - a1) * (b2 - b1) / (a2 - a1))


while True:
    sensorValue = lps.pressure
    valueMaped = min(max(sensorValue, 900), 1050)
    valueMaped = map_range(valueMaped, 900,1050, 5, 100)
    led.value = not(led.value)   #on
    print(valueMaped);
   # midi.send(ControlChange(3,math.floor(valueMaped))) #65536 ->128
    midi.send(NoteOn(math.floor(valueMaped), 120))  # G sharp 2nd octave
    time.sleep(0.1)
    # note how a list of messages can be used
    midi.send(NoteOff(math.floor(valueMaped), 120))
    time.sleep(0.1)