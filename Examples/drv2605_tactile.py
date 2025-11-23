# Play all 123 effects in order for 1 second each.
import time

import board
import busio

import adafruit_drv2605

# Initialize I2C bus and DRV2605 module.
i2c = busio.I2C(board.SCL, board.SDA)
drv = adafruit_drv2605.DRV2605(i2c)

# See table 11.2 for a list of all the effect
# http://www.ti.com/lit/ds/symlink/drv2605.pdf
effect_id = 1
while True:
    print(f"Playing effect #{effect_id}")
    drv.sequence[0] = adafruit_drv2605.Effect(effect_id)  # Set the effect on slot 0.
    # You can assign effects to up to 8 different slots to combine them. 
    # Index the sequence property with a slot number 0 to 7.
    drv.play()  # play the effect
    time.sleep(1)  # for 1 seconds
    drv.stop()  # stop the effect
    # Increment effect ID
    effect_id += 1
    if effect_id > 123:
        effect_id = 1
