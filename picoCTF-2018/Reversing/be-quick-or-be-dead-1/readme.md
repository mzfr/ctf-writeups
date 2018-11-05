# be-quick-or-be-dead-1

__PROBLEMS__

You find this when searching for some music, which leads you to [be-quick-or-be-dead-1](./be-quick-or-be-dead-1). Can you run it fast enough? You can also find the executable in /problems/be-quick-or-be-dead-1_4_98374389c5652d0b16055427532f098f.

__HINT__

What will the key finally be?


__SOLUTION__

Just load it in radare2 `r2 ./be-quick-or-be-dead-1`

```
[0x004005a0]> aaaa
[0x004005a0]> pdf @ sym.calculate_key
/ (fcn) sym.calculate_key 29
|   sym.calculate_key ();
|           ; var unsigned int local_4h @ rbp-0x4
|           ; CALL XREF from sym.get_key (0x4007a9)
|           0x00400706      55             push rbp
|           0x00400707      4889e5         mov rbp, rsp
|           0x0040070a      c745fc8b32c3.  mov dword [local_4h], 0x75c3328b
|           ; CODE XREF from sym.calculate_key (0x40071c)
|       .-> 0x00400711      8345fc01       add dword [local_4h], 1
|       :   0x00400715      817dfc166586.  cmp dword [local_4h], 0xeb866516 ; [0xeb866516:4]=-1
|       `=< 0x0040071c      75f3           jne 0x400711
|           0x0040071e      8b45fc         mov eax, dword [local_4h]
|           0x00400721      5d             pop rbp
\           0x00400722      c3             ret
```

We can see that this function start with `0x75c3328b` and decrements it until its equal to `0xeb866516`. To speed up this function we can change the value to final value minus 1.

We can do that using radare2
```
[0x004005a0]> oo+
[0x004005a0]> s 0x0040070a
[0x0040070a]> pd 1
|           0x0040070a      c745fc8b32c3.  mov dword [local_4h], 0x75c3328b
[0x0040070a]> wa mov dword [rbp-0x4], 0xeb866515
Written 7 byte(s) (mov dword [rbp-0x4], 0xeb866515) = wx c745fc156586eb
```

Patching is done. Now if you'll run the binary again it will give you the flag.

FLAG - `picoCTF{why_bother_doing_unnecessary_computation_402ca676}`
