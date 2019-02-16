# Broken Image

__PROBLEM__

One of our server contained photographs of all the employees, hackers managed to modify the image corresponding to the CEO's. We have been trying to open it since, but failed.

__SOLUTION__

Since the problem statement says that the image was modified in some way and now it can't be opened normally, so we start with checking the headers of the file.

```bash
✦ ➜ xxd -l8 CEO
00000000: aad8 aae0 0010 0046                      .......F
```
We can see that it's clearly a messed up JPG file. How?

Well I have solved lot of such kind of challenges so I just know but if you are beginner then to know what kind of header it could be you should try searching on [wikipedia file signature](https://en.wikipedia.org/wiki/List_of_file_signatures)

The right header for JPG would be:
```
FF D8 FF E0 00 10 4A 46 49 46 00 01
```

So just open the file in hexeditor and fix those headers and save the file and you'll have a correct image with the flag.

FLAG - `xiomara{7h1s_1s_w4y_2_34sy}`
