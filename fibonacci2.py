#!/usr/bin/env python

# fibonacci_gen.py

import time

def fib():
    
   a, b = 0, 1

   while True:
      yield b
      
      a, b = b, a + b


g = fib()

try:
   for e in g:
      print(e, end = " ")
      
 # time.sleep(1)

except KeyboardInterrupt:
   print("Calculation stopped")