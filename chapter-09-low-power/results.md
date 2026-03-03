# Low-Power Measurement Results (Pico 2 / RP2350)

## Test Setup
- Board: Raspberry Pi Pico 2 (RP2350)
- Firmware: MicroPython
- Code: deep_sleep_test.py
- Sleep interval: 10s
- Measurement tool: USB power meter

## Measurements
| Mode | What the board was doing | Current (mA) |
|------|---------------------------|--------------|
| Active | LED pulse + running loop | TBD |
| Idle/Sleep | During `time.sleep_ms()` | TBD |

## Notes
- Power readings can jump during USB activity.
- Repeat the test with different sleep intervals and with USB serial disconnected (if possible).
