# Musically

__PROBLEM__

We can have a list of songs.And a search input where a user can search for a song along with details.
[Link to the Challenge](http://142.93.207.206:7004/)

[Link to the source code](https://ghostbin.com/paste/pzzxm)

__SOLUTION__

Lets start with the source:

```php
 <pre><?php
 $key = ".";
 if(array_key_exists("needle", $_REQUEST)) {
    $key = $_REQUEST["needle"];
}
 if($key != "") {
    passthru("grep -i $key songs.txt");
 } ?> </pre>
```

Okay so what is happening here is that first condition checks whether there is a `needle` parameter exists or not if it does then `$key` is assigned to needle key. Then Second condition just `grep` the searched value on `songs.txt`

So what is wrong with the code? Well, this is bad because in this we can execute our own commands too just like in linux terminal. To do that type `;ls;` in search bar and you'll see list of files. Then again search `;cat flag.txt;` and voila. What we did here was with first `;` we stopped the previous running command that was `grep -i $key songs.txt` and then we run our own command.

This was solved by by teammate @ugtan

FLAG - `GLUG{you_never_gonna_find_song}`
