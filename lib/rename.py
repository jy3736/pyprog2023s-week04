#!/usr/bin/env python

import os
import re
import argparse

class Renamer:
    def __init__(self, dir, pattern):
        self.dir = dir
        self.pattern = pattern

    def rename_files(self):
        files = os.listdir(self.dir)
        for file in files:
            match = re.match(self.pattern, file)
            if match:
                old_path = os.path.join(self.dir, file)
                new_name = match.group(1) + '.pyc'
                new_path = os.path.join(self.dir, new_name)
                os.rename(old_path, new_path)
                print(f'Renamed {old_path} to {new_path}')

def rename_files(dir, pattern=r'^(\w+)\.cpython-\d+\.pyc$'):
    renamer = Renamer(dir, pattern)
    renamer.rename_files()
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Rename pyc files')
    parser.add_argument('dir', metavar='dir', type=str, help='the directory containing the pyc files')
    parser.add_argument('--pattern', metavar='pat', type=str, default=r'^(\w+)\.cpython-\d+\.pyc$', help='the regular expression pattern to match the pyc filenames')
    args = parser.parse_args()
    rename_files(args.dir, args.pattern)
