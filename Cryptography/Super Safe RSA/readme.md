# Super safe RSA

__PROBLEM__

 Dr. Xernon made the mistake of rolling his own crypto.. Can you find the bug and decrypt the message? Connect with nc 2018shell1.picoctf.com 3609.

__HINT__

Just try the first thing that comes to mind.

__SOLUTION__

Connecting to service we get:

> c: 1787623970726643739771686335483107490602840788639676288252539000924355942599227
> n: 8277459395494016699026775407226432970002268013781620574063003740540333302800441
> e: 65537


Now problem with this that the value of N is small. we can easily find the factor of n. This can be done either on [factordb.com](http://factordb.com/) or on [alperton.com](https://www.alpertron.com.ar/ECM.HTM).

After facotrizing `n` we get `p` and `q`.
> p=94 023571 856854 509596 183682 157927 676551
> q=88036 002377 105747 827673 647405 078186 819391

Now we need to find `d` for that we'll need `phi(n)` so again use the [calculate-d.py](../rsa-madlibs/calculate.py) just put in the value and wait for it to give you the value of `d` after that do some `pow` i.e `pow(c,d,n)`.

You'll get a decimal then do the same thing of, changing decimal-hex-ascii and you'll get it.

FLAG - `picoCTF{us3_l@rg3r_pr1m3$_5157}`

