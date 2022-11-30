import argparse

def my_func():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', help='Show you count of letters', action='store_true')
    parser.add_argument('file', help='whats your file?')
    args=parser.parse_args()

    with open(args.file, 'r', newline='') as f:
        text=f.read()

    splitted=text.split(" ")

    w=0
    l=0

    for i in splitted:
        if i: w += 1
        l += len(i)

    if args.f:
       print(f"You have {w} words in your file")
    else:
       print(f"You have {l} letters in your file")

if __name__=='__main__':
     my_func()