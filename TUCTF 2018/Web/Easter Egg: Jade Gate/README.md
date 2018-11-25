# Easter Egg: <br> Jade Gate

__PROBLEM__

Gotta make sure I log my changes. - Joker

http://18.191.227.167/

__SOLUTION__

Using the same git directory we downloaded in problem `copper gate` we have to look into the git logs. After trying for hours looking into the logs I wasn't able to find anything but thanks to @gtrven on discord he guided me through this.

Just go to the `INDEX` file in `.git` folder and do

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

We see a URL `youfoundthejadegate/gate.html` visit that and we have it.

FLAG -`TUCTF{S0_Th1s_D035n7_533m_l1k3_175_f41r_8u7_wh0_3v3r_s41d_l1f3_15_f41r?} `

Again Shoutout to @gtrven on discord for the help.
