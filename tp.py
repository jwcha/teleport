#!/usr/bin/env python3

### python 3 - teleport!                                              2017.11.17
### author: supadood,jwcha

import os
import argparse

def main():
    ### init arg parser
    ### query is mandatory, --verbose --depth is optional
    parser = argparse.ArgumentParser()
    parser.add_argument('query', help='directory to begin recursive sort of most recent files')
    parser.add_argument('--verbose', '-v', help='output more information')
    parser.add_argument('--depth', '-d', help='specify a max depth to recurse')


if __name__ == '__main__':
    main()
