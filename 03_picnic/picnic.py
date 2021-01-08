#!/usr/bin/env python3
"""
Author :  David-Alexandre Guenette <da.guenette@icloud.com>
Date   : 2021-01-05
Purpose: Picnic Game
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic Game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('items',
                        metavar='str',
                        nargs='+',
                        help='Item(s) to bring')

    parser.add_argument('-s',
                        '--sorted',
                        action='store_true',
                        help='Sort the items')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    items = args.items
    sortList = args.sorted
    i = len(items) - 1

    if sortList:
        items.sort()

    if len(items) == 1:
        print("You are bringing {}.".format(items[0]))
    elif len(items) == 2:
        print("You are bringing {} and {}.".format(items[0], items[1]))
    else:
        print("You are bringing {}, and {}.".format(', '.join(items[:i]), items[-1]))

# --------------------------------------------------
if __name__ == '__main__':
    main()
