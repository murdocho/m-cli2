import argparse
import unittest

parser = argparse.ArgumentParser()
parser.add_argument('greeting')
parser.add_argument('--name', help = 'enter the name you want to greet')

args = parser.parse_args()

def what_to_return(args):
    if args.name:
        print(args.greeting, args.name)

    else:
        print(args.greeting, ' World')

what_to_return(args)
'''
if args.name:
    print('Hello', args.name)

elif args.greeting:
    print(args.greeting, ' World')
'''
#else:
#    print(args.greeting, ' World')
