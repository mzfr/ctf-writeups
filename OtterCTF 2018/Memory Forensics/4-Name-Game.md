# 4-Name Game

__PROBLEM__

We know that the account was logged in to a channel called Lunar-3. what is the account name?

format: CTF{flag}

__SOLUTION__

Since the there was a log into the channel there must be some string in the memory about the account name.

so just strings + grep

```bash
➜ strings OtterCTF.vmem| grep Lunar-3  -A 2 -B 3
disabled
mouseOver
keyFocused
Lunar-3
0tt3r8r33z3
Sound/UI.img/
--
c+Yt
tb+Y4c+Y
b+YLc+Y
Lunar-3
Lunar-4
L(dNVxdNV
```

The `-A` parameter will print content of number of lines that is trailing the searched item and `-B` parameter will print content of number of lines that is leading searched item. To be more clear from `man grep`/`grep --help`

```bash
  -B, --before-context=NUM  print NUM lines of leading context
  -A, --after-context=NUM   print NUM lines of trailing context
```


So the only interesting thing in that grep is `0tt3r8r33z3`

FLAG - `CTF{0tt3r8r33z3}`
