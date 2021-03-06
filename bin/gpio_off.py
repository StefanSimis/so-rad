#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Shortcut to switch off all GPIO pins

"""
import RPi.GPIO as GPIO

def run():
    GPIO.setmode(GPIO.BOARD)
    pins = [11,12,13,15]  # FIXME: get from configs
    GPIO.setup(pins, GPIO.OUT)
    GPIO.output(pins, GPIO.LOW)
    GPIO.cleanup()
    print("done")

if __name__ == '__main__':
    run()
