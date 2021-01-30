#!/usr/bin/env python3
"""
Author : echoappletree <echoappletree@localhost>
Date   : 2021-01-30
Purpose: Rock the Casbah
"""

import argparse
import sys





# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Emulate wc (word count)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


    parser.add_argument('file',
                        help='Input file(s)',
                        metavar='FILE',
                        nargs='*',
                        type=argparse.FileType('rt'),
                        default=[sys.stdin])

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    file_arg = args.file


    # Line, word, byte counts

    total_line, total_word, total_byte = 0, 0, 0



    # using a for loop to iterate the list
    for fh in file_arg:
        num_line, num_word, num_byte = 0, 0, 0
        for line in fh:
            # Calculate number of lines
            num_line += 1
            # Calculate number of words
            num_word += len(str.split(line))
            # Calculate number of bytes
            num_byte += len(line)

        # Add to total
        total_line += num_line
        total_word += num_word
        total_byte += num_byte
        # Print results for each file
        print("{:8}{:8}{:8} {}".format(num_line, num_word, num_byte, fh.name))
    
    # Print total if more than one file.
    if len(file_arg) > 1:
        print("{:8}{:8}{:8} total".format(total_line, total_word, total_byte))


# --------------------------------------------------
if __name__ == '__main__':
    main()
