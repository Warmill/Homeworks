import os
import argparse

def directory(raw_path):
    if not os.path.isdir(raw_path):
        raise argparse.ArgumentTypeError('"{}" is not an existing directory'.format(raw_path))
    return os.path.abspath(raw_path)



parser = argparse.ArgumentParser()
parser.add_argument('-c', help='count all files', action='store_true')
parser.add_argument('-d', help='change directory',nargs='?', default=os.path.curdir)
parser.add_argument('-l', help='last file', action='store_true')
args=parser.parse_args()

z = os.listdir(path=args.d)

if args.c:
    cnt = 0
    for el in z:
        if el: cnt += 1
    print(cnt)
elif args.d:
    print(z)
elif args.l:
    print(z[-1])