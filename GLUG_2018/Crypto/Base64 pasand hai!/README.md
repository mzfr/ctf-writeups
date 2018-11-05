# Base64 pasand hai!

__PROBLEM__

Sultan loves Aarfa. Aarfa is very cryptic and mysterious girl.Sultan one day proposes Aarfa.Aarfa being a strong headed girl,is not impressed with Sultan at all.So,she challenges Sultan to find the flag for this level by decoding a file that she gives.
Sultan is very dumb but really loves Aarfa.Can you help him win her heart?

The flag is not in standard format.
The format of the flag here is Glug{}.

__GIVEN__

a3B5a3t4bCVfa0BxaV8hJl9zcn0K

__HINT__

Aarfa's ex was caesar.

__SOLUTION__

As the name suggest just decode the given string with base64. you can do something like
```
➜ echo a3B5a3t4bCVfa0BxaV8hJl9zcn0K | base64 -d
```

This will give you `kpyk{xl%_k@qi_!&_sr}`. Now if you focus on the given hint it says something about `caesar`. Yes that has to be encrypted by caesar cipher.
Just go on my favourite [decoder](https://cryptii.com/pipes/caesar-cipher) and you'll have the flag.

Flag - `Glug{th%_g@me_!&_on}`
