# String Gem

__PROBLEM__

Can you see the flag inside it?
[gem](gem)

__SOLUTION__

So this was just a simple reversing task. All you have to do is check out the disassembled code of binary. I use [radare2](https://rada.re/r/) for most of the reversing. all you have to do is:
```bash
>>> r2 gem
[0x000006a0]> aaaa
[x] Analyze all flags starting with sym. and entry0 (aa)
[x] Analyze function calls (aac)
[x] Analyze len bytes of instructions for references (aar)
[x] Constructing a function name for fcn.* and sym.func.* functions (aan)
[x] Type matching analysis for all functions (afta)
[x] Emulate code to find computed references (aae)
[x] Analyze consecutive function (aat)
[0x000006a0]> s main
[0x000007aa]> pdf
            ;-- main:
/ (fcn) sym.main 143
|   sym.main (int argc, char **argv, char **envp);
|           ; var char *s1 @ rbp-0x40
|           ; var int canary @ rbp-0x8
|           ; STRING XREF from entry0 (0x6bd)
|           0x000007aa      55             push rbp
|           0x000007ab      4889e5         mov rbp, rsp
|           0x000007ae      4883ec40       sub rsp, 0x40
|           0x000007b2      64488b042528.  mov rax, qword fs:[0x28]    ; [0x28:8]=0x19e0 ; '('
|           0x000007bb      488945f8       mov qword [canary], rax
|           0x000007bf      31c0           xor eax, eax
|           0x000007c1      488d3d000100.  lea rdi, str.Give_me_the_flag_:: ; 0x8c8 ; "Give me the flag ::" ; const char *s
|           0x000007c8      e873feffff     call sym.imp.puts           ; int puts(const char *s)
|           0x000007cd      488d45c0       lea rax, [s1]
|           0x000007d1      4889c6         mov rsi, rax
|           0x000007d4      488d3d010100.  lea rdi, str.50s            ; 0x8dc ; "%50s" ; const char *format
|           0x000007db      b800000000     mov eax, 0
|           0x000007e0      e88bfeffff     call sym.imp.__isoc99_scanf ; int scanf(const char *format)
|           0x000007e5      488d45c0       lea rax, [s1]
|           0x000007e9      488d35f80000.  lea rsi, str.GLUG_y0u_c4n7_h1d3_57r1n65_1n_b1n4ry ; 0x8e8 ; "GLUG{y0u_c4n7_h1d3_57r1n65_1n_b1n4ry}" ; const char *s2
|           0x000007f0      4889c7         mov rdi, rax                ; const char *s1
|           0x000007f3      e868feffff     call sym.imp.strcmp         ; int strcmp(const char *s1, const char *s2)
|           0x000007f8      85c0           test eax, eax
|       ,=< 0x000007fa      7516           jne 0x812
|       |   0x000007fc      488d3d0b0100.  lea rdi, str.Yeah__you_got_it ; 0x90e ; "Yeah! you got it" ; const char *s
|       |   0x00000803      e838feffff     call sym.imp.puts           ; int puts(const char *s)
|       |   0x00000808      bf00000000     mov edi, 0                  ; int status
|       |   0x0000080d      e86efeffff     call sym.imp.exit           ; void exit(int status)
|       |   ; CODE XREF from sym.main (0x7fa)
|       `-> 0x00000812      488d3d060100.  lea rdi, str.Nope__that_will_not_work ; 0x91f ; "Nope, that will not work!" ; const char *s
|           0x00000819      e822feffff     call sym.imp.puts           ; int puts(const char *s)
|           0x0000081e      b800000000     mov eax, 0
|           0x00000823      488b55f8       mov rdx, qword [canary]
|           0x00000827      644833142528.  xor rdx, qword fs:[0x28]
|       ,=< 0x00000830      7405           je 0x837
|       |   0x00000832      e819feffff     call sym.imp.__stack_chk_fail ; void __stack_chk_fail(void)
|       |   ; CODE XREF from sym.main (0x830)
|       `-> 0x00000837      c9             leave
\           0x00000838      c3             ret
```

And there's our flag.

FLAG - `GLUG{y0u_c4n7_h1d3_57r1n65_1n_b1n4ry}`
