# pipe

__PROBLEM__

During your adventure, you will likely encounter a situation where you need to process data that you receive over the network rather than through a file. Can you find a way to save the output from this program and search for the flag? Connect with 2018shell2.picoctf.com 44310.

__HINT__

Remember the flag format is picoCTF{XXXX}

Ever heard of a pipe? No not that kind of pipe... This [kind](http://www.linfo.org/pipes.html)

__SOLUTION__

This is basicallly a combination of [net cat](../net%20cat/) and [grep 1](../grep%201).

Run
```
> nc 2018shell2.picoctf.com 44310 | grep pico
```

FLAG - `picoCTF{almost_like_mario_a13e5b27}`
