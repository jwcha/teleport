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
    parser.add_argument('--number', '-n', help='how many files do you want to list? [default=10]', default=10)
    args = parser.parse_args()

    if args.verbose:
        print("verbose mode activate!")
    if args.depth:
        print("depth specified to: {}".format(args.depth))
    if args.number:
        print("I want to list {} of files".format(args.number))

    ### debug check: does query hold anything?
    print("QUERY IS: {}".format(args.query))

    if query[0] == '.':
        query = relative_to_absolute(query)

### check if query is relative or absolute path
def relative_to_absolute_path(query):
    current_dir = os.getcwd()
    if query[0] == '.':
        ### they want current directory
        if query[1] == '.':
            ### they want parent directory
            current_dir = current_dir[:current_dir.rfind('/')]
    return current_dir

### recurse through the query
def talk_a_walk(query):
    dirs, subs, files = [], [], []
    dir_file_dict = {}
    for d, s, f in os.walk(os.getcwd()):
        dirs.append(d)
        subs.append(s)
        files.append(f)

if __name__ == '__main__':
    main()
