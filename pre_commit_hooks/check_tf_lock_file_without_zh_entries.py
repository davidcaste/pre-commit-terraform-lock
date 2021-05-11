import argparse
from typing import Optional
from typing import Sequence


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*')
    args = parser.parse_args(argv)

    retcode = 0
    for filename in args.filenames:
        with open(filename, 'rb') as inputfile:
            for i, line in enumerate(inputfile):
                if line.startswith(b'    "zh:'):
                    print(
                        f'Found a "zip hash" (zh:) entry in {filename}:{i + 1}'
                    )
                    retcode = 1
    return retcode


if __name__ == '__main__':
    exit(main())
