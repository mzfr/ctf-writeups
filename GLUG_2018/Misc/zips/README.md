# Zips

__PROBLEM__

Zip zop Hop boopity bop Hex.

[dump.txt](dump.txt)

__SOLUTION__

We are given some hex values and the name of the problems says `Zips` that mean those hex have to do something with zip files. So let's try to get ascii out of those hex and see what we get.

Just go to [this](http://tomeko.net/online_tools/hex_to_file.php?lang=en) and get your `zip` file. Now this file actually looks like a zip file but we still don't know what type it is. Lets find out the type of this file:
```bash
>>> file zips
zips: bzip2 compressed data, block size = 900k
```
Okay it's a bzip2 file
```bash
>>>bunzip2 zips
bunzip2: Can't guess original name for zips -- using zips.out
```
Now all you have to do is change the extension from `.out` to `.tar` and then keep on extracting the data until you have a folder name [`dump`](dump/). There you'll see the `flag.txt`.

FLAG - `GLUG{mul71pl3_c0mpr35510n_15_fun}`
