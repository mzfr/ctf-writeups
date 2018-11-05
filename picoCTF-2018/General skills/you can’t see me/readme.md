# you can’t see me

__PROBLEM__

’…reading transmission… Y.O.U. .C.A.N.‘.T. .S.E.E. .M.E. …transmission ended…’ Maybe something lies in /problems/you-can-t-see-me_2_cfb71908d8368e3062423b45959784aa.

__HINT__

What command can see/read files?

What's in the manual page of ls?


__SOLUTION__

Go to the given directory and run `ls -la` which gives us
```
drwxr-xr-x   2 root       root        4096 Sep 28 08:34 .
-rw-rw-r--   1 hacksports hacksports    57 Sep 28 08:34 .
drwxr-x--x 576 root       root       53248 Sep 30 03:50 ..
```

If you'll use `tab` to auto complete the file name you'll see that there is a file name `.  ` So just use `cat` command to see the content of the file.
```
> cat `.  `
```

FLAG - `picoCTF{j0hn_c3na_paparapaaaaaaa_paparapaaaaaa_cf5156ef}`
