# 7-Hide And Seek

__PROBLEM__

The reason that we took rick's PC memory dump is because there was a malware infection. Please find the malware process name (including the extension)

BEAWARE! There are only 3 attempts to get the right flag!

format: CTF{flag}

__SOLUTION__

I couldn't solve this one because I ran out of all the chances because I just tried all the output file name's of `malfind`

```bash
➜ vol.py -f OtterCTF.vmem --profile=Win7SP1x64 malfind
Volatility Foundation Volatility Framework 2.6
Process: WmiPrvSE.exe Pid: 2136 Address: 0x1170000
Vad Tag: VadS Protection: PAGE_EXECUTE_READWRITE
Flags: CommitCharge: 2, PrivateMemory: 1, Protection: 6

0x01170000  00 00 00 00 00 00 00 00 9d 88 3b aa 5a 4c 00 01   ..........;.ZL..
0x01170010  ee ff ee ff 00 00 00 00 28 01 17 01 00 00 00 00   ........(.......
0x01170020  28 01 17 01 00 00 00 00 00 00 17 01 00 00 00 00   (...............
0x01170030  00 00 17 01 00 00 00 00 80 00 00 00 00 00 00 00   ................

0x01170000 0000             ADD [EAX], AL
0x01170002 0000             ADD [EAX], AL
0x01170004 0000             ADD [EAX], AL
0x01170006 0000             ADD [EAX], AL
0x01170008 9d               POPF
0x01170009 883b             MOV [EBX], BH
0x0117000b aa               STOSB
0x0117000c 5a               POP EDX
0x0117000d 4c               DEC ESP
0x0117000e 0001             ADD [ECX], AL
0x01170010 ee               OUT DX, AL
0x01170011 ff               DB 0xff
0x01170012 ee               OUT DX, AL
0x01170013 ff00             INC DWORD [EAX]
0x01170015 0000             ADD [EAX], AL
0x01170017 0028             ADD [EAX], CH
0x01170019 0117             ADD [EDI], EDX
0x0117001b 0100             ADD [EAX], EAX
0x0117001d 0000             ADD [EAX], AL
0x0117001f 0028             ADD [EAX], CH
0x01170021 0117             ADD [EDI], EDX
0x01170023 0100             ADD [EAX], EAX
0x01170025 0000             ADD [EAX], AL
0x01170027 0000             ADD [EAX], AL
0x01170029 0017             ADD [EDI], DL
0x0117002b 0100             ADD [EAX], EAX
0x0117002d 0000             ADD [EAX], AL
0x0117002f 0000             ADD [EAX], AL
0x01170031 0017             ADD [EDI], DL
0x01170033 0100             ADD [EAX], EAX
0x01170035 0000             ADD [EAX], AL
0x01170037 008000000000     ADD [EAX+0x0], AL
0x0117003d 0000             ADD [EAX], AL
0x0117003f 00               DB 0x0

Process: WmiPrvSE.exe Pid: 2136 Address: 0x1850000
Vad Tag: VadS Protection: PAGE_EXECUTE_READWRITE
Flags: CommitCharge: 2, PrivateMemory: 1, Protection: 6

0x01850000  00 00 00 00 00 00 00 00 06 87 bd 8e 5d 19 00 01   ............]...
0x01850010  ee ff ee ff 00 00 00 00 28 01 85 01 00 00 00 00   ........(.......
0x01850020  28 01 85 01 00 00 00 00 00 00 85 01 00 00 00 00   (...............
0x01850030  00 00 85 01 00 00 00 00 80 00 00 00 00 00 00 00   ................

0x01850000 0000             ADD [EAX], AL
0x01850002 0000             ADD [EAX], AL
0x01850004 0000             ADD [EAX], AL
0x01850006 0000             ADD [EAX], AL
0x01850008 06               PUSH ES
0x01850009 87bd8e5d1900     XCHG [EBP+0x195d8e], EDI
0x0185000f 01ee             ADD ESI, EBP
0x01850011 ff               DB 0xff
0x01850012 ee               OUT DX, AL
0x01850013 ff00             INC DWORD [EAX]
0x01850015 0000             ADD [EAX], AL
0x01850017 0028             ADD [EAX], CH
0x01850019 018501000000     ADD [EBP+0x1], EAX
0x0185001f 0028             ADD [EAX], CH
0x01850021 018501000000     ADD [EBP+0x1], EAX
0x01850027 0000             ADD [EAX], AL
0x01850029 008501000000     ADD [EBP+0x1], AL
0x0185002f 0000             ADD [EAX], AL
0x01850031 008501000000     ADD [EBP+0x1], AL
0x01850037 008000000000     ADD [EAX+0x0], AL
0x0185003d 0000             ADD [EAX], AL
0x0185003f 00               DB 0x0

Process: explorer.exe Pid: 2728 Address: 0x1cb0000
Vad Tag: VadS Protection: PAGE_EXECUTE_READWRITE
Flags: CommitCharge: 16, MemCommit: 1, PrivateMemory: 1, Protection: 6

0x01cb0000  41 ba 80 00 00 00 48 b8 38 a1 9c ff fe 07 00 00   A.....H.8.......
0x01cb0010  48 ff 20 90 41 ba 81 00 00 00 48 b8 38 a1 9c ff   H...A.....H.8...
0x01cb0020  fe 07 00 00 48 ff 20 90 41 ba 82 00 00 00 48 b8   ....H...A.....H.
0x01cb0030  38 a1 9c ff fe 07 00 00 48 ff 20 90 41 ba 83 00   8.......H...A...

0x01cb0000 41               INC ECX
0x01cb0001 ba80000000       MOV EDX, 0x80
0x01cb0006 48               DEC EAX
0x01cb0007 b838a19cff       MOV EAX, 0xff9ca138
0x01cb000c fe07             INC BYTE [EDI]
0x01cb000e 0000             ADD [EAX], AL
0x01cb0010 48               DEC EAX
0x01cb0011 ff20             JMP DWORD [EAX]
0x01cb0013 90               NOP
0x01cb0014 41               INC ECX
0x01cb0015 ba81000000       MOV EDX, 0x81
0x01cb001a 48               DEC EAX
0x01cb001b b838a19cff       MOV EAX, 0xff9ca138
0x01cb0020 fe07             INC BYTE [EDI]
0x01cb0022 0000             ADD [EAX], AL
0x01cb0024 48               DEC EAX
0x01cb0025 ff20             JMP DWORD [EAX]
0x01cb0027 90               NOP
0x01cb0028 41               INC ECX
0x01cb0029 ba82000000       MOV EDX, 0x82
0x01cb002e 48               DEC EAX
0x01cb002f b838a19cff       MOV EAX, 0xff9ca138
0x01cb0034 fe07             INC BYTE [EDI]
0x01cb0036 0000             ADD [EAX], AL
0x01cb0038 48               DEC EAX
0x01cb0039 ff20             JMP DWORD [EAX]
0x01cb003b 90               NOP
0x01cb003c 41               INC ECX
0x01cb003d ba               DB 0xba
0x01cb003e 83               DB 0x83
0x01cb003f 00               DB 0x0

Process: explorer.exe Pid: 2728 Address: 0x3c30000
Vad Tag: VadS Protection: PAGE_EXECUTE_READWRITE
Flags: CommitCharge: 1, MemCommit: 1, PrivateMemory: 1, Protection: 6

0x03c30000  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
0x03c30010  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
0x03c30020  00 00 c3 03 00 00 00 00 00 00 00 00 00 00 00 00   ................
0x03c30030  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................

0x03c30000 0000             ADD [EAX], AL
0x03c30002 0000             ADD [EAX], AL
0x03c30004 0000             ADD [EAX], AL
0x03c30006 0000             ADD [EAX], AL
0x03c30008 0000             ADD [EAX], AL
0x03c3000a 0000             ADD [EAX], AL
0x03c3000c 0000             ADD [EAX], AL
0x03c3000e 0000             ADD [EAX], AL
0x03c30010 0000             ADD [EAX], AL
0x03c30012 0000             ADD [EAX], AL
0x03c30014 0000             ADD [EAX], AL
0x03c30016 0000             ADD [EAX], AL
0x03c30018 0000             ADD [EAX], AL
0x03c3001a 0000             ADD [EAX], AL
0x03c3001c 0000             ADD [EAX], AL
0x03c3001e 0000             ADD [EAX], AL
0x03c30020 0000             ADD [EAX], AL
0x03c30022 c3               RET
0x03c30023 0300             ADD EAX, [EAX]
0x03c30025 0000             ADD [EAX], AL
0x03c30027 0000             ADD [EAX], AL
0x03c30029 0000             ADD [EAX], AL
0x03c3002b 0000             ADD [EAX], AL
0x03c3002d 0000             ADD [EAX], AL
0x03c3002f 0000             ADD [EAX], AL
0x03c30031 0000             ADD [EAX], AL
0x03c30033 0000             ADD [EAX], AL
0x03c30035 0000             ADD [EAX], AL
0x03c30037 0000             ADD [EAX], AL
0x03c30039 0000             ADD [EAX], AL
0x03c3003b 0000             ADD [EAX], AL
0x03c3003d 0000             ADD [EAX], AL
0x03c3003f 00               DB 0x0

Process: BitTorrent.exe Pid: 2836 Address: 0x5730000
Vad Tag: VadS Protection: PAGE_EXECUTE_READWRITE
Flags: CommitCharge: 1, MemCommit: 1, PrivateMemory: 1, Protection: 6

0x05730000  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
0x05730010  00 00 73 05 00 00 00 00 00 00 00 00 00 00 00 00   ..s.............
0x05730020  10 00 73 05 00 00 00 00 00 00 00 00 00 00 00 00   ..s.............
0x05730030  20 00 73 05 00 00 00 00 00 00 00 00 00 00 00 00   ..s.............

0x05730000 0000             ADD [EAX], AL
0x05730002 0000             ADD [EAX], AL
0x05730004 0000             ADD [EAX], AL
0x05730006 0000             ADD [EAX], AL
0x05730008 0000             ADD [EAX], AL
0x0573000a 0000             ADD [EAX], AL
0x0573000c 0000             ADD [EAX], AL
0x0573000e 0000             ADD [EAX], AL
0x05730010 0000             ADD [EAX], AL
0x05730012 7305             JAE 0x5730019
0x05730014 0000             ADD [EAX], AL
0x05730016 0000             ADD [EAX], AL
0x05730018 0000             ADD [EAX], AL
0x0573001a 0000             ADD [EAX], AL
0x0573001c 0000             ADD [EAX], AL
0x0573001e 0000             ADD [EAX], AL
0x05730020 1000             ADC [EAX], AL
0x05730022 7305             JAE 0x5730029
0x05730024 0000             ADD [EAX], AL
0x05730026 0000             ADD [EAX], AL
0x05730028 0000             ADD [EAX], AL
0x0573002a 0000             ADD [EAX], AL
0x0573002c 0000             ADD [EAX], AL
0x0573002e 0000             ADD [EAX], AL
0x05730030 2000             AND [EAX], AL
0x05730032 7305             JAE 0x5730039
0x05730034 0000             ADD [EAX], AL
0x05730036 0000             ADD [EAX], AL
0x05730038 0000             ADD [EAX], AL
0x0573003a 0000             ADD [EAX], AL
0x0573003c 0000             ADD [EAX], AL
0x0573003e 0000             ADD [EAX], AL

Process: PresentationFo Pid: 724 Address: 0x5c0000
Vad Tag: VadS Protection: PAGE_EXECUTE_READWRITE
Flags: CommitCharge: 2, PrivateMemory: 1, Protection: 6

0x005c0000  00 00 00 00 00 00 00 00 95 a4 16 c2 d2 96 00 01   ................
0x005c0010  ee ff ee ff 00 00 00 00 28 01 5c 00 00 00 00 00   ........(.\.....
0x005c0020  28 01 5c 00 00 00 00 00 00 00 5c 00 00 00 00 00   (.\.......\.....
0x005c0030  00 00 5c 00 00 00 00 00 80 00 00 00 00 00 00 00   ..\.............

0x005c0000 0000             ADD [EAX], AL
0x005c0002 0000             ADD [EAX], AL
0x005c0004 0000             ADD [EAX], AL
0x005c0006 0000             ADD [EAX], AL
0x005c0008 95               XCHG EBP, EAX
0x005c0009 a4               MOVSB
0x005c000a 16               PUSH SS
0x005c000b c2d296           RET 0x96d2
0x005c000e 0001             ADD [ECX], AL
0x005c0010 ee               OUT DX, AL
0x005c0011 ff               DB 0xff
0x005c0012 ee               OUT DX, AL
0x005c0013 ff00             INC DWORD [EAX]
0x005c0015 0000             ADD [EAX], AL
0x005c0017 0028             ADD [EAX], CH
0x005c0019 015c0000         ADD [EAX+EAX+0x0], EBX
0x005c001d 0000             ADD [EAX], AL
0x005c001f 0028             ADD [EAX], CH
0x005c0021 015c0000         ADD [EAX+EAX+0x0], EBX
0x005c0025 0000             ADD [EAX], AL
0x005c0027 0000             ADD [EAX], AL
0x005c0029 005c0000         ADD [EAX+EAX+0x0], BL
0x005c002d 0000             ADD [EAX], AL
0x005c002f 0000             ADD [EAX], AL
0x005c0031 005c0000         ADD [EAX+EAX+0x0], BL
0x005c0035 0000             ADD [EAX], AL
0x005c0037 008000000000     ADD [EAX+0x0], AL
0x005c003d 0000             ADD [EAX], AL
0x005c003f 00               DB 0x0

Process: PresentationFo Pid: 724 Address: 0xa10000
Vad Tag: VadS Protection: PAGE_EXECUTE_READWRITE
Flags: CommitCharge: 37, PrivateMemory: 1, Protection: 6

0x00a10000  00 00 00 00 00 00 00 00 1f 9a 5b bc e5 93 00 01   ..........[.....
0x00a10010  ee ff ee ff 00 00 00 00 28 01 a1 00 00 00 00 00   ........(.......
0x00a10020  28 01 a1 00 00 00 00 00 00 00 a1 00 00 00 00 00   (...............
0x00a10030  00 00 a1 00 00 00 00 00 80 00 00 00 00 00 00 00   ................

0x00a10000 0000             ADD [EAX], AL
0x00a10002 0000             ADD [EAX], AL
0x00a10004 0000             ADD [EAX], AL
0x00a10006 0000             ADD [EAX], AL
0x00a10008 1f               POP DS
0x00a10009 9a5bbce5930001   CALL FAR 0x100:0x93e5bc5b
0x00a10010 ee               OUT DX, AL
0x00a10011 ff               DB 0xff
0x00a10012 ee               OUT DX, AL
0x00a10013 ff00             INC DWORD [EAX]
0x00a10015 0000             ADD [EAX], AL
0x00a10017 0028             ADD [EAX], CH
0x00a10019 01a100000000     ADD [ECX+0x0], ESP
0x00a1001f 0028             ADD [EAX], CH
0x00a10021 01a100000000     ADD [ECX+0x0], ESP
0x00a10027 0000             ADD [EAX], AL
0x00a10029 00a100000000     ADD [ECX+0x0], AH
0x00a1002f 0000             ADD [EAX], AL
0x00a10031 00a100000000     ADD [ECX+0x0], AH
0x00a10037 008000000000     ADD [EAX+0x0], AL
0x00a1003d 0000             ADD [EAX], AL
0x00a1003f 00               DB 0x0

Process: PresentationFo Pid: 724 Address: 0x7fffff10000
Vad Tag: VadS Protection: PAGE_EXECUTE_READWRITE
Flags: CommitCharge: 1, PrivateMemory: 1, Protection: 6

0x7fffff10000  00 00 00 00 00 00 00 00 78 0d 00 00 00 00 00 00   ........x.......
0x7fffff10010  0e 00 00 00 49 c7 c2 00 00 00 00 48 b8 e0 19 14   ....I......H....
0x7fffff10020  f9 fe 07 00 00 ff e0 49 c7 c2 01 00 00 00 48 b8   .......I......H.
0x7fffff10030  e0 19 14 f9 fe 07 00 00 ff e0 49 c7 c2 02 00 00   ..........I.....

0xfff10000 0000             ADD [EAX], AL
0xfff10002 0000             ADD [EAX], AL
0xfff10004 0000             ADD [EAX], AL
0xfff10006 0000             ADD [EAX], AL
0xfff10008 780d             JS 0xfff10017
0xfff1000a 0000             ADD [EAX], AL
0xfff1000c 0000             ADD [EAX], AL
0xfff1000e 0000             ADD [EAX], AL
0xfff10010 0e               PUSH CS
0xfff10011 0000             ADD [EAX], AL
0xfff10013 0049c7           ADD [ECX-0x39], CL
0xfff10016 c20000           RET 0x0
0xfff10019 0000             ADD [EAX], AL
0xfff1001b 48               DEC EAX
0xfff1001c b8e01914f9       MOV EAX, 0xf91419e0
0xfff10021 fe07             INC BYTE [EDI]
0xfff10023 0000             ADD [EAX], AL
0xfff10025 ffe0             JMP EAX
0xfff10027 49               DEC ECX
0xfff10028 c7c201000000     MOV EDX, 0x1
0xfff1002e 48               DEC EAX
0xfff1002f b8e01914f9       MOV EAX, 0xf91419e0
0xfff10034 fe07             INC BYTE [EDI]
0xfff10036 0000             ADD [EAX], AL
0xfff10038 ffe0             JMP EAX
0xfff1003a 49               DEC ECX
0xfff1003b c7               DB 0xc7
0xfff1003c c20200           RET 0x2
0xfff1003f 00               DB 0x0

Process: PresentationFo Pid: 724 Address: 0x7fffff20000
Vad Tag: VadS Protection: PAGE_EXECUTE_READWRITE
Flags: CommitCharge: 1, PrivateMemory: 1, Protection: 6

0x7fffff20000  d8 ff ff ff ff ff ff ff 08 00 00 00 00 00 00 00   ................
0x7fffff20010  01 00 00 00 00 00 00 00 00 00 08 01 38 00 00 00   ............8...
0x7fffff20020  15 00 0e 00 0e 00 00 00 f8 73 f3 f7 fe 07 00 00   .........s......
0x7fffff20030  00 10 b0 f7 fe 07 00 00 a8 ed b3 f7 fe 07 00 00   ................

0xfff20000 d8ff             FDIVR ST0, ST7
0xfff20002 ff               DB 0xff
0xfff20003 ff               DB 0xff
0xfff20004 ff               DB 0xff
0xfff20005 ff               DB 0xff
0xfff20006 ff               DB 0xff
0xfff20007 ff08             DEC DWORD [EAX]
0xfff20009 0000             ADD [EAX], AL
0xfff2000b 0000             ADD [EAX], AL
0xfff2000d 0000             ADD [EAX], AL
0xfff2000f 0001             ADD [ECX], AL
0xfff20011 0000             ADD [EAX], AL
0xfff20013 0000             ADD [EAX], AL
0xfff20015 0000             ADD [EAX], AL
0xfff20017 0000             ADD [EAX], AL
0xfff20019 0008             ADD [EAX], CL
0xfff2001b 0138             ADD [EAX], EDI
0xfff2001d 0000             ADD [EAX], AL
0xfff2001f 0015000e000e     ADD [0xe000e00], DL
0xfff20025 0000             ADD [EAX], AL
0xfff20027 00f8             ADD AL, BH
0xfff20029 73f3             JAE 0xfff2001e
0xfff2002b f7fe             IDIV ESI
0xfff2002d 07               POP ES
0xfff2002e 0000             ADD [EAX], AL
0xfff20030 0010             ADD [EAX], DL
0xfff20032 b0f7             MOV AL, 0xf7
0xfff20034 fe07             INC BYTE [EDI]
0xfff20036 0000             ADD [EAX], AL
0xfff20038 a8ed             TEST AL, 0xed
0xfff2003a b3f7             MOV BL, 0xf7
0xfff2003c fe07             INC BYTE [EDI]
0xfff2003e 0000             ADD [EAX], AL

Process: mscorsvw.exe Pid: 412 Address: 0xba0000
Vad Tag: VadS Protection: PAGE_EXECUTE_READWRITE
Flags: CommitCharge: 1, PrivateMemory: 1, Protection: 6

0x00ba0000  9e 17 1d ae b0 f0 00 01 ee ff ee ff 00 00 00 00   ................
0x00ba0010  a8 00 ba 00 a8 00 ba 00 00 00 ba 00 00 00 ba 00   ................
0x00ba0020  40 00 00 00 88 05 ba 00 00 00 be 00 3f 00 00 00   @...........?...
0x00ba0030  01 00 00 00 00 00 00 00 f0 0f ba 00 f0 0f ba 00   ................

0x00ba0000 9e               SAHF
0x00ba0001 17               POP SS
0x00ba0002 1daeb0f000       SBB EAX, 0xf0b0ae
0x00ba0007 01ee             ADD ESI, EBP
0x00ba0009 ff               DB 0xff
0x00ba000a ee               OUT DX, AL
0x00ba000b ff00             INC DWORD [EAX]
0x00ba000d 0000             ADD [EAX], AL
0x00ba000f 00a800ba00a8     ADD [EAX-0x57ff4600], CH
0x00ba0015 00ba000000ba     ADD [EDX-0x46000000], BH
0x00ba001b 0000             ADD [EAX], AL
0x00ba001d 00ba00400000     ADD [EDX+0x4000], BH
0x00ba0023 008805ba0000     ADD [EAX+0xba05], CL
0x00ba0029 00be003f0000     ADD [ESI+0x3f00], BH
0x00ba002f 0001             ADD [ECX], AL
0x00ba0031 0000             ADD [EAX], AL
0x00ba0033 0000             ADD [EAX], AL
0x00ba0035 0000             ADD [EAX], AL
0x00ba0037 00f0             ADD AL, DH
0x00ba0039 0f               DB 0xf
0x00ba003a ba00f00fba       MOV EDX, 0xba0ff000
0x00ba003f 00               DB 0x0

Process: mscorsvw.exe Pid: 412 Address: 0x16a0000
Vad Tag: VadS Protection: PAGE_EXECUTE_READWRITE
Flags: CommitCharge: 1, PrivateMemory: 1, Protection: 6

0x016a0000  87 79 5b b7 e7 b6 00 01 ee ff ee ff 00 00 00 00   .y[.............
0x016a0010  a8 00 6a 01 a8 00 6a 01 00 00 6a 01 00 00 6a 01   ..j...j...j...j.
0x016a0020  40 00 00 00 88 05 6a 01 00 00 6e 01 3f 00 00 00   @.....j...n.?...
0x016a0030  01 00 00 00 00 00 00 00 f0 0f 6a 01 f0 0f 6a 01   ..........j...j.

0x016a0000 87795b           XCHG [ECX+0x5b], EDI
0x016a0003 b7e7             MOV BH, 0xe7
0x016a0005 b600             MOV DH, 0x0
0x016a0007 01ee             ADD ESI, EBP
0x016a0009 ff               DB 0xff
0x016a000a ee               OUT DX, AL
0x016a000b ff00             INC DWORD [EAX]
0x016a000d 0000             ADD [EAX], AL
0x016a000f 00a8006a01a8     ADD [EAX-0x57fe9600], CH
0x016a0015 006a01           ADD [EDX+0x1], CH
0x016a0018 0000             ADD [EAX], AL
0x016a001a 6a01             PUSH 0x1
0x016a001c 0000             ADD [EAX], AL
0x016a001e 6a01             PUSH 0x1
0x016a0020 40               INC EAX
0x016a0021 0000             ADD [EAX], AL
0x016a0023 0088056a0100     ADD [EAX+0x16a05], CL
0x016a0029 006e01           ADD [ESI+0x1], CH
0x016a002c 3f               AAS
0x016a002d 0000             ADD [EAX], AL
0x016a002f 0001             ADD [ECX], AL
0x016a0031 0000             ADD [EAX], AL
0x016a0033 0000             ADD [EAX], AL
0x016a0035 0000             ADD [EAX], AL
0x016a0037 00f0             ADD AL, DH
0x016a0039 0f6a01           PUNPCKHDQ MM0, [ECX]
0x016a003c f00f6a01         PUNPCKHDQ MM0, [ECX]

Process: mscorsvw.exe Pid: 3124 Address: 0xaf0000
Vad Tag: VadS Protection: PAGE_EXECUTE_READWRITE
Flags: CommitCharge: 2, PrivateMemory: 1, Protection: 6

0x00af0000  00 00 00 00 00 00 00 00 79 38 fd bf bb 0c 00 01   ........y8......
0x00af0010  ee ff ee ff 00 00 00 00 28 01 af 00 00 00 00 00   ........(.......
0x00af0020  28 01 af 00 00 00 00 00 00 00 af 00 00 00 00 00   (...............
0x00af0030  00 00 af 00 00 00 00 00 80 00 00 00 00 00 00 00   ................

0x00af0000 0000             ADD [EAX], AL
0x00af0002 0000             ADD [EAX], AL
0x00af0004 0000             ADD [EAX], AL
0x00af0006 0000             ADD [EAX], AL
0x00af0008 7938             JNS 0xaf0042
0x00af000a fd               STD
0x00af000b bfbb0c0001       MOV EDI, 0x1000cbb
0x00af0010 ee               OUT DX, AL
0x00af0011 ff               DB 0xff
0x00af0012 ee               OUT DX, AL
0x00af0013 ff00             INC DWORD [EAX]
0x00af0015 0000             ADD [EAX], AL
0x00af0017 0028             ADD [EAX], CH
0x00af0019 01af00000000     ADD [EDI+0x0], EBP
0x00af001f 0028             ADD [EAX], CH
0x00af0021 01af00000000     ADD [EDI+0x0], EBP
0x00af0027 0000             ADD [EAX], AL
0x00af0029 00af00000000     ADD [EDI+0x0], CH
0x00af002f 0000             ADD [EAX], AL
0x00af0031 00af00000000     ADD [EDI+0x0], CH
0x00af0037 008000000000     ADD [EAX+0x0], AL
0x00af003d 0000             ADD [EAX], AL
0x00af003f 00               DB 0x0

Process: mscorsvw.exe Pid: 3124 Address: 0x1330000
Vad Tag: VadS Protection: PAGE_EXECUTE_READWRITE
Flags: CommitCharge: 2, PrivateMemory: 1, Protection: 6

0x01330000  00 00 00 00 00 00 00 00 22 0a 9a cc 73 9b 00 01   ........"...s...
0x01330010  ee ff ee ff 00 00 00 00 28 01 33 01 00 00 00 00   ........(.3.....
0x01330020  28 01 33 01 00 00 00 00 00 00 33 01 00 00 00 00   (.3.......3.....
0x01330030  00 00 33 01 00 00 00 00 80 00 00 00 00 00 00 00   ..3.............

0x01330000 0000             ADD [EAX], AL
0x01330002 0000             ADD [EAX], AL
0x01330004 0000             ADD [EAX], AL
0x01330006 0000             ADD [EAX], AL
0x01330008 220a             AND CL, [EDX]
0x0133000a 9acc739b0001ee   CALL FAR 0xee01:0x9b73cc
0x01330011 ff               DB 0xff
0x01330012 ee               OUT DX, AL
0x01330013 ff00             INC DWORD [EAX]
0x01330015 0000             ADD [EAX], AL
0x01330017 0028             ADD [EAX], CH
0x01330019 0133             ADD [EBX], ESI
0x0133001b 0100             ADD [EAX], EAX
0x0133001d 0000             ADD [EAX], AL
0x0133001f 0028             ADD [EAX], CH
0x01330021 0133             ADD [EBX], ESI
0x01330023 0100             ADD [EAX], EAX
0x01330025 0000             ADD [EAX], AL
0x01330027 0000             ADD [EAX], AL
0x01330029 0033             ADD [EBX], DH
0x0133002b 0100             ADD [EAX], EAX
0x0133002d 0000             ADD [EAX], AL
0x0133002f 0000             ADD [EAX], AL
0x01330031 0033             ADD [EBX], DH
0x01330033 0100             ADD [EAX], EAX
0x01330035 0000             ADD [EAX], AL
0x01330037 008000000000     ADD [EAX+0x0], AL
0x0133003d 0000             ADD [EAX], AL
0x0133003f 00               DB 0x0

Process: svchost.exe Pid: 3196 Address: 0x5d0000
Vad Tag: VadS Protection: PAGE_EXECUTE_READWRITE
Flags: CommitCharge: 64, MemCommit: 1, PrivateMemory: 1, Protection: 6

0x005d0000  56 57 53 55 48 83 ec 28 48 8b e9 ff e2 48 83 c4   VWSUH..(H....H..
0x005d0010  28 5d 5b 5f 5e c3 00 00 00 00 00 00 00 00 00 00   (][_^...........
0x005d0020  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
0x005d0030  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................

0x005d0000 56               PUSH ESI
0x005d0001 57               PUSH EDI
0x005d0002 53               PUSH EBX
0x005d0003 55               PUSH EBP
0x005d0004 48               DEC EAX
0x005d0005 83ec28           SUB ESP, 0x28
0x005d0008 48               DEC EAX
0x005d0009 8be9             MOV EBP, ECX
0x005d000b ffe2             JMP EDX
0x005d000d 48               DEC EAX
0x005d000e 83c428           ADD ESP, 0x28
0x005d0011 5d               POP EBP
0x005d0012 5b               POP EBX
0x005d0013 5f               POP EDI
0x005d0014 5e               POP ESI
0x005d0015 c3               RET
0x005d0016 0000             ADD [EAX], AL
0x005d0018 0000             ADD [EAX], AL
0x005d001a 0000             ADD [EAX], AL
0x005d001c 0000             ADD [EAX], AL
0x005d001e 0000             ADD [EAX], AL
0x005d0020 0000             ADD [EAX], AL
0x005d0022 0000             ADD [EAX], AL
0x005d0024 0000             ADD [EAX], AL
0x005d0026 0000             ADD [EAX], AL
0x005d0028 0000             ADD [EAX], AL
0x005d002a 0000             ADD [EAX], AL
0x005d002c 0000             ADD [EAX], AL
0x005d002e 0000             ADD [EAX], AL
0x005d0030 0000             ADD [EAX], AL
0x005d0032 0000             ADD [EAX], AL
0x005d0034 0000             ADD [EAX], AL
0x005d0036 0000             ADD [EAX], AL
0x005d0038 0000             ADD [EAX], AL
0x005d003a 0000             ADD [EAX], AL
0x005d003c 0000             ADD [EAX], AL
0x005d003e 0000             ADD [EAX], AL

Process: svchost.exe Pid: 3196 Address: 0x2440000
Vad Tag: VadS Protection: PAGE_EXECUTE_READWRITE
Flags: CommitCharge: 128, MemCommit: 1, PrivateMemory: 1, Protection: 6

0x02440000  20 00 00 00 e0 ff 07 00 0c 00 00 00 01 00 05 00   ................
0x02440010  00 42 00 50 00 30 00 70 00 60 00 00 00 00 00 00   .B.P.0.p.`......
0x02440020  48 8b 45 28 c7 00 00 00 00 00 c7 40 04 00 00 00   H.E(.......@....
0x02440030  00 48 8b 45 28 48 8d 40 08 48 89 c2 48 8b 45 20   .H.E(H.@.H..H.E.

0x02440000 2000             AND [EAX], AL
0x02440002 0000             ADD [EAX], AL
0x02440004 e0ff             LOOPNZ 0x2440005
0x02440006 07               POP ES
0x02440007 000c00           ADD [EAX+EAX], CL
0x0244000a 0000             ADD [EAX], AL
0x0244000c 0100             ADD [EAX], EAX
0x0244000e 0500004200       ADD EAX, 0x420000
0x02440013 50               PUSH EAX
0x02440014 0030             ADD [EAX], DH
0x02440016 007000           ADD [EAX+0x0], DH
0x02440019 60               PUSHA
0x0244001a 0000             ADD [EAX], AL
0x0244001c 0000             ADD [EAX], AL
0x0244001e 0000             ADD [EAX], AL
0x02440020 48               DEC EAX
0x02440021 8b4528           MOV EAX, [EBP+0x28]
0x02440024 c70000000000     MOV DWORD [EAX], 0x0
0x0244002a c7400400000000   MOV DWORD [EAX+0x4], 0x0
0x02440031 48               DEC EAX
0x02440032 8b4528           MOV EAX, [EBP+0x28]
0x02440035 48               DEC EAX
0x02440036 8d4008           LEA EAX, [EAX+0x8]
0x02440039 48               DEC EAX
0x0244003a 89c2             MOV EDX, EAX
0x0244003c 48               DEC EAX
0x0244003d 8b4520           MOV EAX, [EBP+0x20]

Process: svchost.exe Pid: 3196 Address: 0x4ce0000
Vad Tag: VadS Protection: PAGE_EXECUTE_READWRITE
Flags: CommitCharge: 256, MemCommit: 1, PrivateMemory: 1, Protection: 6

0x04ce0000  20 00 00 00 e0 ff 0f 00 0c 00 00 00 01 00 05 00   ................
0x04ce0010  00 42 00 50 00 30 00 70 00 60 00 00 00 00 00 00   .B.P.0.p.`......
0x04ce0020  ba fc ff ff ff 03 55 20 03 55 5c b9 04 00 1a 00   ......U..U\.....
0x04ce0030  4c 8b c5 ff 95 e0 37 00 00 8b 4d 24 89 08 48 8d   L.....7...M$..H.

0x04ce0000 2000             AND [EAX], AL
0x04ce0002 0000             ADD [EAX], AL
0x04ce0004 e0ff             LOOPNZ 0x4ce0005
0x04ce0006 0f000c00         STR WORD [EAX+EAX]
0x04ce000a 0000             ADD [EAX], AL
0x04ce000c 0100             ADD [EAX], EAX
0x04ce000e 0500004200       ADD EAX, 0x420000
0x04ce0013 50               PUSH EAX
0x04ce0014 0030             ADD [EAX], DH
0x04ce0016 007000           ADD [EAX+0x0], DH
0x04ce0019 60               PUSHA
0x04ce001a 0000             ADD [EAX], AL
0x04ce001c 0000             ADD [EAX], AL
0x04ce001e 0000             ADD [EAX], AL
0x04ce0020 bafcffffff       MOV EDX, 0xfffffffc
0x04ce0025 035520           ADD EDX, [EBP+0x20]
0x04ce0028 03555c           ADD EDX, [EBP+0x5c]
0x04ce002b b904001a00       MOV ECX, 0x1a0004
0x04ce0030 4c               DEC ESP
0x04ce0031 8bc5             MOV EAX, EBP
0x04ce0033 ff95e0370000     CALL DWORD [EBP+0x37e0]
0x04ce0039 8b4d24           MOV ECX, [EBP+0x24]
0x04ce003c 8908             MOV [EAX], ECX
0x04ce003e 48               DEC EAX
0x04ce003f 8d               DB 0x8d

Process: svchost.exe Pid: 3196 Address: 0x4de0000
Vad Tag: VadS Protection: PAGE_EXECUTE_READWRITE
Flags: CommitCharge: 256, MemCommit: 1, PrivateMemory: 1, Protection: 6

0x04de0000  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
0x04de0010  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
0x04de0020  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
0x04de0030  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................

0x04de0000 0000             ADD [EAX], AL
0x04de0002 0000             ADD [EAX], AL
0x04de0004 0000             ADD [EAX], AL
0x04de0006 0000             ADD [EAX], AL
0x04de0008 0000             ADD [EAX], AL
0x04de000a 0000             ADD [EAX], AL
0x04de000c 0000             ADD [EAX], AL
0x04de000e 0000             ADD [EAX], AL
0x04de0010 0000             ADD [EAX], AL
0x04de0012 0000             ADD [EAX], AL
0x04de0014 0000             ADD [EAX], AL
0x04de0016 0000             ADD [EAX], AL
0x04de0018 0000             ADD [EAX], AL
0x04de001a 0000             ADD [EAX], AL
0x04de001c 0000             ADD [EAX], AL
0x04de001e 0000             ADD [EAX], AL
0x04de0020 0000             ADD [EAX], AL
0x04de0022 0000             ADD [EAX], AL
0x04de0024 0000             ADD [EAX], AL
0x04de0026 0000             ADD [EAX], AL
0x04de0028 0000             ADD [EAX], AL
0x04de002a 0000             ADD [EAX], AL
0x04de002c 0000             ADD [EAX], AL
0x04de002e 0000             ADD [EAX], AL
0x04de0030 0000             ADD [EAX], AL
0x04de0032 0000             ADD [EAX], AL
0x04de0034 0000             ADD [EAX], AL
0x04de0036 0000             ADD [EAX], AL
0x04de0038 0000             ADD [EAX], AL
0x04de003a 0000             ADD [EAX], AL
0x04de003c 0000             ADD [EAX], AL
0x04de003e 0000             ADD [EAX], AL

Process: chrome.exe Pid: 4076 Address: 0x47d0000
Vad Tag: VadS Protection: PAGE_EXECUTE_READWRITE
Flags: CommitCharge: 1, MemCommit: 1, PrivateMemory: 1, Protection: 6

0x047d0000  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
0x047d0010  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
0x047d0020  00 00 7d 04 00 00 00 00 00 00 00 00 00 00 00 00   ..}.............
0x047d0030  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................

0x047d0000 0000             ADD [EAX], AL
0x047d0002 0000             ADD [EAX], AL
0x047d0004 0000             ADD [EAX], AL
0x047d0006 0000             ADD [EAX], AL
0x047d0008 0000             ADD [EAX], AL
0x047d000a 0000             ADD [EAX], AL
0x047d000c 0000             ADD [EAX], AL
0x047d000e 0000             ADD [EAX], AL
0x047d0010 0000             ADD [EAX], AL
0x047d0012 0000             ADD [EAX], AL
0x047d0014 0000             ADD [EAX], AL
0x047d0016 0000             ADD [EAX], AL
0x047d0018 0000             ADD [EAX], AL
0x047d001a 0000             ADD [EAX], AL
0x047d001c 0000             ADD [EAX], AL
0x047d001e 0000             ADD [EAX], AL
0x047d0020 0000             ADD [EAX], AL
0x047d0022 7d04             JGE 0x47d0028
0x047d0024 0000             ADD [EAX], AL
0x047d0026 0000             ADD [EAX], AL
0x047d0028 0000             ADD [EAX], AL
0x047d002a 0000             ADD [EAX], AL
0x047d002c 0000             ADD [EAX], AL
0x047d002e 0000             ADD [EAX], AL
0x047d0030 0000             ADD [EAX], AL
0x047d0032 0000             ADD [EAX], AL
0x047d0034 0000             ADD [EAX], AL
0x047d0036 0000             ADD [EAX], AL
0x047d0038 0000             ADD [EAX], AL
0x047d003a 0000             ADD [EAX], AL
0x047d003c 0000             ADD [EAX], AL
0x047d003e 0000             ADD [EAX], AL

Process: vmware-tray.ex Pid: 3720 Address: 0x670000
Vad Tag: VadS Protection: PAGE_EXECUTE_READWRITE
Flags: CommitCharge: 1, PrivateMemory: 1, Protection: 6

0x00670000  9c 4c 5b ae 8c 8a 00 01 ee ff ee ff 00 00 00 00   .L[.............
0x00670010  a8 00 67 00 a8 00 67 00 00 00 67 00 00 00 67 00   ..g...g...g...g.
0x00670020  40 00 00 00 88 05 67 00 00 00 6b 00 3f 00 00 00   @.....g...k.?...
0x00670030  01 00 00 00 00 00 00 00 f0 0f 67 00 f0 0f 67 00   ..........g...g.

0x00670000 9c               PUSHF
0x00670001 4c               DEC ESP
0x00670002 5b               POP EBX
0x00670003 ae               SCASB
0x00670004 8c8a0001eeff     MOV [EDX-0x11ff00], CS
0x0067000a ee               OUT DX, AL
0x0067000b ff00             INC DWORD [EAX]
0x0067000d 0000             ADD [EAX], AL
0x0067000f 00a8006700a8     ADD [EAX-0x57ff9900], CH
0x00670015 006700           ADD [EDI+0x0], AH
0x00670018 0000             ADD [EAX], AL
0x0067001a 670000           ADD [BX+SI], AL
0x0067001d 006700           ADD [EDI+0x0], AH
0x00670020 40               INC EAX
0x00670021 0000             ADD [EAX], AL
0x00670023 008805670000     ADD [EAX+0x6705], CL
0x00670029 006b00           ADD [EBX+0x0], CH
0x0067002c 3f               AAS
0x0067002d 0000             ADD [EAX], AL
0x0067002f 0001             ADD [ECX], AL
0x00670031 0000             ADD [EAX], AL
0x00670033 0000             ADD [EAX], AL
0x00670035 0000             ADD [EAX], AL
0x00670037 00f0             ADD AL, DH
0x00670039 0f6700           PACKUSWB MM0, [EAX]
0x0067003c f00f6700         PACKUSWB MM0, [EAX]

Process: vmware-tray.ex Pid: 3720 Address: 0x510000
Vad Tag: VadS Protection: PAGE_EXECUTE_READWRITE
Flags: CommitCharge: 23, PrivateMemory: 1, Protection: 6

0x00510000  f0 26 16 8e 6a 2f 00 01 ee ff ee ff 00 00 00 00   .&..j/..........
0x00510010  a8 00 51 00 a8 00 51 00 00 00 51 00 00 00 51 00   ..Q...Q...Q...Q.
0x00510020  40 00 00 00 88 05 51 00 00 00 55 00 29 00 00 00   @.....Q...U.)...
0x00510030  01 00 00 00 00 00 00 00 f0 6f 52 00 f0 6f 52 00   .........oR..oR.

0x00510000 f02616           PUSH SS
0x00510003 8e6a2f           MOV GS, [EDX+0x2f]
0x00510006 0001             ADD [ECX], AL
0x00510008 ee               OUT DX, AL
0x00510009 ff               DB 0xff
0x0051000a ee               OUT DX, AL
0x0051000b ff00             INC DWORD [EAX]
0x0051000d 0000             ADD [EAX], AL
0x0051000f 00a8005100a8     ADD [EAX-0x57ffaf00], CH
0x00510015 005100           ADD [ECX+0x0], DL
0x00510018 0000             ADD [EAX], AL
0x0051001a 51               PUSH ECX
0x0051001b 0000             ADD [EAX], AL
0x0051001d 005100           ADD [ECX+0x0], DL
0x00510020 40               INC EAX
0x00510021 0000             ADD [EAX], AL
0x00510023 008805510000     ADD [EAX+0x5105], CL
0x00510029 005500           ADD [EBP+0x0], DL
0x0051002c 2900             SUB [EAX], EAX
0x0051002e 0000             ADD [EAX], AL
0x00510030 0100             ADD [EAX], EAX
0x00510032 0000             ADD [EAX], AL
0x00510034 0000             ADD [EAX], AL
0x00510036 0000             ADD [EAX], AL
0x00510038 f06f             OUTS DX, DWORD [ESI]
0x0051003a 52               PUSH EDX
0x0051003b 00f0             ADD AL, DH
0x0051003d 6f               OUTS DX, DWORD [ESI]
0x0051003e 52               PUSH EDX
0x0051003f 00               DB 0x0

Process: vmware-tray.ex Pid: 3720 Address: 0xc00000
Vad Tag: VadS Protection: PAGE_EXECUTE_READWRITE
Flags: CommitCharge: 1, PrivateMemory: 1, Protection: 6

0x00c00000  33 d2 3c f0 3c cf 00 01 ee ff ee ff 00 00 00 00   3.<.<...........
0x00c00010  a8 00 c0 00 a8 00 c0 00 00 00 c0 00 00 00 c0 00   ................
0x00c00020  40 00 00 00 88 05 c0 00 00 00 c4 00 3f 00 00 00   @...........?...
0x00c00030  01 00 00 00 00 00 00 00 f0 0f c0 00 f0 0f c0 00   ................

0x00c00000 33d2             XOR EDX, EDX
0x00c00002 3cf0             CMP AL, 0xf0
0x00c00004 3ccf             CMP AL, 0xcf
0x00c00006 0001             ADD [ECX], AL
0x00c00008 ee               OUT DX, AL
0x00c00009 ff               DB 0xff
0x00c0000a ee               OUT DX, AL
0x00c0000b ff00             INC DWORD [EAX]
0x00c0000d 0000             ADD [EAX], AL
0x00c0000f 00a800c000a8     ADD [EAX-0x57ff4000], CH
0x00c00015 00c0             ADD AL, AL
0x00c00017 0000             ADD [EAX], AL
0x00c00019 00c0             ADD AL, AL
0x00c0001b 0000             ADD [EAX], AL
0x00c0001d 00c0             ADD AL, AL
0x00c0001f 004000           ADD [EAX+0x0], AL
0x00c00022 0000             ADD [EAX], AL
0x00c00024 8805c0000000     MOV [0xc0], AL
0x00c0002a c400             LES EAX, [EAX]
0x00c0002c 3f               AAS
0x00c0002d 0000             ADD [EAX], AL
0x00c0002f 0001             ADD [ECX], AL
0x00c00031 0000             ADD [EAX], AL
0x00c00033 0000             ADD [EAX], AL
0x00c00035 0000             ADD [EAX], AL
0x00c00037 00f0             ADD AL, DH
0x00c00039 0fc000           XADD [EAX], AL
0x00c0003c f00fc000         LOCK XADD [EAX], AL

Process: vmware-tray.ex Pid: 3720 Address: 0xa10000
Vad Tag: VadS Protection: PAGE_EXECUTE_READWRITE
Flags: CommitCharge: 1, PrivateMemory: 1, Protection: 6

0x00a10000  12 d2 1f 89 e6 fd 00 01 ee ff ee ff 00 00 00 00   ................
0x00a10010  a8 00 a1 00 a8 00 a1 00 00 00 a1 00 00 00 a1 00   ................
0x00a10020  40 00 00 00 88 05 a1 00 00 00 a5 00 3f 00 00 00   @...........?...
0x00a10030  01 00 00 00 00 00 00 00 f0 0f a1 00 f0 0f a1 00   ................

0x00a10000 12d2             ADC DL, DL
0x00a10002 1f               POP DS
0x00a10003 89e6             MOV ESI, ESP
0x00a10005 fd               STD
0x00a10006 0001             ADD [ECX], AL
0x00a10008 ee               OUT DX, AL
0x00a10009 ff               DB 0xff
0x00a1000a ee               OUT DX, AL
0x00a1000b ff00             INC DWORD [EAX]
0x00a1000d 0000             ADD [EAX], AL
0x00a1000f 00a800a100a8     ADD [EAX-0x57ff5f00], CH
0x00a10015 00a1000000a1     ADD [ECX-0x5f000000], AH
0x00a1001b 0000             ADD [EAX], AL
0x00a1001d 00a100400000     ADD [ECX+0x4000], AH
0x00a10023 008805a10000     ADD [EAX+0xa105], CL
0x00a10029 00a5003f0000     ADD [EBP+0x3f00], AH
0x00a1002f 0001             ADD [ECX], AL
0x00a10031 0000             ADD [EAX], AL
0x00a10033 0000             ADD [EAX], AL
0x00a10035 0000             ADD [EAX], AL
0x00a10037 00f0             ADD AL, DH
0x00a10039 0fa1             POP FS
0x00a1003b 00f0             ADD AL, DH
0x00a1003d 0fa1             POP FS
0x00a1003f 00               DB 0x0

Process: WebCompanionIn Pid: 3880 Address: 0x1a0000
Vad Tag: VadS Protection: PAGE_EXECUTE_READWRITE
Flags: CommitCharge: 1, PrivateMemory: 1, Protection: 6

0x001a0000  1e 31 9d e7 c5 1d 00 01 ee ff ee ff 00 00 00 00   .1..............
0x001a0010  a8 00 1a 00 a8 00 1a 00 00 00 1a 00 00 00 1a 00   ................
0x001a0020  40 00 00 00 88 05 1a 00 00 00 1e 00 3f 00 00 00   @...........?...
0x001a0030  01 00 00 00 00 00 00 00 f0 0f 1a 00 f0 0f 1a 00   ................

0x001a0000 1e               PUSH DS
0x001a0001 319de7c51d00     XOR [EBP+0x1dc5e7], EBX
0x001a0007 01ee             ADD ESI, EBP
0x001a0009 ff               DB 0xff
0x001a000a ee               OUT DX, AL
0x001a000b ff00             INC DWORD [EAX]
0x001a000d 0000             ADD [EAX], AL
0x001a000f 00a8001a00a8     ADD [EAX-0x57ffe600], CH
0x001a0015 001a             ADD [EDX], BL
0x001a0017 0000             ADD [EAX], AL
0x001a0019 001a             ADD [EDX], BL
0x001a001b 0000             ADD [EAX], AL
0x001a001d 001a             ADD [EDX], BL
0x001a001f 004000           ADD [EAX+0x0], AL
0x001a0022 0000             ADD [EAX], AL
0x001a0024 88051a000000     MOV [0x1a], AL
0x001a002a 1e               PUSH DS
0x001a002b 003f             ADD [EDI], BH
0x001a002d 0000             ADD [EAX], AL
0x001a002f 0001             ADD [ECX], AL
0x001a0031 0000             ADD [EAX], AL
0x001a0033 0000             ADD [EAX], AL
0x001a0035 0000             ADD [EAX], AL
0x001a0037 00f0             ADD AL, DH
0x001a0039 0f               DB 0xf
0x001a003a 1a00             SBB AL, [EAX]
0x001a003c f0               DB 0xf0
0x001a003d 0f               DB 0xf
0x001a003e 1a00             SBB AL, [EAX]

Process: WebCompanionIn Pid: 3880 Address: 0x7c0000
Vad Tag: VadS Protection: PAGE_EXECUTE_READWRITE
Flags: CommitCharge: 1, PrivateMemory: 1, Protection: 6

0x007c0000  78 a5 7c 82 a4 72 00 01 ee ff ee ff 00 00 00 00   x.|..r..........
0x007c0010  a8 00 7c 00 a8 00 7c 00 00 00 7c 00 00 00 7c 00   ..|...|...|...|.
0x007c0020  40 00 00 00 88 05 7c 00 00 00 80 00 3f 00 00 00   @.....|.....?...
0x007c0030  01 00 00 00 00 00 00 00 f0 0f 7c 00 f0 0f 7c 00   ..........|...|.

0x007c0000 78a5             JS 0x7bffa7
0x007c0002 7c82             JL 0x7bff86
0x007c0004 a4               MOVSB
0x007c0005 7200             JB 0x7c0007
0x007c0007 01ee             ADD ESI, EBP
0x007c0009 ff               DB 0xff
0x007c000a ee               OUT DX, AL
0x007c000b ff00             INC DWORD [EAX]
0x007c000d 0000             ADD [EAX], AL
0x007c000f 00a8007c00a8     ADD [EAX-0x57ff8400], CH
0x007c0015 007c0000         ADD [EAX+EAX+0x0], BH
0x007c0019 007c0000         ADD [EAX+EAX+0x0], BH
0x007c001d 007c0040         ADD [EAX+EAX+0x40], BH
0x007c0021 0000             ADD [EAX], AL
0x007c0023 0088057c0000     ADD [EAX+0x7c05], CL
0x007c0029 0080003f0000     ADD [EAX+0x3f00], AL
0x007c002f 0001             ADD [ECX], AL
0x007c0031 0000             ADD [EAX], AL
0x007c0033 0000             ADD [EAX], AL
0x007c0035 0000             ADD [EAX], AL
0x007c0037 00f0             ADD AL, DH
0x007c0039 0f               DB 0xf
0x007c003a 7c00             JL 0x7c003c
0x007c003c f0               DB 0xf0
0x007c003d 0f               DB 0xf
0x007c003e 7c00             JL 0x7c0040

Process: WebCompanionIn Pid: 3880 Address: 0x7ef40000
Vad Tag: VadS Protection: PAGE_EXECUTE_READWRITE
Flags: CommitCharge: 1, PrivateMemory: 1, Protection: 6

0x7ef40000  ec ff ff ff 04 00 00 00 01 00 00 00 00 00 08 01   ................
0x7ef40010  1c 00 00 00 15 00 0e 00 0e 00 00 00 8c 07 24 73   ..............$s
0x7ef40020  00 10 fd 72 5c 70 ff 72 2c 30 fd 72 00 00 00 00   ...r\p.r,0.r....
0x7ef40030  00 00 00 00 10 00 f3 7e 1a 00 f3 7e 24 00 f3 7e   .......~...~$..~

0x7ef40000 ec               IN AL, DX
0x7ef40001 ff               DB 0xff
0x7ef40002 ff               DB 0xff
0x7ef40003 ff0400           INC DWORD [EAX+EAX]
0x7ef40006 0000             ADD [EAX], AL
0x7ef40008 0100             ADD [EAX], EAX
0x7ef4000a 0000             ADD [EAX], AL
0x7ef4000c 0000             ADD [EAX], AL
0x7ef4000e 0801             OR [ECX], AL
0x7ef40010 1c00             SBB AL, 0x0
0x7ef40012 0000             ADD [EAX], AL
0x7ef40014 15000e000e       ADC EAX, 0xe000e00
0x7ef40019 0000             ADD [EAX], AL
0x7ef4001b 008c0724730010   ADD [EDI+EAX+0x10007324], CL
0x7ef40022 fd               STD
0x7ef40023 725c             JB 0x7ef40081
0x7ef40025 70ff             JO 0x7ef40026
0x7ef40027 722c             JB 0x7ef40055
0x7ef40029 30fd             XOR CH, BH
0x7ef4002b 7200             JB 0x7ef4002d
0x7ef4002d 0000             ADD [EAX], AL
0x7ef4002f 0000             ADD [EAX], AL
0x7ef40031 0000             ADD [EAX], AL
0x7ef40033 0010             ADD [EAX], DL
0x7ef40035 00f3             ADD BL, DH
0x7ef40037 7e1a             JLE 0x7ef40053
0x7ef40039 00f3             ADD BL, DH
0x7ef4003b 7e24             JLE 0x7ef40061
0x7ef4003d 00f3             ADD BL, DH
0x7ef4003f 7e               DB 0x7e

Process: WebCompanionIn Pid: 3880 Address: 0x7ef30000
Vad Tag: VadS Protection: PAGE_EXECUTE_READWRITE
Flags: CommitCharge: 1, PrivateMemory: 1, Protection: 6

0x7ef30000  00 00 00 00 97 19 00 00 00 00 00 00 0e 00 00 00   ................
0x7ef30010  68 00 00 00 00 e9 4a 09 89 81 68 01 00 00 00 e9   h.....J...h.....
0x7ef30020  40 09 89 81 68 02 00 00 00 e9 36 09 89 81 68 03   @...h.....6...h.
0x7ef30030  00 00 00 e9 2c 09 89 81 68 04 00 00 00 e9 22 09   ....,...h.....".

0x7ef30000 0000             ADD [EAX], AL
0x7ef30002 0000             ADD [EAX], AL
0x7ef30004 97               XCHG EDI, EAX
0x7ef30005 1900             SBB [EAX], EAX
0x7ef30007 0000             ADD [EAX], AL
0x7ef30009 0000             ADD [EAX], AL
0x7ef3000b 000e             ADD [ESI], CL
0x7ef3000d 0000             ADD [EAX], AL
0x7ef3000f 006800           ADD [EAX+0x0], CH
0x7ef30012 0000             ADD [EAX], AL
0x7ef30014 00e9             ADD CL, CH
0x7ef30016 4a               DEC EDX
0x7ef30017 098981680100     OR [ECX+0x16881], ECX
0x7ef3001d 0000             ADD [EAX], AL
0x7ef3001f e940098981       JMP 0x7c0964
0x7ef30024 6802000000       PUSH DWORD 0x2
0x7ef30029 e936098981       JMP 0x7c0964
0x7ef3002e 6803000000       PUSH DWORD 0x3
0x7ef30033 e92c098981       JMP 0x7c0964
0x7ef30038 6804000000       PUSH DWORD 0x4
0x7ef3003d e9               DB 0xe9
0x7ef3003e 2209             AND CL, [ECX]

Process: Lavasoft.WCAss Pid: 3496 Address: 0x580000
Vad Tag: VadS Protection: PAGE_EXECUTE_READWRITE
Flags: CommitCharge: 2, PrivateMemory: 1, Protection: 6

0x00580000  00 00 00 00 00 00 00 00 50 d6 10 d6 57 0e 00 01   ........P...W...
0x00580010  ee ff ee ff 00 00 00 00 28 01 58 00 00 00 00 00   ........(.X.....
0x00580020  28 01 58 00 00 00 00 00 00 00 58 00 00 00 00 00   (.X.......X.....
0x00580030  00 00 58 00 00 00 00 00 80 00 00 00 00 00 00 00   ..X.............

0x00580000 0000             ADD [EAX], AL
0x00580002 0000             ADD [EAX], AL
0x00580004 0000             ADD [EAX], AL
0x00580006 0000             ADD [EAX], AL
0x00580008 50               PUSH EAX
0x00580009 d6               SALC
0x0058000a 10d6             ADC DH, DL
0x0058000c 57               PUSH EDI
0x0058000d 0e               PUSH CS
0x0058000e 0001             ADD [ECX], AL
0x00580010 ee               OUT DX, AL
0x00580011 ff               DB 0xff
0x00580012 ee               OUT DX, AL
0x00580013 ff00             INC DWORD [EAX]
0x00580015 0000             ADD [EAX], AL
0x00580017 0028             ADD [EAX], CH
0x00580019 015800           ADD [EAX+0x0], EBX
0x0058001c 0000             ADD [EAX], AL
0x0058001e 0000             ADD [EAX], AL
0x00580020 2801             SUB [ECX], AL
0x00580022 58               POP EAX
0x00580023 0000             ADD [EAX], AL
0x00580025 0000             ADD [EAX], AL
0x00580027 0000             ADD [EAX], AL
0x00580029 005800           ADD [EAX+0x0], BL
0x0058002c 0000             ADD [EAX], AL
0x0058002e 0000             ADD [EAX], AL
0x00580030 0000             ADD [EAX], AL
0x00580032 58               POP EAX
0x00580033 0000             ADD [EAX], AL
0x00580035 0000             ADD [EAX], AL
0x00580037 008000000000     ADD [EAX+0x0], AL
0x0058003d 0000             ADD [EAX], AL
0x0058003f 00               DB 0x0

Process: Lavasoft.WCAss Pid: 3496 Address: 0x660000
Vad Tag: VadS Protection: PAGE_EXECUTE_READWRITE
Flags: CommitCharge: 50, PrivateMemory: 1, Protection: 6

0x00660000  00 00 00 00 00 00 00 00 aa 32 b3 a9 8f 81 00 01   .........2......
0x00660010  ee ff ee ff 00 00 00 00 28 01 66 00 00 00 00 00   ........(.f.....
0x00660020  28 01 66 00 00 00 00 00 00 00 66 00 00 00 00 00   (.f.......f.....
0x00660030  00 00 66 00 00 00 00 00 80 00 00 00 00 00 00 00   ..f.............

0x00660000 0000             ADD [EAX], AL
0x00660002 0000             ADD [EAX], AL
0x00660004 0000             ADD [EAX], AL
0x00660006 0000             ADD [EAX], AL
0x00660008 aa               STOSB
0x00660009 32b3a98f8100     XOR DH, [EBX+0x818fa9]
0x0066000f 01ee             ADD ESI, EBP
0x00660011 ff               DB 0xff
0x00660012 ee               OUT DX, AL
0x00660013 ff00             INC DWORD [EAX]
0x00660015 0000             ADD [EAX], AL
0x00660017 0028             ADD [EAX], CH
0x00660019 016600           ADD [ESI+0x0], ESP
0x0066001c 0000             ADD [EAX], AL
0x0066001e 0000             ADD [EAX], AL
0x00660020 2801             SUB [ECX], AL
0x00660022 660000           ADD [EAX], AL
0x00660025 0000             ADD [EAX], AL
0x00660027 0000             ADD [EAX], AL
0x00660029 006600           ADD [ESI+0x0], AH
0x0066002c 0000             ADD [EAX], AL
0x0066002e 0000             ADD [EAX], AL
0x00660030 0000             ADD [EAX], AL
0x00660032 660000           ADD [EAX], AL
0x00660035 0000             ADD [EAX], AL
0x00660037 008000000000     ADD [EAX+0x0], AL
0x0066003d 0000             ADD [EAX], AL
0x0066003f 00               DB 0x0

Process: Lavasoft.WCAss Pid: 3496 Address: 0x7fffff10000
Vad Tag: VadS Protection: PAGE_EXECUTE_READWRITE
Flags: CommitCharge: 1, PrivateMemory: 1, Protection: 6

0x7fffff10000  d8 ff ff ff ff ff ff ff 08 00 00 00 00 00 00 00   ................
0x7fffff10010  01 00 00 00 00 00 00 00 00 00 08 01 38 00 00 00   ............8...
0x7fffff10020  15 00 0e 00 0e 00 00 00 f8 73 f3 f7 fe 07 00 00   .........s......
0x7fffff10030  00 10 b0 f7 fe 07 00 00 a8 ed b3 f7 fe 07 00 00   ................

0xfff10000 d8ff             FDIVR ST0, ST7
0xfff10002 ff               DB 0xff
0xfff10003 ff               DB 0xff
0xfff10004 ff               DB 0xff
0xfff10005 ff               DB 0xff
0xfff10006 ff               DB 0xff
0xfff10007 ff08             DEC DWORD [EAX]
0xfff10009 0000             ADD [EAX], AL
0xfff1000b 0000             ADD [EAX], AL
0xfff1000d 0000             ADD [EAX], AL
0xfff1000f 0001             ADD [ECX], AL
0xfff10011 0000             ADD [EAX], AL
0xfff10013 0000             ADD [EAX], AL
0xfff10015 0000             ADD [EAX], AL
0xfff10017 0000             ADD [EAX], AL
0xfff10019 0008             ADD [EAX], CL
0xfff1001b 0138             ADD [EAX], EDI
0xfff1001d 0000             ADD [EAX], AL
0xfff1001f 0015000e000e     ADD [0xe000e00], DL
0xfff10025 0000             ADD [EAX], AL
0xfff10027 00f8             ADD AL, BH
0xfff10029 73f3             JAE 0xfff1001e
0xfff1002b f7fe             IDIV ESI
0xfff1002d 07               POP ES
0xfff1002e 0000             ADD [EAX], AL
0xfff10030 0010             ADD [EAX], DL
0xfff10032 b0f7             MOV AL, 0xf7
0xfff10034 fe07             INC BYTE [EDI]
0xfff10036 0000             ADD [EAX], AL
0xfff10038 a8ed             TEST AL, 0xed
0xfff1003a b3f7             MOV BL, 0xf7
0xfff1003c fe07             INC BYTE [EDI]
0xfff1003e 0000             ADD [EAX], AL

Process: Lavasoft.WCAss Pid: 3496 Address: 0x7fffff00000
Vad Tag: VadS Protection: PAGE_EXECUTE_READWRITE
Flags: CommitCharge: 1, PrivateMemory: 1, Protection: 6

0x7fffff00000  00 00 00 00 00 00 00 00 78 0d 00 00 00 00 00 00   ........x.......
0x7fffff00010  0e 00 00 00 49 c7 c2 00 00 00 00 48 b8 e0 19 14   ....I......H....
0x7fffff00020  f9 fe 07 00 00 ff e0 49 c7 c2 01 00 00 00 48 b8   .......I......H.
0x7fffff00030  e0 19 14 f9 fe 07 00 00 ff e0 49 c7 c2 02 00 00   ..........I.....

0xfff00000 0000             ADD [EAX], AL
0xfff00002 0000             ADD [EAX], AL
0xfff00004 0000             ADD [EAX], AL
0xfff00006 0000             ADD [EAX], AL
0xfff00008 780d             JS 0xfff00017
0xfff0000a 0000             ADD [EAX], AL
0xfff0000c 0000             ADD [EAX], AL
0xfff0000e 0000             ADD [EAX], AL
0xfff00010 0e               PUSH CS
0xfff00011 0000             ADD [EAX], AL
0xfff00013 0049c7           ADD [ECX-0x39], CL
0xfff00016 c20000           RET 0x0
0xfff00019 0000             ADD [EAX], AL
0xfff0001b 48               DEC EAX
0xfff0001c b8e01914f9       MOV EAX, 0xf91419e0
0xfff00021 fe07             INC BYTE [EDI]
0xfff00023 0000             ADD [EAX], AL
0xfff00025 ffe0             JMP EAX
0xfff00027 49               DEC ECX
0xfff00028 c7c201000000     MOV EDX, 0x1
0xfff0002e 48               DEC EAX
0xfff0002f b8e01914f9       MOV EAX, 0xf91419e0
0xfff00034 fe07             INC BYTE [EDI]
0xfff00036 0000             ADD [EAX], AL
0xfff00038 ffe0             JMP EAX
0xfff0003a 49               DEC ECX
0xfff0003b c7               DB 0xc7
0xfff0003c c20200           RET 0x2
0xfff0003f 00               DB 0x0

Process: WebCompanion.e Pid: 3856 Address: 0x1f0000
Vad Tag: VadS Protection: PAGE_EXECUTE_READWRITE
Flags: CommitCharge: 1, PrivateMemory: 1, Protection: 6

0x001f0000  2e 7f f0 8b 0a 71 00 01 ee ff ee ff 00 00 00 00   .....q..........
0x001f0010  a8 00 1f 00 a8 00 1f 00 00 00 1f 00 00 00 1f 00   ................
0x001f0020  40 00 00 00 88 05 1f 00 00 00 23 00 3f 00 00 00   @.........#.?...
0x001f0030  01 00 00 00 00 00 00 00 f0 0f 1f 00 f0 0f 1f 00   ................

0x001f0000 2e7ff0           JG 0x1efff3 ;NOT TAKEN
0x001f0003 8b0a             MOV ECX, [EDX]
0x001f0005 7100             JNO 0x1f0007
0x001f0007 01ee             ADD ESI, EBP
0x001f0009 ff               DB 0xff
0x001f000a ee               OUT DX, AL
0x001f000b ff00             INC DWORD [EAX]
0x001f000d 0000             ADD [EAX], AL
0x001f000f 00a8001f00a8     ADD [EAX-0x57ffe100], CH
0x001f0015 001f             ADD [EDI], BL
0x001f0017 0000             ADD [EAX], AL
0x001f0019 001f             ADD [EDI], BL
0x001f001b 0000             ADD [EAX], AL
0x001f001d 001f             ADD [EDI], BL
0x001f001f 004000           ADD [EAX+0x0], AL
0x001f0022 0000             ADD [EAX], AL
0x001f0024 88051f000000     MOV [0x1f], AL
0x001f002a 2300             AND EAX, [EAX]
0x001f002c 3f               AAS
0x001f002d 0000             ADD [EAX], AL
0x001f002f 0001             ADD [ECX], AL
0x001f0031 0000             ADD [EAX], AL
0x001f0033 0000             ADD [EAX], AL
0x001f0035 0000             ADD [EAX], AL
0x001f0037 00f0             ADD AL, DH
0x001f0039 0f1f00           NOP DWORD [EAX]
0x001f003c f00f1f00         NOP DWORD [EAX]

Process: WebCompanion.e Pid: 3856 Address: 0x7d0000
Vad Tag: VadS Protection: PAGE_EXECUTE_READWRITE
Flags: CommitCharge: 1, PrivateMemory: 1, Protection: 6

0x007d0000  01 a0 33 b8 02 5c 00 01 ee ff ee ff 00 00 00 00   ..3..\..........
0x007d0010  a8 00 7d 00 a8 00 7d 00 00 00 7d 00 00 00 7d 00   ..}...}...}...}.
0x007d0020  40 00 00 00 88 05 7d 00 00 00 81 00 3f 00 00 00   @.....}.....?...
0x007d0030  01 00 00 00 00 00 00 00 f0 0f 7d 00 f0 0f 7d 00   ..........}...}.

0x007d0000 01a033b8025c     ADD [EAX+0x5c02b833], ESP
0x007d0006 0001             ADD [ECX], AL
0x007d0008 ee               OUT DX, AL
0x007d0009 ff               DB 0xff
0x007d000a ee               OUT DX, AL
0x007d000b ff00             INC DWORD [EAX]
0x007d000d 0000             ADD [EAX], AL
0x007d000f 00a8007d00a8     ADD [EAX-0x57ff8300], CH
0x007d0015 007d00           ADD [EBP+0x0], BH
0x007d0018 0000             ADD [EAX], AL
0x007d001a 7d00             JGE 0x7d001c
0x007d001c 0000             ADD [EAX], AL
0x007d001e 7d00             JGE 0x7d0020
0x007d0020 40               INC EAX
0x007d0021 0000             ADD [EAX], AL
0x007d0023 0088057d0000     ADD [EAX+0x7d05], CL
0x007d0029 0081003f0000     ADD [ECX+0x3f00], AL
0x007d002f 0001             ADD [ECX], AL
0x007d0031 0000             ADD [EAX], AL
0x007d0033 0000             ADD [EAX], AL
0x007d0035 0000             ADD [EAX], AL
0x007d0037 00f0             ADD AL, DH
0x007d0039 0f               DB 0xf
0x007d003a 7d00             JGE 0x7d003c
0x007d003c f0               DB 0xf0
0x007d003d 0f               DB 0xf
0x007d003e 7d00             JGE 0x7d0040

Process: WebCompanion.e Pid: 3856 Address: 0x4990000
Vad Tag: VadS Protection: PAGE_EXECUTE_READWRITE
Flags: CommitCharge: 27, PrivateMemory: 1, Protection: 6

0x04990000  13 e6 17 8b 1b 43 00 01 ee ff ee ff 00 00 00 00   .....C..........
0x04990010  a8 00 99 04 a8 00 99 04 00 00 99 04 00 00 99 04   ................
0x04990020  40 00 00 00 88 05 99 04 00 00 9d 04 25 00 00 00   @...........%...
0x04990030  01 00 00 00 00 00 00 00 f0 af 9a 04 f0 af 9a 04   ................

0x04990000 13e6             ADC ESP, ESI
0x04990002 17               POP SS
0x04990003 8b1b             MOV EBX, [EBX]
0x04990005 43               INC EBX
0x04990006 0001             ADD [ECX], AL
0x04990008 ee               OUT DX, AL
0x04990009 ff               DB 0xff
0x0499000a ee               OUT DX, AL
0x0499000b ff00             INC DWORD [EAX]
0x0499000d 0000             ADD [EAX], AL
0x0499000f 00a8009904a8     ADD [EAX-0x57fb6700], CH
0x04990015 009904000099     ADD [ECX-0x66fffffc], BL
0x0499001b 0400             ADD AL, 0x0
0x0499001d 009904400000     ADD [ECX+0x4004], BL
0x04990023 008805990400     ADD [EAX+0x49905], CL
0x04990029 009d04250000     ADD [EBP+0x2504], BL
0x0499002f 0001             ADD [ECX], AL
0x04990031 0000             ADD [EAX], AL
0x04990033 0000             ADD [EAX], AL
0x04990035 0000             ADD [EAX], AL
0x04990037 00f0             ADD AL, DH
0x04990039 af               SCASD
0x0499003a 9a               DB 0x9a
0x0499003b 04f0             ADD AL, 0xf0
0x0499003d af               SCASD
0x0499003e 9a               DB 0x9a
0x0499003f 04               DB 0x4
```
But for your sake you can read how to solve this one here: https://github.com/aadityapurani/My-CTF-Solutions/blob/master/otterctf-2018/memory-forensics/HideAndSeek.md
