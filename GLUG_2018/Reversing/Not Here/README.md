# Not Here

__PROBLEM__

Flag is supposed to be here
Download the binary file below.
[flagger](flagger)


__SOLUTION__

Again let just start with radare2.

```bash
➜ r2 flagger
 -- No such file or directory.
[0x000005a0]> aaaa
[x] Analyze all flags starting with sym. and entry0 (aa)
[x] Analyze function calls (aac)
[x] Analyze len bytes of instructions for references (aar)
[x] Constructing a function name for fcn.* and sym.func.* functions (aan)
[x] Type matching analysis for all functions (afta)
[x] Emulate code to find computed references (aae)
[x] Analyze consecutive function (aat)
[0x000005a0]> s main
[0x0000075a]> pdf
            ;-- main:
/ (fcn) sym.main 35
|   sym.main (int argc, char **argv, char **envp);
|           ; STRING XREF from entry0 (0x5bd)
|           0x0000075a      55             push rbp
|           0x0000075b      4889e5         mov rbp, rsp
|           0x0000075e      488d3da10000.  lea rdi, str.No_flags_Here  ; 0x806 ; "No flags Here!" ; const char *s
|           0x00000765      e806feffff     call sym.imp.puts           ; int puts(const char *s)
|           0x0000076a      488d3da40000.  lea rdi, [0x00000815]       ; "  \n" ; const char *s
|           0x00000771      e8fafdffff     call sym.imp.puts           ; int puts(const char *s)
|           0x00000776      b800000000     mov eax, 0
|           0x0000077b      5d             pop rbp
\           0x0000077c      c3             ret
[0x0000075a]> s sym.imp.puts
[0x00000570]> pdf
/ (fcn) sym.imp.puts 6
|   sym.imp.puts (const char *s);
|           ; CALL XREFS from sym.main (0x765, 0x771)
\           0x00000570      ff25520a2000   jmp qword reloc.puts        ; [0x200fc8:8]=0x576 ; "v\x05"
[0x00000570]> psbi 0x00000570
0x00000570 %R
0x00000575 h
0x00000577 %J
0x00000585 h
0x00000588 %b
0x00000595 f
0x00000598 1I^HHPTL:
0x000005b4 H
0x000005bb H=
0x000005c2
0x000005c9 D
0x000005ce H=9
0x000005d6 UH1
0x000005de H9HtH
0x000005ed Ht]f.
0x000005fb ]@
0x00000605 f.
0x0000060b H=
0x00000616 H5
0x0000061d UH)HHHH?HHtH
0x0000063e Ht]f
0x0000064b ]@
0x00000655 f.
0x0000065b =
0x00000665 u/H=
0x0000066f UHtH=
0x0000067d H
0x0000068d ]
0x00000694 fD
0x0000069e UH]fUHH@dH%(
0x000006b8 HE1EGELEUEGE{E7EhE1E5E_E1E5E_E4ElE5E0E_E4E_EcElE4E5E5E1EcE}E
0x00000734 H
0x00000739 HEHEHUdH3%(
0x0000074e t(UHH=
0x00000762 H=
0x0000076e ]
0x0000077f AWAVIAUATL%
0x00000791 UH-
0x00000799 SAIL)HHHt 1
0x000007bb LLDAHH9uH[]A\A]A^A_f.
0x000007eb HH
0x000007fd A
0x00000805 No flags Here!
0x00000814
0x00000818 ;@
0x00000821 D
0x0000082d t
0x00000835 \
0x0000083d >
0x0000084d d
0x00000856 T
0x0000085e zR
0x0000086b x
0x00000879  +
0x00000885 zR
0x0000089b x
0x000008a6 $
0x000008a9 0
0x000008b5 FJw
0x000008c4 ?;*3$"
0x000008cc D
0x000008d5 \
0x000008ed AC
0x00000906 |
0x0000090d J#
0x00000915 AC^
0x00000925 D
0x00000929 Pe
0x00000935 BBE B(H0H8M@r8A0A(B BBB
0x0000096f x
```
See a big string that looks like a flag. Yes `HE1EGELEUEGE{E7EhE1E5E_E1E5E_E4ElE5E0E_E4E_EcElE4E5E5E1EcE}E` this one.

Just clean that string up and you'll have it. But what happened there? Nothing all we did was start checked out the main function and since there wasn't much happening. we check out the the other function i.e `sym.imp.puts`

FLAG - `GLUG{7h15_15_4l50_4_cl4551c}`
