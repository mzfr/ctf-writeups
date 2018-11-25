# Professor Plum's <br> Ravenous Researcher

__PROBLEM__

Professor Plum is hiring! Maybe you can get the job!

http://18.223.185.148/

__HINT__

Where does Mr. Boddy live?

__SOLUTION__

I am grateful to @gtrven on discord for helping me in this.

We visit the given URL and after a bit finds out that we'll have to tell where we want to look for MR. Boddy. Now this might sound like vague but if you'll notice the error we get when we enter a random word say `room`

```
Nice try but he's not there

Maybe try somewhere else in the mansion?
```

Notice the word `mansion`. @gtrve told we there's a game called `clue` and it have rooms like Kitchen, Conservatory, Dining Room, Ballroom, Study, Hall, Lounge, Library, Billiard Room in it. So I tried all the rooms and found out that `Billiard Room` gives a different error

```
Nice try but you can't find him

Maybe try looking again?
```

Now one thing is obvious that we'll have to look through what kind of data is being send or received.

For this I used [`tamper data`](https://chrome.google.com/webstore/detail/tamper-chrome-extension/hifhgpdkfodlpnlmlnmhchnkepplebkb?hl=en) extension on chrome and modified the requests `Found_Boddy=0; Location=YmlsbGlhcmQgcm9vbQ%3D%3D` to `Found_Boddy=1; Location=YmlsbGlhcmQgcm9vbQ%3D%3D` for all the requests that were caught in tamper data and then got

```
Congrats! You found him
TUCTF{1_4ccu53_pr0f3550r_plum_w17h_7h3_c00k13_1n_7h3_b1ll14rd_r00m}
```

FLAG - `TUCTF{1_4ccu53_pr0f3550r_plum_w17h_7h3_c00k13_1n_7h3_b1ll14rd_r00m}`

P.S -  @gtrven told me that burp suite's repeater can be used for checking which room have different message and stuff. I was not comfortable with burp suite plus number of rooms were not many so I tried every room manually.
