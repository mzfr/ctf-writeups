# Assembly-0

__PROBLEM__

What does asm0(0xb6,0xc6) return? Submit the flag as a hexadecimal value (starting with ‘0x’). NOTE: Your submission for this question will NOT be in the normal flag format. [Source](./intro_asm_rev.S) located in the directory at /problems/assembly-0_0_5a220faedfaf4fbf26e6771960d4a359.

__HINT__

basical assembly [tutorial](https://www.tutorialspoint.com/assembly_programming/assembly_basic_syntax.htm)
assembly [registers](https://www.tutorialspoint.com/assembly_programming/assembly_registers.htm)

__SOLUTION__

Hint was more then enough for this problem but if you want you can watch [this](https://www.youtube.com/watch?v=wLXIWKUWpSs) video.

Assembly code
```
.intel_syntax noprefix
.bits 32

.global asm0

asm0:
    push    ebp
    mov ebp,esp
    mov eax,DWORD PTR [ebp+0x8]
    mov ebx,DWORD PTR [ebp+0xc]
    mov eax,ebx
    mov esp,ebp
    pop ebp
    ret
```

we have to find the answer of asm0(0xb6, 0xc6). Looking at the code above we see that those two args are placed in eax and ebx. So answer to this problem will be 0xc6 Why? Because assembly functions always return value that is present in the eax register.

FLAG - `0xc6`
