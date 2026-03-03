# baseline_inference_harness.py
# TinyML-style timing + memory harness for Pico 2 / RP2350 (MicroPython)
#
# Purpose:
# - Measure timing (ms) for a repeatable compute workload
# - Record free memory before/after (so later you can compare to real model inference)

import time
import gc

def workload(n=20000):
    # A deterministic integer workload (avoids floats)
    x = 1
    for i in range(1, n):
        x = (x * 33 + i) & 0xFFFFFFFF
    return x

gc.collect()
mem_before = gc.mem_free()
t0 = time.ticks_ms()

out = workload(30000)

t1 = time.ticks_ms()
mem_after = gc.mem_free()

print("Workload output:", out)
print("Time (ms):", time.ticks_diff(t1, t0))
print("Mem free before:", mem_before)
print("Mem free after :", mem_after)
print("Mem delta      :", mem_after - mem_before)
