# blaise's cipher

__PROBLEM__

My buddy Blaise told me he learned about this cool cipher invented by a guy also named Blaise! Can you figure out what it says? Connect with nc 2018shell1.picoctf.com 59396.

__HINT__

There are tools that make this easy.

This cipher was NOT invented by Pascal

__SOLUTION__

Connecting to the service and again we get a message but this time we can clearly see that something is present in the format of flag format `pohzCZK{g1gt3w3_n1pn3wd_ax3s7_maj_1h7m92d3}`.

Now too know what kind of cipher this is we just have to google the name `blaise's cipher` which shows us that it a `Blaise de Vigenère cipher`.

Again using an [online decoder](https://www.guballa.de/vigenere-solver) we put in all the content and get the flag.
Why are we putting all the content because it's easy to crack the cipher if we have more cipher text. Try it yourself, first just put in the flag and you will get gibberish but putting all the content given you'll get everything right.

FLAG - `picoCTF{v1gn3r3_c1ph3rs_ar3n7_bad_1c7b92d3}`

P.S - I would suggest to read the plaintext we get from the ciphertext. It is really insteresting.
