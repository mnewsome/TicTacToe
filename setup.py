#!/usr/bin/env python

from distutils.core import setup

setup(
      name='tictactoe',
      version='1.0',
      description='Unbeatable Tic Tac Toe',
      author='Malcolm Newsome',
      autho_email='malcolm.newsome@gmail.com',
      py_modules=['game'],
      packages=['src', 'tests']
)