"""Unix2dos Batch — Convert LF and CRLF line endings in a folder of text files."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='unix2dos_batch',
        description='Convert LF and CRLF line endings in a folder of text files.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Unix2dos Batch')
    print('Line endings that match the repo.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
