#!/usr/bin/env python

from setuptools import setup, Extension

wiringpi_module = Extension(
    '_wiringpi',
    sources=[
        'wiringpi_wrap.c',
        'WiringPi/wiringPi/wiringPi.c',
        'WiringPi/wiringPi/serial.c',
        'WiringPi/wiringPi/wiringShift.c'
    ],
)

setup(
    name = 'wiringpi',
    version = '1.0',
    author = "Philip Howard",
    packages = ["wiringpi"],
    url = 'https://github.com/WiringPi/WiringPi-Python/',
    description = """A python interface to WiringPi library which allows for
    easily interfacing with the GPIO pins of the Raspberry Pi. Also supports
    i2c and SPI""",
    long_description=open('README.md').read(),
    ext_modules = [wiringpi_module],
    install_requires=[],
)
