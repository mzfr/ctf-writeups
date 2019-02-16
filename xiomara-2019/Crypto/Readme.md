# Esoteric Programming

__PROBLEM__

USdgZV85XDd+NXh3bUg2T04zQzEqQVotOSUqIzVSdXRye04hLUN8PClda2pMaGE0SHgxYnVDc3hxcCl0c19UXW9bTX5OXUlIR0xLRGhIR1pkREMyMVR4WFcsVVRAcSdQPDtAPzhcPHw6M0oxNjU0MzIrQi8uJyYlJFUiIX4lJHtOIWt9fGg7bGtqTEthNHlHY2JhdC1yd3ZvKFZfXnBcImBPS3xcPj1GakpDOEFGWVhiQlUwU1JXUHRUUyhRUE9OQDldPX01TDNsNzBHaDMsMTApLidYKyojKCd+UXIjIiF+fWk8bWxrTWNiZ3ozZGNiREN5eHEqWFdgcnFwXFsheQ==


__SOLUTION__

As the name suggest it's esoteric language but which one.
If you look at the file name it says `benolmstead.txt`, simple google search will show that `Ben olmstead` created `malbolge`.

We start with decoding the given string with base64
```
✦ ➜ echo "USdgZV85XDd+NXh3bUg2T04zQzEqQVotOSUqIzVSdXRye04hLUN8PClda2pMaGE0SHgxYnVDc3hxcCl0c19UXW9bTX5OXUlIR0xLRGhIR1pkREMyMVR4WFcsVVRAcSdQPDtAPzhcPHw6M0oxNjU0MzIrQi8uJyYlJFUiIX4lJHtOIWt9fGg7bGtqTEthNHlHY2JhdC1yd3ZvKFZfXnBcImBPS3xcPj1GakpDOEFGWVhiQlUwU1JXUHRUUyhRUE9OQDldPX01TDNsNzBHaDMsMTApLidYKyojKCd+UXIjIiF+fWk8bWxrTWNiZ3ozZGNiREN5eHEqWFdgcnFwXFsheQ==" | base64 -d
Q'`e_9\7~5xwmH6ON3C1*AZ-9%*#5Rutr{N!-C|<)]kjLha4Hx1buCsxqp)ts_T]o[M~N]IHGLKDhHGZdDC21TxXW,UT@q'P<;@?8\<|:3J165432+B/.'&%$U"!~%${N!k}|h;lkjLKa4yGcbat-rwvo(V_^p\"`OK|\>=FjJC8AFYXbBU0SRWPtTS(QPON@9]=}5L3l70Gh3,10).'X+*#('~Qr#"!~}i<mlkMcbgz3dcbDCyxq*XW`rqp\[!y
```

Using [Malbolge online interpreter](http://malbolge.doleczek.pl/) we try decoding the string we got after base64 but that gives us error. First I tried removing the error but that seemed to simply give more erros so this time I decode the given base64 along with rot13

```bash
>>> echo "USdgZV85XDd+NXh3bUg2T04zQzEqQVotOSUqIzVSdXRye04hLUN8PClda2pMaGE0SHgxYnVDc3hxcCl0c19UXW9bTX5OXUlIR0xLRGhIR1pkREMyMVR4WFcsVVRAcSdQPDtAPzhcPHw6M0oxNjU0MzIrQi8uJyYlJFUiIX4lJHtOIWt9fGg7bGtqTEthNHlHY2JhdC1yd3ZvKFZfXnBcImBPS3xcPj1GakpDOEFGWVhiQlUwU1JXUHRUUyhRUE9OQDldPX01TDNsNzBHaDMsMTApLidYKyojKCd+UXIjIiF+fWk8bWxrTWNiZ3ozZGNiREN5eHEqWFdgcnFwXFsheQ==" | base64 -d | tr '[a-m][n-z][A-M][N-Z]' '[n-z][a-m][N-Z][A-M]'

D'`r_9\7~5kjzU6BA3P1*NM-9%*#5Ehge{A!-P|<)]xwYun4Uk1ohPfkdc)gf_G]b[Z~A]VUTYXQuUTMqQP21GkKJ,HG@d'C<;@?8\<|:3W165432+O/.'&%$H"!~%${A!x}|u;yxwYXn4lTpong-ejib(I_^c\"`BX|\>=SwWP8NSLKoOH0FEJCgGF(DCBA@9]=}5Y3y70Tu3,10).'K+*#('~De#"!~}v<zyxZpotm3qpoQPlkd*KJ`edc\[!l
```

The `tr '[a-m][n-z][A-M][N-Z]' '[n-z][a-m][N-Z][A-M]'` command is actually bash way of doing rot13.

Now if you use that string into the interpreter you'll get the flag.

FLAG - `xiomara{Mlab0lge_Is_verY_Simple_for_you}`
