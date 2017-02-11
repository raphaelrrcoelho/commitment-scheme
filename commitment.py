from sys import argv
import random

def main():
    if argv[1] == 'commit':
        msg = argv[2]
        key = str(random.getrandbits(256))
        com = hashing(key + msg)
        print("com: %s" % com)
        print("key: %s" % key)

    if argv[1] == 'verify':
        pass

def hashing(value):
    return value + '!'

if __name__ == "__main__":
    main()

