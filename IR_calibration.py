# Calibrates IR LEDS
# Reports current resistance either every 5 seconds, press of a button, or a constant stream (hopefully this is the chosen one)
import RPi.GPIO as GPIO

x0 = 0  #x1-x3 are the IR LED sensors from left to right
x1 = 0
x2 = 0

