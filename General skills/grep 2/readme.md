# grep 2

__PROBLEM__

This one is a little bit harder. Can you find the flag in /problems/grep-2_2_413a577106278d0711d28a98f4f6ac28/files on the shell server? Remember, grep is your friend.

__HINT__

grep [tutorial](https://ryanstutorials.net/linuxtutorial/grep.php)

__SOLUTION__

If you'll go to the given directory and run `ls` command you'll see that there are multiple directories now obviously we cannot get into all those directory and find the flag, manually well that is why it's called `grep`

Run
```
> grep "picoCTF" */*
> files2/file16:picoCTF{grep_r_and_you_will_find_8eb84049}
```

Here `*/*` means that you want to go into directories recursively.

FLAG - `picoCTF{grep_r_and_you_will_find_8eb84049}`
