# Baby RE

__PROBLEM__

A script was discovered in one of the most obsolete locations in a system and have been trying to analyse it since, could you help us analyse it.

[File](Baby_RE.pyc)

__SOLUTION__

We are given a pyc file so first we'll have to decompile it using [uncompyle6](https://pypi.org/project/uncompyle6/2.2.0/).

```python
✦ ➜ uncompyle6 Baby_RE.pyc
# uncompyle6 version 3.2.5
# Python bytecode 3.6 (3379)
# Decompiled from: Python 3.5.6 (default, Jan  6 2019, 09:00:50)
# [GCC 8.2.1 20181127]
# Embedded file name: flag.py
# Compiled at: 2019-01-04 23:02:56
# Size of source mod 2**32: 528 bytes
print('HELLO HACKER')
password = input('Enter the Flag: ')
KEY = '*************Welcome To Anokha CTF!!**********'
I = 9
FLAG = [171, 89, 80, 83, 57, 229, 28, 232, 53, 28, 17, 161, 32, 15, 172, 202, 227, 22, 5, 237, 240, 178, 203, 218, 206, 160, 74, 163, 189, 161, 172, 90, 67, 168, 176, 180, 100, 11, 84]
FLAG_ = []
for X in password:
    FLAG_.append((ord(X) + I ^ ord(KEY[I])) % 255)
    I = (I + 1) % len(KEY)

if FLAG == FLAG_:
    print('You Win')
else:
    print('Try Again !')
# okay decompiling Baby_RE.pyc

```

Now we have the source code and we can see that there is some XOR happening right there.
So I wrote a simple code to reverse that up(not exactly :smile:)

```python
from string import printable

KEY = '*************Welcome To Anokha CTF!!**********'
FLAG = [171, 89, 80, 83, 57, 229, 28, 232, 53, 28, 17, 161, 32, 15, 172, 202, 227, 22, 5, 237, 240, 178, 203, 218, 206, 160, 74, 163, 189, 161, 172, 90, 67, 168, 176, 180, 100, 11, 84]
I = 9
DOPE = []
ind = 0
for i in range(len(FLAG)):
    # print("Bruteforcing 1st: ", i)
    for X in printable:
        value = ord(X) + I ^ ord(KEY[I]) % 255
        if value == FLAG[ind]:
            print(X)
            I = (I + 1) % len(KEY)
            ind += 1

```
This actually doesn't reverse anything but kind of bruteforce the right values.

FLAG - `xiomara{I_am_Just_Sitting_Here_H@Xor!!}`
