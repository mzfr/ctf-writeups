# Raretowin

__PROBLEM__

We are given a zip file that contains memory dump and we need to find out the full path to the virus.


__SOLUTION__

 This is quite confusing but __@kroz__ figure out the correct way to do it.

 The rar file is infact not a rar file but a vulnerability listed by Checkpoint recently in which .ace file can masquerade as .rar.

 So the first step is to rename the file `music.ace`, then `unace` software on Linux, the default doesn't work. So download [this](http://webdiis.unizar.es/pub/unix/archive/linunace25.tgz)

Then just run the unace on the music.ace file:

```
./unace e music.ace

UNACE v2.5     Copyright by ACE Compression Software       Jun 18 2003 22:25:55

processing archive /root/ctf/shit/music.ace
Working: Creating listfile. Please wait.
Working: Reading archive. Please wait.
created on 22.2.2019 with ver 2.0 by
*UNREGISTERED VERSION*
 extracting readme.txt                                    CRC OK
 extracting \..MORE FEAT SKYLAR GREY - GLORIOUS.mp3
CRC-check error on MACKLEMORE FEAT SKYLAR GREY - GLORIOUS.mp3
 extracting \..MORE FEAT LIL YACHTY - MARMALADE.mp3
CRC-check error on MACKLEMORE FEAT LIL YACHTY - MARMALADE.mp3
 extracting MACKLEMORE & RYAN LEWIS - DOWNTOWN.mp3
CRC-check error on MACKLEMORE & RYAN LEWIS - DOWNTOWN.mp3
 extracting \..N LEWIS - THRIFT SHOP FEAT. WANZ.mp3
CRC-check error on MACKLEMORE & RYAN LEWIS - THRIFT SHOP FEAT. WANZ.mp3
 extracting \.. - CANT HOLD US FEAT. RAY DALTON.mp3
CRC-check error on MACKLEMORE & RYAN LEWIS - CANT HOLD US FEAT. RAY DALTON.mp3
 extracting \..ORE FEAT KESHA -  GOOD OLD DAYS .mp3
CRC-check error on MACKLEMORE FEAT KESHA -  GOOD OLD DAYS .mp3
 extracting C:/Users/Public/Data/firefox.exe
Error: Could not create directory:
C:/Users/Public/Data
Error: Could not create destination file: \..Data/firefox.exe
Disk might be write-protected.

extracted: 7 files, totaling 42.153K bytes (compressed 42.153K)
Got CRC check errors on 6 files.
```
As we can see it extracts music and a suspicious firefox.exe which is a dropped payload.

And the flag is `C:\\Users\\Public\\Data\\firefox.exe` (md5sum of it )

FLAG - `Securinets{9c2623856856ce8aa830a5feb0e4910d}`
