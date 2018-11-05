# Go Get it!

__PROBLEM__

Head over to the link below to find the flag.
[LINK](http://104.248.49.223:7070/)

__HINT__

Can you send a get parameter through url.

For example:

https://www.google.com/search?q=flag

__SOLUTION__

After you head over to the given link you'll see something like:
>
This is just a decoy of the FLAG!
If you ask nicely, maybe i will give it to you.
View Source Code of this page [Here](https://pastebin.com/LvfdATxz)

The Page source is:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Flag!Flag!Flag!</title>
    <link rel="stylesheet" href="css/main.css">
</head>
<body>
    <div class='contain-flag'>
      <div class='pole'></div>
      <div class='flag'></div>
      <div class='shadow'></div>
      <div class='flag flag-2'></div>
    </div>
    <div>
        <center>
        <h3>This is just a decoy of the FLAG!</h3>
        <small>If you ask nicely, maybe i will give it to you.</small>
        <small>View Source of this page <a href="https://pastebin.com/LvfdATxz" target="_blank">Here</a></small>
        </center>
    </div>
    <pre><?php
    $flag = #REDACTED

    if(array_key_exists("flag", $_GET)) {
        if($_GET["flag"] === "true"){
        echo $flag;
        }
    }
    ?>
    </pre>
</body>
</html>
```

If you'll see the `PHP` in the source of the page you'll notice that it is checking whether there exists a `flag` query in the sent requests or not. So all we have to do it send that and that can be done by adding `?flag=true` to the given URL so the full URL becomes `http://104.248.49.223:7070/?flag=true`. That will give you the flag.

Flag - `GLUG{4lw4y5_fuzz_f0r_h1dd3n_p4r4m373r5} `
