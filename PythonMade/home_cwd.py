#!/usr/bin/env pyhon

from pathlib import Path
from shutil import copyfile
import os

print(f'Current working directory: {Path.cwd()}')
print(f'Home directory: {Path.home()}')

source = Path.cwd() / Path('words.txt')
print(source)

_path = Path.cwd() / 'PythonMade' # / Path('words.txt')
print(_path)

if os.path.isdir(_path):
    print('Folder exists')
else:
    _path.mkdir()

_path = Path.cwd() / 'PythonMade' / Path('words.txt')

copyfile(source, _path)
print(source)
print(source.absolute())

Path.touch(Path.cwd() / 'PythonMade' / Path('empty.txt'))

# _path = Path.cwd() / 'PythonMade' / Path('empty.txt')
# _path.rename = Path.cwd() / 'PythonMade' / Path('blank.txt')

print(f'The parent directory of {_path} is {_path.parent}')
print(f'The parent of parent directory of {_path} is {_path.parent.parent}')
print(f'All parents of {_path} are ')

print(list(_path.parents))

print(_path.parts)
print(_path.drive)
print(_path.root)

_path =  Path.cwd() / 'PythonMade' / Path('x.5.1.tar.gz')

print(_path.stem)
print(_path.suffix)

_path =  Path.cwd()

for e in _path.glob('*.py'):
    print(e)

# path.mkdir()