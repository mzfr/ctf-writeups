# Super Safe RSA 3

__PROBLEM__

 The more primes, the safer.. right.?.? Connect with nc 2018shell1.picoctf.com 55431.

__HINT__

How would you find d if there are more than 2 prime factors of n?

__SOLUTION__

Connection to service we get:

>c: 194732599351366681376233015053875072009225980382382323563970387486742391475630834430246697121738557519142068815434239364615048514788798491105767807292055872375604441022762177071825852304745757594802547640207893551063301171257784988077775851353910761532094487362846940718054558350866139247592113029475591
n: 3189045736846566741028512343030385631639142688912438001802647200228206399093978664376810351262143656752409015249543089619950399945488151408711148210761185472710051069138766012738257323040348539920616815955530701650288955586901005651491564474799552525916205536523560996191502749127777700374154180890194291
e: 65537

Since we don't see anything unusual about these number so we follwo the hint and try to get the factors of n.
Using [alpertron.com](https://www.alpertron.com.ar/ECM.HTM) we get multiple factors of n.
This is confusing because if we had two factors we would have easily got the FLAG by finding the `phi(n)=p*q` followed by `d` and then `pow(c,d,n)`.
But what to do with so many multiples? Well the thing we need to understand here is that phi(n) isn't just the product of two (factor-1) it is the product of all the (factors-1).
Example: say the factor of n is p,q,a,z,t,w. so phi(n) would
```
phi(n) = (p-1)*(q-1)*(a-1)*(z-1)*(t-1)*(w-1)
```

Now we know what to do with multiple primes we calculate the `phi(n)` by using method mentioned above, after that we use [calculate-d.py](../rsa-madlibs/calculate-d.py) this time we put the value of `phi` variable and it gets us our `d`, after that `pow(c,d,n)` and voila.

Follow the decimal-hex-ascii and you'll have your flag.

FLAG - `picoCTF{p_&_q_n0_r_$_t!!_5280799}`
