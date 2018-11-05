# Desrouleauxs

__PROBLEM__

 Our network administrator is having some trouble handling the tickets for all of of our incidents. Can you help him out by answering all the questions? Connect with nc 2018shell1.picoctf.com 14079. [incidents.json](./incidents.json)

__HINT___

If you need to code, python has some good libraries for it.

__SOLUTION__

I don't know why does this kind of problem exists in CTFs. So all you have to do is answer the question using that JSON file.

First question
>What is the most common source IP address? If there is more than one IP address that is the most common, you may give any of the most common ones.

Answer: 248.0.40.3

Second question
>How many unique destination IP addresses were targeted by the source IP address 248.0.40.3?

Answer: 4
In this question the source IP changes so if it was `159.244.90.48` then asnwer would be `3` and if it was `109.165.249.213` then answer would be `2`

Third question
>What is the average number of unique destination IP addresses that were sent a file with the same hash? Your answer needs to be correct to 2 decimal places.

This question was very confusing and not just for me but for lot of other people.

The solution of this question is
```
    File A - 202c039d90890a56 -- 230.133.250.144
    File B - c8d375ac6838d6c2 -- 247.123.233.70
    Fiel C - 3a9fa679b4970226 -- 230.133.250.144, 55.147.213.232
    File D - 3f3799a5e45f6a2f -- 55.147.213.232
    File E - 5d46ae30d1ac00d1 -- 167.139.249.203
    File F - cf469af70ceae4c9 -- 217.17.74.52
    File G - f83ad50a7a0a07fe -- 167.139.249.203,68.227.44.122
```

so average = 9/7 = 1.28

Actually I solved this question by brute force method. [Here's](desrouleaux.py)my code for brute force.

FLAG - `picoCTF{J4y_s0n_d3rUUUULo_4f3aae0d}`
