from sys import argv
from hashlib import sha256
from random import getrandbits

def main():
    if argv[1] == 'commit':
        msg = argv[2]
        key = "{0:0{1}x}".format(getrandbits(256), 64) 
        print(len(key))
        com = hashing(key + msg)
        print("com: %s lenght: %i" % (com, len(com)))
        print("key: %s lenght: %i" % (key, len(key)))

    if argv[1] == 'verify':
        com = argv[2]
        key = argv[3]        
        msg = argv[4]
        print(com == hashing(key + msg))

def hashing(value):
    encoded_value = value.encode()
    print(sha256(encoded_value).hexdigest())
    return sha256(encoded_value).hexdigest()

if __name__ == "__main__":
    main()

