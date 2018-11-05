# Aca-Shell-A

__PROBLEM__

It’s never a bad idea to brush up on those linux skills or even learn some new ones before you set off on this adventure! Connect with nc 2018shell2.picoctf.com 33158.

__SOLUTION__

Here's the walkthrough:
```
❯ nc 2018shell2.picoctf.com 33158
Sweet! We have gotten access into the system but we aren't root.
It's some sort of restricted shell! I can't see what you are typing
but I can see your output. I'll be here to help you along.
If you need help, type "echo 'Help Me!'" and I'll see what I can do
There is not much time left!

~/$ ls
blackmail
executables
passwords
photos
secret

~/$ cd secret
Now we are cookin'! Take a look around there and tell me what you find!

~/secret$ ls
intel_1
intel_2
intel_3
intel_4
intel_5
profile_AipieG5Ua9aewei5ieSoh7aph
profile_Xei2uu5suwangohceedaifohs
profile_ahShaighaxahMooshuP1johgo
profile_ahqueith5aekongieP4ahzugi
profile_aik4hah9ilie9foru0Phoaph0
profile_bah9Ech9oa4xaicohphahfaiG
profile_ie7sheiP7su2At2ahw6iRikoe
profile_of0Nee4laith8odaeLachoonu
profile_poh9eij4Choophaweiwev6eev
profile_poo3ipohGohThi9Cohverai7e
Sabatoge them! Get rid of all their intel files!

~/secret$ rm int*
Nice! Once they are all gone, I think I can drop you a file of an exploit!
Just type "echo 'Drop it in!' " and we can give it a whirl!

~/secret$ echo 'Drop it in!'
Drop it in!
I placed a file in the executables folder as it looks like the only place we can execute from!
Run the script I wrote to have a little more impact on the system!

~/secret$ cd ..

~/$ ls
blackmail
executables
passwords
photos
secret

~/$ cd executables

~/executables$ ls
dontLookHere

~/executables$ ./dontLookHere
 cf69 a945 2efc 049b c832 b41f b76f f57e 9e0a 3275 d297 e0b0 7a9a b2c8 c64a 8150 5d5b ccd4 2d68 eed4 4111 abc2 aeb0 f650 f489
 5e42 49d2 0b85 7627 a089 db3f 3788 0d72 3ee6 e1e1 295d a61b 6ce6 b4f4 26e5 0c19 af21 94f7 5f22 e213 7176 53ea d99d c44c f9d7
 571f 031f 43ec c803 9200 d377 b04f e0da 3ae0 b741 4e61 e11e 6c3b 4c73 bc18 2f92 fc7b c406 9e40 c5e9 47c9 f67c 8bb1 0d4c 80db
 65a8 f775 e505 cec5 9d90 4f23 d382 788a f3a9 deb8 e83d ae83 c136 d390 651d b58c 734f 02c0 1cf3 f5dc 160f 6eab 505b 3f7f 3567
 50f7 0feb cc71 4051 1395 15bf 659b 1595 d70f 711e d699 2c71 f68f 50fe 145b eed4 32ae 725e e0b3 3a28 2d5f 86f2 0d15 922a 8515
 52a6 9f7f 2901 09d2 00b9 88a4 af8a 01ab 00d4 363a 010f 0cf9 180a b9a6 f3fe beb2 3317 90e1 3cd1 2027 0548 ba3d 9139 b591 4ea5
 8fcc 7ef9 1f01 2980 d036 8ac4 a322 834a a1b8 f648 53fc e2cf 5c97 0a3c 2527 eb74 f478 ba32 a253 8086 e93d 0cb2 58ae bbca 287d
 b835 48fe 1ff5 b0f9 46ca e08d 1893 382c 47f7 2a4f 21cd 1d22 aad0 97f8 c38d ceaa 3c74 f421 a7f6 4b1c 270a 7798 f7b0 45d3 8529
 3994 2d68 4cc5 8690 628f 292b a742 d795 b2f4 6e5d 1bb5 4bed 34cc 4f6d 3d04 8509 50a6 8185 3114 7bb9 c093 b626 97fa ada0 1a91
 5769 ecaf 3e3a bc69 e73e 171a 3fa1 82f7 bf41 f9df cf19 a428 d2ee 595d f1a9 0511 201f e950 cdba ab22 0f5a b270 85aa 9940 aa4b
 7d11 bcbe 8b0c 6742 729c cca0 f4ea 2077 bf4c 812b 18fa 1209 ddd2 8103 061f 21f2 c765 7479 fecc c6e8 aa92 95b8 25ef ce2c a103
 0921 f65a c332 8782 d6d4 2d15 3947 15cd dd67 2e8c 8bbd e946 9399 8357 6432 182e 2b89 92ea c1f2 8b09 22a6 1946 8e66 4b19 81b1
 8be0 35be 3893 508b 0330 b7b0 fbe5 40a5 8b7c 29f3 20bb 925c abc7 24f2 1eda 02f0 d063 66dc 4e24 4d7b b7c1 4783 3472 e887 d9c6
 8a39 f0a6 d38f c58f 6499 c3c5 6f40 e9b6 e912 31e8 1854 5ffb 0068 41b7 c628 d9fa a2ad a2a5 6012 a468 9fcd 890a 5f2e f480 2231
 27fe b6e8 da5b 14a9 4f3e fc4f 15b8 0b47 a1de a573 3c89 2c3e c623 b173 1225 85e3 f556 9e63 22ef 07af d680 97f0 019f a9d8 1e1b
 08da 4271 9d8b 2308 e434 b51a e0c9 f045 a08a c2bf 2cf2 b91e 51f0 8097 967e cacb 78a9 5ef3 bbb7 ca13 9388 f61f abff bf47 a1ae
 4130 e52d 2cce 304d 981a a70e c224 b182 ee1f 1759 b47b 99f7 1b30 11cf 77c5 0945 82e1 9023 babf 5676 1658 a4d4 72af a559 e806
 70f3 0eaa c313 3ddf 9a88 b84e 1c75 483f 20f5 ed2f a56d f132 ec15 e63c 6da0 078a e1b4 1562 a0ac d22d d5cf 8bca 1a6c 9d11 53f4
 a17f 49f4 9cbe 3d14 5a08 227d f25f b797 1ea6 1432 33d3 5e3d e6ba 1ed6 14ab 30b5 1d5f 246b 20ee 9d55 5d65 d0d8 1182 be0d c9b0
 00ea b594 cd44 7ac4 d171 52d4 e84c 4c09 c1c4 3acb 8ed5 dabf 6ccd e114 cd12 a810 d935 8a93 cdd5 d385 5b09 c872 9025 75d1 b78e
 989c e635 7f52 bebf c6a5 7ded a1be 9e4c 7b13 7cad e89b 38e5 1525 c675 0c3c e220 0fd5 40ad d8e7 f5bb f3d6 faa7 1015 ba04 9d0c
 26a7 de49 745f 19dd acd1 baa2 d90d 1b97 223d d9fb 4165 a388 8467 88d8 9111 5b36 4360 c277 44af ea3e 936a 48b1 bd50 b8a9 6bf8
 cb9f d283 8c48 5895 d193 197b 9aba b7d0 673e af37 5d56 8aec 4972 6ac2 6882 81a8 24e7 56a9 db6e f46b 413c 9a59 3977 0af7 38f3
 c889 01ed 9c61 8113 4320 3ae1 71ce aaba 90da e360 d63a d166 7372 848a a34c d0a9 df1d 71a3 8d50 aebb 090a 5982 276f 5f6e bb83
 d4b9 92d5 fb9a aa26 405c 5570 ec22 2554 108b 1ed4 acb3 9e7a 98f8 10fc dadd 2606 d038 f2cb 8264 f816 9283 5209 6a25 9e9a 886a
 4d32 6fc1 31f3 69a0 2492 a18e 00bd 227d a917 5823 14bc c373 9f32 46b2 4bc5 e820 7b24 0c6e 4dce dcce 5827 cd7b a0d9 b5fd 8156
 e545 e098 b896 2f77 be76 4307 51bb 35b2 a32f 71cc f454 1c49 2467 7a82 1044 0c2b 3f84 08db 4c9a f1e9 bcf2 3374 c125 41da 2b18
 c5f6 fb5d 2717 53d5 0385 ed7a f40c e91d 8881 432d 687c 6832 010f da13 a7d9 4e85 0bfe 66ed 50f0 cfd8 e24e fb93 c6e4 0edd b3af
 ba54 ee13 f127 e3a3 0730 33f1 f302 f810 d1b0 d7d7 e1ba b243 6af1 cb9f f6c3 e489 0148 62a5 f6e0 4932 651a c1dc ee88 e2e0 fd47
Looking through the text above, I think I have found the password. I am just having trouble with a username.
Oh drats! They are onto us! We could get kicked out soon!
Quick! Print the username to the screen so we can close are backdoor and log into the account directly!
You have to find another way other than echo!

~/executables$ whoami
l33th4x0r
Perfect! One second!
Okay, I think I have got what we are looking for. I just need to to copy the file to a place we can read.
Try copying the file called TopSecret in tmp directory into the passwords folder.

~/executables$ cp /tmp/TopSecret ../passwords
Server shutdown in 10 seconds...
Quick! go read the file before we lose our connection!

~/executables$ cd ..

~/$ cd passwords

~/passwords$ ls
TopSecret

~/passwords$ cat TopSecret
Major General John M. Schofield's graduation address to the graduating class of 1879 at West Point is as follows: The discipline which makes the soldiers of a free country reliable in battle is not to be gained by harsh or tyrannical treatment.On the contrary, such treatment is far more likely to destroy than to make an army.It is possible to impart instruction and give commands in such a manner and such a tone of voice as to inspire in the soldier no feeling butan intense desire to obey, while the opposite manner and tone of voice cannot fail to excite strong resentment and a desire to disobey.The one mode or other of dealing with subordinates springs from a corresponding spirit in the breast of the commander.He who feels the respect which is due to others, cannot fail to inspire in them respect for himself, while he who feels,and hence manifests disrespect towards others, especially his subordinates, cannot fail to inspire hatred against himself.
picoCTF{CrUsHeD_It_9edaa84a}
```

FLAG - `picoCTF{CrUsHeD_It_9edaa84a}`
