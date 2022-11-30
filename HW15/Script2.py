import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-c', help='count all files', action='store_true')
parser.add_argument('-d', help='change directory',nargs='?', default=os.path.curdir)
parser.add_argument('-l', help='last file', action='store_true')
args=parser.parse_args()

z = os.listdir(path=args.d)

if args.l:
    print(z[-1])
elif args.c and args.d:
    cnt = 0
    for el in z:
        if el: cnt += 1
    print(cnt)
