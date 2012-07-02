#!/usr/bin/env python

from distutils.core import setup, Extension

wiringpi_module = Extension('_wiringpi',
                            sources=['wiringpi_wrap.c', 'wiringPi.c', 'serial.c', 'wiringShift.c'],
                            )

setup (name = 'wiringpi',
        version = '0.1',
        author = "Philip Howard",
        description = """WiringPi for Python""",
        ext_modules = [wiringpi_module],
        py_modules = ["wiringpi"],
        )
