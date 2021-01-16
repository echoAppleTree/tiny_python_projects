#!/usr/bin/env python3
"""
Author : David-Alexandre Guenette <da.guenette@icloud.com>
Date   : 2021-01-16
Purpose: Howler (upper-cases input)
"""

import argparse
import os

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Howler (upper-cases input)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input string or file')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='str',
                        type='str',
                        default='')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text
    outfile = args.outfile

    # --------------------------------------------------
    def handle_outfile(outfile, txt):
        """Write to outfile if there's an outfile"""

        if outfile:
            out_fh = open(outfile, 'wt')
            out_fh.write(txt)
            out_fh.close()
            return out_fh

        else:
            return print(txt)

    # --------------------------------------------------
    if os.path.isfile(text):
        fh = open(text).read().rstrip().upper()
        handle_outfile(outfile, fh)
    else:
        fh = text.upper()
        handle_outfile(outfile, fh)



# --------------------------------------------------
if __name__ == '__main__':
    main()
