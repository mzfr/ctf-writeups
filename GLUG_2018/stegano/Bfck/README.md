# Bfck

__PROBLEM__

You walk past the bin,
You do the sin.
Bin is not the way,
Walk it by the way.

Here is a Image, Now give me the flag.
[stromwalk.jpg](stromwalk.jpg)

__SOLUTION__

Notice those `bin` and `walk` in the question well it refers to [binwalk](https://github.com/ReFirmLabs/binwalk).
So simply run binwalk on the given image and we see:

```
➜ binwalk stromwalk.jpg

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             JPEG image data, JFIF standard 1.02
30            0x1E            TIFF image data, little-endian offset of first image directory: 8
451           0x1C3           Unix path: /www.w3.org/1999/02/22-rdf-syntax-ns#">
899           0x383           Unix path: /purl.org/dc/elements/1.1/">
1327          0x52F           Unix path: /ns.adobe.com/xap/1.0/mm/">
29457         0x7311          Zip archive data, at least v2.0 to extract, compressed size: 3088, uncompressed size: 3129, name: qrcode.png
32693         0x7FB5          End of Zip archive
```

Well there's a hidden ZIP and an image file there. So just extract them using binwalk
```
>>> binwalk -e stromwalk.jpg
DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             JPEG image data, JFIF standard 1.02
30            0x1E            TIFF image data, little-endian offset of first image directory: 8
451           0x1C3           Unix path: /www.w3.org/1999/02/22-rdf-syntax-ns#">
899           0x383           Unix path: /purl.org/dc/elements/1.1/">
1327          0x52F           Unix path: /ns.adobe.com/xap/1.0/mm/">
29457         0x7311          Zip archive data, at least v2.0 to extract, compressed size: 3088, uncompressed size: 3129, name: qrcode.png
32693         0x7FB5          End of Zip archive
```

You'll have a [folder](extracted/) with random name. In that folder we have an image called [`qrcode.png`](qrcode.png) and I don't need to tell you this that it's an image of a qrcode :smile:.

Now go to [this](https://www.imgonline.com.ua/eng/scan-qr-bar-code.php) website give your qrcode image to it and you'll get back a [link](https://pastebin.com/T87kA2NB) to a `paste` and there you'll get

```
--[------->++<]>-.[->+++<]>.+++++.-----------.+++++++++.+++++++++.+[->+++<]>++.+.-[----->+++<]>.--[->++<]>-.+.++[->+++<]>++.+++++.++++++.[->+++++<]>+++.+[--->+<]>+++.++[->+++<]>.>++++++++++.--[----->+<]>+.+++++.++++++.[---->+<]>+++.+[----->+<]>.------------.++++++++.+++++.++[++>---<]>.+.>++++++++++.>--[-->+++++<]>.>++++++++++.[->+++<]>++....[-->+++++++<]>.+++++.-.-.-[--->+<]>++.------.+[->++<]>+.+++++.+++++++++.--------------.>--[-->+++++<]>.-[->+++++<]>.[--->+<]>----.[-->+<]>-----.---.-[----->+<]>--.--------.-[--->+<]>--.+[->+++<]>+.++++++++.------------.+[-->+<]>+.++++.-----[->++<]>-.-[->++++++<]>.--[->++<]>-.+[-->+<]>+++++.+++[->++<]>+.+++[++>---<]>.++[->++<]>..-[--->+<]>.[->+++++<]>++.++++.-[-->+<]>-..++++++[->++<]>.[----->+<]>+.-[---->+<]>+++.+++++++.-[-->+++<]>-.>++++++++++..[->+++<]>++....---[----->++<]>.-------------.[--->+<]>---.+.---.----.-[->+++++<]>-.[-->+++<]>.+++++++++++.>++++++++++.>--[-->+++<]>.
```

Yes that's [brainfuck](https://en.wikipedia.org/wiki/Brainfuck) don't even thing and just go to [this](https://www.tutorialspoint.com/execute_brainfk_online.php) put the given code and you'll have:
```
$bfi main.bf
#include<stdio.h>
int main()
{
    puts("GLUG{br41nfuck_15_4c7u4lly_c00l}");

    return 0;
}
```

FLAG - `GLUG{br41nfuck_15_4c7u4lly_c00l}`
