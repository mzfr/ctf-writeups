# TUX

__PROBLEM__

Can you find something here, looks like it's broken.
Download the image below.

[TUX](tux)

__SOLUTION__

Problem says that it's an image but when you try to open it we get error. So first thing we do it see the signature of the given `image`.

```bash
>>> xxd -l8 tux
00000000: 8450 8e47 1d0a 1f0a                      .P.G....
```
We see the first 8 bits of the file and it some random numbers but when we check out signatures [here](https://en.wikipedia.org/wiki/List_of_file_signatures) we realise that it should be `89 50 4E 47 0D 0A 1A 0A` to make this file a proper `PNG` file. So just edit those and save the file and you'll have the [image](tux_image)

FLAG - `GLUG{p3n6u1n5_4r3_n07_b1rd5}`
