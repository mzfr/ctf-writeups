# Literal

__PROBLEM__

Something's going over my head, and it's too fast for me to catch! (Difficulty: Easy)

http://18.222.124.7

__SOLUTION__

visiting the given URL will redirect you to a wikipedia page called [Fork Bomb](https://en.wikipedia.org/wiki/Fork_bomb)
For this I used [httpie](https://httpie.org/)

```bash
➜ http http://18.222.124.7
HTTP/1.1 200 OK
Accept-Ranges: bytes
Connection: Keep-Alive
Content-Length: 95
Content-Type: text/html; charset=UTF-8
Date: Sun, 25 Nov 2018 17:50:51 GMT
ETag: "5f-57b42cc30d8d7"
Keep-Alive: timeout=5, max=100
Last-Modified: Thu, 22 Nov 2018 15:48:27 GMT
Server: Apache/2.4.34 (Amazon)

<html>

<head>
        <meta http-equiv="refresh" content="0; URL='Literal.html'" />
</head>

</html>
```
Then try to go on `Literal.html`

```bash
➜ http http://18.222.124.7/Literal.html
HTTP/1.1 200 OK
Accept-Ranges: bytes
Connection: Keep-Alive
Content-Length: 841
Content-Type: text/html; charset=UTF-8
Date: Sun, 25 Nov 2018 17:51:25 GMT
ETag: "349-57b42af66aaaa"
Keep-Alive: timeout=5, max=100
Last-Modified: Thu, 22 Nov 2018 15:40:24 GMT
Server: Apache/2.4.34 (Amazon)

<html>
  <head>
  <meta http-equiv="Refresh" content="1; url=https://en.wikipedia.org/wiki/Fork_bomb">
  </head>
  <body>
  <!--
        *   *                     f   f   f
      *  ** *                   ff  ff  ff
      * * ** ||                ff  ff  ff
    **   ||||T||              fUffffffff
      *   |C|||T| oooooooooooo fFff
           |||||||{ooooooooooRfff3o
          ooo4ooooooooooooooLff.ooooo0
        oooNooooooooooooooo3ooooooo5ooo.
        oooo4oooooRoooooooooo3oooooooooo.
        oooDooooo4oooooNooooooooooooooooo
        ooooooooooooooGoooooooooooooooooo
        ooooooooooooooooooooo3oooooooooRo
         oooooooo0oooooooooooooooooooooo
          oooooooffUoooooooooooooooooo
            ooofff5ooooooooooooooooo
             fff }ooooooooooooooo
            fff
  -->
  Redirecting to Wikipedia...!
  </body>
</html>

```

We can see the flag but it's with lot of junk clean it up.

FLAG - `TUCTF{R34L.0N35.4R3.D4NG3R0U5}`
