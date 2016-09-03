import sys
import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import android_asset_resizer

requires = [
    'pillow',
]

setup(
    name='android-asset-resizer',
    version=android_asset_resizer.__version__,
    description='A command-line utility for generating Android drawables in'
                ' the required densities.',
    long_description=open('README.rst').read(),
    keywords='android asset resource res drawable resizer',
    license=open('LICENSE').read(),
    author='Tristan Waddington',
    author_email='tristan.waddington@gmail.com',
    url='https://github.com/twaddington/android-asset-resizer',
    install_requires=requires,
    packages=['android_asset_resizer'],
    scripts=['bin/aaresize'],
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ]
)
