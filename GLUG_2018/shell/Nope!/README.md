# Nope!

__PROBLEM__

Nope!, you can't get it.
ssh shell8@142.93.207.206 -p1333
Password - shell8

__SOLUTION__

Well this one was a bit interesting. We start with `ls` and see `flag.txt`
so obviously we do `cat falg.txt` and we get `Nope`? wait is that a flag? Nope :wink:
So we do the following:

```bash
>>> cat *
Nope
>>> which cat
/usr/local/broken/cat
>>> while read line; do echo $line; done < flag.txt
GLUG{3v3ry7h1n6_1f_f1l3_h3r3}
```

What just happened there? Let's take it step by step
1) `cat *` - we try to see content of all the files and it just returns `Nope`

2) `which cat` - Since cat was returning `Nope` for everything so we check whatsup with our sweet little `cat` :smile_cat:, so this command shows us that the cat is actually broken. Oh No !! :scream_cat:

3) That is just another command to read the content of the file.


FLAG - `GLUG{3v3ry7h1n6_1f_f1l3_h3r3}`
