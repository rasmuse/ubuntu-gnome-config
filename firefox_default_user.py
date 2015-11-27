#!/usr/bin/python3

import configparser
import os

def main():
    parser = configparser.ConfigParser()
    parser.read(os.path.expanduser('~/.mozilla/firefox/profiles.ini'))

    for data in parser.values():
        if data.get('Default', False):
            print(os.path.expanduser('~/.mozilla/firefox/' + data['Path']))

if __name__ == '__main__':
    main()
