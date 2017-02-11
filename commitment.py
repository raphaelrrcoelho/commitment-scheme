from sys import argv
from hashlib import sha256
from random import getrandbits

def main():
    if argv[1] == 'commit':
        msg = argv[2]
        key = str(getrandbits(256))
        com = hashing(key + msg)
        print("com: %s" % com)
        print("key: %s" % key)

    if argv[1] == 'verify':
        com = argv[2]
        key = argv[3]        
        msg = argv[4]
        print(com == hashing(key + msg))

def hashing(value):
    encoded_value = value.encode()
    return sha256(encoded_value).hexdigest()

if __name__ == "__main__":
    main()

