# DANGER ZONE

__PROBLEM__

 Legend says, this program was written by Kenny Loggins himself.

__HINT__

what is a .pyc file and can you convert it?

__SOLUTION__

We are given the .pyc file so using [uncompyle6](https://pypi.org/project/uncompyle6/) we get

```python
➜ uncompyle6 dangerzone.pyc
# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.7.1 (default, Oct 22 2018, 10:41:28)
# [GCC 8.2.1 20180831]
# Embedded file name: ./dangerzone.py
# Compiled at: 2018-11-22 12:44:11
import base64

def reverse(s):
    return s[::-1]


def b32decode(s):
    return base64.b32decode(s)


def reversePigLatin(s):
    return s[-1] + s[:-1]


def rot13(s):
    return s.decode('rot13')


def main():
    print 'Something Something Danger Zone'
    return '=YR2XYRGQJ6KWZENQZXGTQFGZ3XCXZUM33UOEIBJ'


if __name__ == '__main__':
    s = main()
    print s
# okay decompiling dangerzone.pyc
```

This shows us that a value is to be passed from the given function and then we'll get the flag.
You can manually try it or use python code to get the function
My teammate(@ugtan) was able to solve it using the following code

```
import itertools
L = [reverse, __]
Funs = itertools.permutations(L)
For i in funs:
    For j in i:
        s = j(s)
    print(s)
```
