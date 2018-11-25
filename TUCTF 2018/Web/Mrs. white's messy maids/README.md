# Mrs. White's <br> Messy Maids

__PROBLEM__

Mrs. White's simple website might be hiding some murderous intentions...

http://18.218.152.56/

__SOLUTION__

First thing we check is the source and we see

```
<html>
        <head>
            <title>Mrs. White</title>
        <link rel="stylesheet" href="styles.css">
        </head>

    <body>
        <h1>Welcome to Mrs. White's Maid Service</h1>
        <img src="https://tinyurl.com/ybbtf3nv" height="500">
        <p>We offer only the best maids for all your cleaning needs
        <br>
        To learn more about our services, call 275-317-3581
        <!-- I might kill if I could find him. Stupid Mr. /Boddy --></p>
        </body>
</html>
```

See the last line something about `/Boddy` so we try visiting `18.218.152.56/Boddy/` and we have it

FLAG - `TUCTF{1_4ccu53_Mr5._Wh173_w17h_7h3_c4ndl3571ck_1n_7h3_c0mm3n75}`
