deep_sleep_test.py
# deep_sleep_test.py
# RP2350 / Pico 2 MicroPython low-power sleep cycle test
#
# What it does:
# - Blinks LED briefly (so you know it woke)
# - Sleeps for SLEEP_MS
# - Repeats forever
#
# Measure current with a USB power meter:
# - During the brief blink = "active"
# - During sleep = "sleep current"

import time
from machine import Pin

SLEEP_MS = 10_000   # 10 seconds. Change this to 60_000 for 60s, etc.

led = Pin("LED", Pin.OUT)

def pulse_led(ms=150):
    led.value(1)
    time.sleep_ms(ms)
    led.value(0)

while True:
    # Wake indicator
    pulse_led(150)

    # Give you a moment to see the LED before sleeping
    time.sleep_ms(200)

    # Sleep (light sleep / idle depending on port capabilities)
    # If your MicroPython port supports deep sleep later, we can switch to it.
    time.sleep_ms(SLEEP_MS)
