===============
WiringPi Python
===============

A library for working with the Raspberry Pi GPIO header in Python.
Implements many Arduino Wiring functions for the Raspberry Pi, including Serial and Digital/PWM output.

Prerequisites
=============

You must have python-dev installed

Class-based Usage
=================

    import wiringpi
    io = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_PINS)
    io.pinMode(1,io.OUTPUT)
    io.digitalWrite(1,io.HIGH)

    GPIO with /sys/class/gpio (You must first export the interfaces):
    import wiringpi
    io = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_SYS)
    io.pinMode(1,io.OUTPUT)
    io.digitalWrite(1,io.HIGH)

    Serial:
    serial = wiringpi.Serial('/dev/ttyAMA0',9600)
    serial.puts("hello")
    serial.close()

Usage
=====

    import wiringpi
    wiringpi.wiringPiSetup // For sequential pin numbering, one of these MUST be called before using IO functions
    OR
    wiringpi.wiringPiSetupSys // For /sys/class/gpio with GPIO pin numbering
    OR
    wiringpi.wiringPiSetupGpio // For GPIO pin numbering

General IO
==========

    wiringpi.pinMode(1,1) // Set pin 1 to output
    wiringpi.digitalWrite(1,1) // Write 1 HIGH to pin 1
    wiringpi.digitalRead(1) // Read pin 1

Bit shifting
============

    wiringpi.shiftOut(1,2,0,123) // Shift out 123 (b1110110, byte 0-255) to data pin 1, clock pin 2

Serial
======

    serial = wiringpi.serialOpen('/dev/ttyAMA0',9600) // Requires device/baud and returns an ID
    wiringpi.serialPuts(serial,"hello")
    wiringpi.serialClose(serial) // Pass in ID

Full details at
===============

https://projects.drogon.net/raspberry-pi/wiringpi/

