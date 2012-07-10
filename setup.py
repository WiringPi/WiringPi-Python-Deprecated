#!/usr/bin/env python

from distutils.core import setup, Extension

wiringpi_module = Extension('_wiringpi',
                            sources=['wiringpi_wrap.c', 'WiringPi/wiringPi/wiringPi.c', 'WiringPi/wiringPi/serial.c', 'WiringPi/wiringPi/wiringShift.c'],
                            )

setup (name = 'wiringpi',
        version = '1.0',
        author = "Philip Howard",
        description = """WiringPi for Python""",
        ext_modules = [wiringpi_module],
        py_modules = ["wiringpi"],
        )
