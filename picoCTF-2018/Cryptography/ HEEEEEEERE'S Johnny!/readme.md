# HEEEEEEERE'S Johnny!

__PROBLEM__

Okay, so we found some important looking files on a linux computer. Maybe they can be used to get a password to the process. Connect with nc 2018shell1.picoctf.com 40157. Files can be found here: [passwd](./passwd) [shadow](./shadow).

__HINT__

If at first you don't succeed, try, try again. And again. And again.

If you're not careful these kind of problems can really "rockyou".


__SOLUTION__

This problem can easily be solved by using the very famous tool [John the ripper](https://www.openwall.com/john/).

You only need two commands
`unshadow passwd shadow > crack`

This will unshadow the passwd and the shadow file into crack file and then
`john -show crack`

I followed [this](https://www.cyberciti.biz/faq/unix-linux-password-cracking-john-the-ripper/) to succesfully retrieve the flag.

FLAG - `picoCTF{password1}`
