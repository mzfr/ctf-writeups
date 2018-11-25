# YEAH RIGHT

__PROBLEM__

Difficulty: very easy
What an insensitive little program.
Show it who's boss!

nc 18.224.3.130 12345

[yeahright](yeahright) and [flag](flag)

__HINT__

Notice anything left inside the program?

__SOLUTION__

Since it was a reversing problem first thing I did was used rabin2 to chekc all the strings

```bash
➜ rabin2 -z yeahright
[Strings]
Num Paddr      Vaddr      Len Size Section  Type  String
000 0x00000a98 0x00000a98  40  41 (.rodata) ascii 7h3_m057_53cr37357_p455w0rd_y0u_3v3r_54w
001 0x00000ac1 0x00000ac1  20  21 (.rodata) ascii *Ahem*... password?
002 0x00000ad6 0x00000ad6  10  11 (.rodata) ascii yeahright!
003 0x00000ae1 0x00000ae1  15  16 (.rodata) ascii /bin/cat ./flag
```

We can see the password

Connecting to the service and give the password we get the flag.

FLAG - `TUCTF{n07_my_fl46_n07_my_pr0bl3m}`
