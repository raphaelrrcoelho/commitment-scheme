Commitment Scheme API

```
commit(msg) -> (com, key)
veryfy(com, key, msg) -> boolean
```

Commitment Scheme API Implementation

```
commit(msg) -> (Hash(key | msg), key) // key = randon 256-bit value 
veryfy(com, key, msg) -> com == Hash(key | msg)
```
Usage

```
python commitment.py [commit] <msg>
python commitment.py [verify] <com> <key> <msg>
```
