# LoadSomeBits

__PROBLEM__

Can you find the flag encoded inside this [image](pico2018-special-logo.bmp)? You can also find the file in /problems/loadsomebits_2_c5bba4da53a839fcdda89e5203ac44d0 on the shell server.

__HINT__

Look through the Least Significant Bits for the image

If you interpret a binary sequence (seq) as ascii and then try interpreting the same binary sequence from an offset of 1 (seq[1:]) as ascii do you get something similar or completely different?

__SOLUTION__

First it is important to know what is [LSB](https://en.wikipedia.org/wiki/Bit_numbering). If you'll know what it is you'll be able to play with.

I wrote some code in python for this problem:

```
bits = ""
for seq in range(16):
    with open("pico2018-special-logo.bmp", "rb") as f:
        data = f.read()
        data = data[seq:]

        for c in data:
            lsb = str(c & 0x1)
            bits += lsb

        bytess = [chr(int(bits[i:i+8], 2)) for i in range(0, len(bits), 8)]
        lsbstr = "".join(bytess)

        if "picoCTF" in lsbstr:
            print(lsbstr)
            break
```

This will break when it encounters our flag.

FLAG - `picoCTF{st0r3d_iN_tH3_l345t_s1gn1f1c4nT_b1t5_2705826400}`
