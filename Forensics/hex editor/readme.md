# hex editor

__PROBLEM__

 This [cat](hex_editor.jpg) has a secret to teach you. You can also find the file in /problems/hex-editor_0_8c20f979e6b2740dee597871ff1a74ee on the shell server.

__HINT__

What is a hex editor?

Maybe google knows.

[xxd](http://linuxcommand.org/man_pages/xxd1.html)

[hexedit](http://linuxcommand.org/man_pages/hexedit1.html)

[bvi](http://manpages.ubuntu.com/manpages/cosmic/en/man1/bvi.1.html)

__SOLUTION__

This si a simple task where you are supposed to check the hex of the given image.

Run
```
xxd hex_editor.jpg
```

And scroll to the last, there you'll see the flag.

FLAG - `picoCTF{and_thats_how_u_edit_hex_kittos_3E03e57d}`
