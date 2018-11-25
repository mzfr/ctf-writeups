# Easter Egg: <br> Copper Gate

__PROBLEM__

How did I end up here? - Joker

http://18.191.227.167/

__SOLUTION__

I had no clue what to do since I didn't find anything in source.
So I used [dirb](https://aur.archlinux.org/packages/dirb/) and found out that there was a `.git` directory on that website.

Using [Gittool's](https://github.com/internetwache/GitTools) `gitdumper` I downloaded the directory and then using `extracter` I got all the commits.

Then I found the image that had base64 of the flag ` VFVDVEZ7VzNsYzBtM19UMF9UaDNfMDQ1MTVfVGgzX0MwcHAzcl9LM3l9Cg== `

FLAG - `TUCTF{W3lc0m3_T0_Th3_04515_Th3_C0pp3r_K3y}`
