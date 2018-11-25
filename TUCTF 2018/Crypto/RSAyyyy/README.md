# RSAyyyy

__PROBLEM__

This challenge is designed to give an overview of the RSA algorithm.
If you have a team member that is less familiar with RSA that wants to be, give this challenge to them.
[This](https://simple.wikipedia.org/wiki/RSA_algorithm) might be useful.

nc 3.16.57.250 12345

__SOLUTION__

When you netcat to the server you are greeted with the following message
```
               AAA               YYYYYYY       YYYYYYYYYYYYYY       YYYYYYYYYYYYYY       YYYYYYY
              A:::A              Y:::::Y       Y:::::YY:::::Y       Y:::::YY:::::Y       Y:::::Y
             A:::::A             Y:::::Y       Y:::::YY:::::Y       Y:::::YY:::::Y       Y:::::Y
            A:::::::A            Y::::::Y     Y::::::YY::::::Y     Y::::::YY::::::Y     Y::::::Y
           A:::::::::A           YYY:::::Y   Y:::::YYYYYY:::::Y   Y:::::YYYYYY:::::Y   Y:::::YYY
          A:::::A:::::A             Y:::::Y Y:::::Y      Y:::::Y Y:::::Y      Y:::::Y Y:::::Y
         A:::::A A:::::A             Y:::::Y:::::Y        Y:::::Y:::::Y        Y:::::Y:::::Y
        A:::::A   A:::::A             Y:::::::::Y          Y:::::::::Y          Y:::::::::Y
       A:::::A     A:::::A             Y:::::::Y            Y:::::::Y            Y:::::::Y
      A:::::AAAAAAAAA:::::A             Y:::::Y              Y:::::Y              Y:::::Y
     A:::::::::::::::::::::A            Y:::::Y              Y:::::Y              Y:::::Y
    A:::::AAAAAAAAAAAAA:::::A           Y:::::Y              Y:::::Y              Y:::::Y
   A:::::A             A:::::A          Y:::::Y              Y:::::Y              Y:::::Y
  A:::::A               A:::::A      YYYY:::::YYYY        YYYY:::::YYYY        YYYY:::::YYYY
 A:::::A                 A:::::A     Y:::::::::::Y        Y:::::::::::Y        Y:::::::::::Y
AAAAAAA                   AAAAAAA    YYYYYYYYYYYYY        YYYYYYYYYYYYY        YYYYYYYYYYYYY

This challenge is designed to act as an introduction to RSA.
If you have a team member that is not already familiar with RSA,
then give this challenge to them.

For the first level, I recommend looking at
https://simple.wikipedia.org/wiki/RSA_algorithm
but any description of the RSA algorithm will do.

Later levels will probably require further research.

Let's get started!



Level 1: Calculating n

p = 2574755069
q = 2914669501
What is n?
```

It's easy in RSA n=p*q so just multiple the values which will give you n=7504560072159450569

```
Way to go!

Congratulations! You beat Level 1!

In order to calculate the ciphertext,
the message needs to be converted to an integer.


Level 2: Calculating m

message = "draught operand mightn't Nobel Juliet"
What is m?
```

So this might be confusing at first because most people just try to change the string into integers but that would not give the correct answer to get the correct answer you'll have to get the hex of the string and then change it into integer, you'll get m=49954527464255829976689522888633345002370443768254754957762089930007595204397331458385268

```
Nice job!

Congratulations! You beat Level 2!

Now, we are going to actually calculate ciphertext.


Level 3: Calculating c

p = 3549562609
q = 2451107779
What is n?
```

Again n=p*q which gives n=8700360522967435411

```
Ayyyyy

e = 65537
m = 7162252228817417076
What is c?
```

Okay so in RSA we have something like `c=m^e mod n` so using python we can just do `pow(m,e,n)` we get `1037069652894580590`

```
Way to go!

Congratulations! You beat Level 3!

In order for RSA to be asymmetrical,
the private exponent, d, needs to be calculated.


Level 4: Calculating d

p = 2203025723
q = 2230647037
What is tot(n)?
```

tot(n) is also know as phi(n) and can be calculate using the formula `phi(n) = (p-1)*(q-1)` so phi(n) or tot(n) = `4914172797011059992`

```
e = 65537
What is d?
```

to find d here we'll have to use `modinverse(e,phi)` so using the [calculate-d.py](calculate-d.py) we find `d=618836200829032121`

```
Yeah! You do that RSA!

Congratulations! You beat Level 4!

The easiest way to break RSA is factoring n, if it is possible.


Level 5: Factoring n

n = 8161155376032099187
What is p?
```

Using `https://www.alpertron.com.ar/ECM.HTM` we find the `    8 161155 376032 099187 = 2742818297 × 2975463371`

```
What is q?
2975463371
```

```
Congratulations! You beat Level 5!

Now, let's put everything together and break RSA!


Level 6: Breaking simple RSA

c = 4312287109452306269
n = 7096619028399642233
e = 65537
What is p?
2154140939

Whoop whoop!

What is q?
3294407947

Yeah! You do that RSA!

What is tot(n)?
7096619022951093348

Yeah! You do that RSA!

What is d?
1373043154416892193

Yeah! You do that RSA!

Finally, what is m?
7089073055325120867

Ayyyyy

Congratulations! You beat Level 6!


Congratulations on finishing this introduction to RSA!
I hope this was fun and informative.

Here's your flag:
TUCTF{RSA_1$_R34LLY_C00L_4ND_1MP0RT4NT_CRYPT0}
```

Everything is similar to previous steps just in the last method we use `pow(c,d,n)` to crack the RSA

FLAG - `TUCTF{RSA_1$_R34LLY_C00L_4ND_1MP0RT4NT_CRYPT0}`
