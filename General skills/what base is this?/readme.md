# what base is this?

__PROBLEM__

To be successful on your mission, you must be able read data represented in different ways, such as hexadecimal or binary. Can you get the flag from this program to prove you are ready? Connect with nc 2018shell2.picoctf.com 1225.

__HINT__

I hear python is a good means (among many) to convert things.

It might help to have multiple windows open


__SOLUTION__

First question  -> [Binary-to-text](https://www.browserling.com/tools/binary-to-text)
Second question -> [Hex-to-text](https://codebeautify.org/hex-string-converter)
Third questions -> [octal-to-text](http://www.unit-conversion.info/texttools/octal/)

Here's a walkthrough:

```
> nc 2018shell2.picoctf.com 1225
We are going to start at the very beginning and make sure you understand how data is stored.
cake
Please give me the 01100011 01100001 01101011 01100101 as a word.
To make things interesting, you have 30 seconds.
Input:
cake
Please give me the 6170706c65 as a word.
Input:
apple
Please give me the  143 157 165 143 150 as a word.
Input:
couch
You got it! You're super quick!
Flag: picoCTF{delusions_about_finding_values_451a9a74}
```

FLAG - `picoCTF{delusions_about_finding_values_451a9a74}`
