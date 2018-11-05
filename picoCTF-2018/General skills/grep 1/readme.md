# grep 1

__PROBLEM__

Can you find the flag in [file](file)? This would be really obnoxious to look through by hand, see if you can find a faster way. You can also find the file in /problems/grep-1_2_ee2b29d2f2b29c65db957609a3543418 on the shell server.

__HINT__

grep [tutorial](https://ryanstutorials.net/linuxtutorial/grep.php)

__SOLUTION__

Run
```bash
grep "picoCTF" file
```
Basically you are asking the `grep` command to find a string `picoCTF` in a `file`

FLAG - `picoCTF{grep_and_you_will_find_52e63a9f}`
