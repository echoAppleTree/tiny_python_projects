#!/usr/bin/env python3
"""
Author : David-Alexandre Guenette <da.guenette@icloud.com>
Date   : 2021-01-10
Purpose: Jump the Five
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Jump the Five',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('str',
                        metavar='str',
                        help='Input text')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    inputUsr = args.str



    # 01 - Define the dict 
    jumper = {
        '1': '9',
        '2': '8',
        '3': '7',
        '4': '6',
        '5': '0',
        '6': '4',
        '7': '3',
        '8': '2',
        '9': '1',
        '0': '5'
    }

    # 02 - Iterate over the inputUsr.
    for char in inputUsr:
        # 03 - If the char in inputUsr is in jumper, it's a number.
        if char in jumper:
            # 04 - Encrypt number and avoid printing new line.
            print(jumper.get(char), end = '')
        else:
            # 05 - Print the letter if there's any letter.
            print(char, end = '')

    # 06 - End line
    print()

# --------------------------------------------------
if __name__ == '__main__':
    main()
