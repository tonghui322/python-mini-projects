#实现cat命令：通过输入文件路径，读取文件内容。
import argparse
from pathlib import Path
from sys import stderr, stdout
import os

class CatError(Exception):
    pass

class Logger:
    def __init__(self, verbosity=False):
        self.verbose = verbosity

    def error(self, message):
        print(f"ERROR:{message}")

logger = Logger()

def readFile(src: Path):
    if src.is_dir():
        logger.error(f"the path {src}: is a directory")
    else:
        with open(src,'r',encoding="utf-8") as f:
            for lines in f:
                print(lines,end='')

def cli() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog='cat',
        description='cat command implementation im python',
        epilog = 'Example:'
    )

    parser.add_argument(
        'source',
        type=Path,
        help='Source.file'
    )
    print(parser.parse_args())
    return parser.parse_args()

def main():
    args = cli()
    try:
        readFile(args.source)
    except CatError as e:
        logger.error(e)
        exit(1)
    except KeyboardInterrupt:
        logger.error('\nInterrupt')

if __name__ == "__main__":
    main()
