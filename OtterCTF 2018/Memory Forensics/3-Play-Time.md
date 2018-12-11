# 3-Play-Time

__PROBLEM__

Rick just loves to play some good old videogames. can you tell which game is he playing? whats the IP address of the server?

format: CTF{flag}


__SOLUTION__

To find the name of the game I started with looking at the process tree
```bash
➜ vol.py -f OtterCTF.vmem --profile=Win7SP1x64 pstree
Name                                                  Pid   PPid   Thds   Hnds Time
-------------------------------------------------- ------ ------ ------ ------ ----
 0xfffffa801b27e060:explorer.exe                     2728   2696     33    854 2018-08-04 19:27:04 UTC+0000
. 0xfffffa801b486b30:Rick And Morty                  3820   2728      4    185 2018-08-04 19:32:55 UTC+0000
.. 0xfffffa801a4c5b30:vmware-tray.ex                 3720   3820      8    147 2018-08-04 19:33:02 UTC+0000
. 0xfffffa801b2f02e0:WebCompanion.e                  2844   2728      0 ------ 2018-08-04 19:27:07 UTC+0000
. 0xfffffa801a4e3870:chrome.exe                      4076   2728     44   1160 2018-08-04 19:29:30 UTC+0000
.. 0xfffffa801a4eab30:chrome.exe                     4084   4076      8     86 2018-08-04 19:29:30 UTC+0000
.. 0xfffffa801a5ef1f0:chrome.exe                     1796   4076     15    170 2018-08-04 19:33:41 UTC+0000
.. 0xfffffa801aa00a90:chrome.exe                     3924   4076     16    228 2018-08-04 19:29:51 UTC+0000
.. 0xfffffa801a635240:chrome.exe                     3648   4076     16    207 2018-08-04 19:33:38 UTC+0000
.. 0xfffffa801a502b30:chrome.exe                      576   4076      2     58 2018-08-04 19:29:31 UTC+0000
.. 0xfffffa801a4f7b30:chrome.exe                     1808   4076     13    229 2018-08-04 19:29:32 UTC+0000
.. 0xfffffa801a7f98f0:chrome.exe                     2748   4076     15    181 2018-08-04 19:31:15 UTC+0000
. 0xfffffa801b5cb740:LunarMS.exe                      708   2728     18    346 2018-08-04 19:27:39 UTC+0000
. 0xfffffa801b1cdb30:vmtoolsd.exe                    2804   2728      6    190 2018-08-04 19:27:06 UTC+0000
. 0xfffffa801b290b30:BitTorrent.exe                  2836   2728     24    471 2018-08-04 19:27:07 UTC+0000
.. 0xfffffa801b4c9b30:bittorrentie.e                 2624   2836     13    316 2018-08-04 19:27:21 UTC+0000
.. 0xfffffa801b4a7b30:bittorrentie.e                 2308   2836     15    337 2018-08-04 19:27:19 UTC+0000
 0xfffffa8018d44740:System                              4      0     95    411 2018-08-04 19:26:03 UTC+0000
```

You'll notice that there's only one process that stands out `LunarMS`. Just to confirm it I googled it and yes it's a game.
For IP again I did the netscan but with `grep`

```bash
➜ vol.py -f OtterCTF.vmem --profile=Win7SP1x64 netscan | grep MS
Volatility Foundation Volatility Framework 2.6
0x7d6124d0         TCPv4    192.168.202.131:49530          77.102.199.102:7575  CLOSED           708      LunarMS.exe
0x7e413a40         TCPv4    -:0                            -:0                  CLOSED           708      LunarMS.exe
0x7e521b50         TCPv4    -:0                            -:0                  CLOSED           708      LunarMS.exe

```
FLAG - Game Name - `CTF{LunarMS}`
       Server IP - `CTF{77.102.199.102}`
