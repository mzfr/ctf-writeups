# Truly an artist

__PROBLEM__

 Can you help us find the flag in this [Meta-Material](2018.png)? You can also find the file in /problems/truly-an-artist_4_cdd9e325cf9bacd265b98a7fe336e840.

__HINT__

Try looking beyond the image.

Who created this?

__SOLUTION__

In this we have to check the [metadata](https://en.wikipedia.org/wiki/Metadata) of the image. There are lots of existing tools but we can also use `xxd`

Just like `hex editor` problem, check out the last part of hex of the given image `xxd 2018.png` and there will be your flag.

FLAG - `picoCTF{look_in_image_13509d38}`
