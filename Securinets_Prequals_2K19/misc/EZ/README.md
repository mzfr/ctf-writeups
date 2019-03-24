# EZ

__PROBLEM__

Welcome to Securinets, this one is an easy one.

Please make sure you hash the WORD with sha1 (lowercase hash letter)

The final flag is : Securinets{the_hash_of_the_word}

[Pic Link](pic.zip)

Author:BlueWhale


__SOLUTION__

Again I started with strings followed by exiftool and then binwalk and none of those gave anything interesting. And then I noticed that the image is of `.png` format that means we can use `zsteg` on that image.

```bash
➜ zsteg pic.png
b1,rgb,lsb,xy       .. text: "--START--\n\"The fact is that upon his entrance I had instantly recognized the extreme\npersonal danger in which I lay. The only conceivable escape for him lay in silencing\nmy tongue. In an instant I had slipped the revolver from the drawer into my\npocket and"
b2,b,msb,xy         .. text: "_uW}W}W}"
b3,b,lsb,xy         .. file: very old 16-bit-int big-endian archive
b4,r,lsb,xy         .. text: "\nvvwgffwfwvwgg"
b4,g,lsb,xy         .. text: "gwvwvffwvgvfggfvwgvfvgfgvgffvwfvwgfvfgvvwwvfwgfwfgvgvgffwgffffffwgfffgfgvwvfwgvfwwfwvwfgvwvfwgvffgvfvwffwgvwvwvfggffvgfgwgfffgvfwgvfvgffwgfwwgfgwgfffgvfwwvfvgfffgvgwgffvwvgvwvfvgfgwgvfvwfgvwfffgvgvgffwwvfwgfvfgfgfgffwgvgvwfgvvffwwfvwwvgvwvgfffgfgfgfgfgvwvf"
b4,b,lsb,xy         .. text: "wfgggfgfgffwffwfvfffwfggwfgwvfgfvfgfvggfwfvfvfggvfgvwgwgwfwgvfffvfgfvfgvvgggwggvvfgfwfwwwfwwvfgfvggvwfggvggfwfggfgggvgwwwfgvvfggwfwgvfgwwfggvfggvfgwvfggvfvfgfggvfwvwgffvfwvvfgwwfgfwfffwgwgvgggvfwwvfgvvfffwfgwvfgvvgwwwfgvvfgvwfwwvfgfwfwgwffvvfgvvfgvvfgvvggg"
b4,rgb,lsb,xy       .. text: "ogWef&vfFmw"
b4,rgb,msb,xy       .. text: "`vnovng>"
b4,bgr,lsb,xy       .. text: "ogVev&ffG}g"
```

This show that there's some strings hidden there, let's extract that

```
--START--
"The fact is that upon his entrance I had instantly recognized the extreme
personal danger in which I lay. The only conceivable escape for him lay in silencing
my tongue. In an instant I had slipped the revolver from the drawer into my
pocket and was covering him through the cloth. At his remark I drew the weapon
out and laid it cocked upon the table. He still smiled and blinked, but there was
something about his eyes which made me feel very glad that I had it there,
"You evidently don't know me,' said he.
"'On the contrary,' I answered, 'I think it is fairly evident that I do. Pray take
a chair. I can spare you five minutes if you have anything to say.'
"'All that I have to say has already crossed your mind,' said he.
"'Then possibly my answer has crossed yours,' I replied.
"'You stand fast?'
"'Absolutely.'
"He clapped his hand into his pocket, and I raised the pistol from the table.
But he merely drew out a <DETELED_WORD> in which he had scribbled some
dates.
"You crossed my path on the fourth of January,' said he. 'On the twenty-third
you incommoded me; by the middle of February I was seriously inconvenienced
by you; at the end of March I was absolutely hampered in my plans; and now, at
the close of April, I find myself placed in such a position through your continual
persecution that I am in positive danger of losing my liberty. The situation is
becoming an impossible one.'
"'Have you any suggestion to make?' I asked.
"'You must drop it, Mr. Holmes,' said he, swaying his face about. 'You really
must, you know.'"
--END--
```

This is what we get from the extracted data and now all we have to do is to find the `<DELETED_WORD>`. Simply google any part of the paragraph and it will give us the [original](https://www.pagebypagebooks.com/Arthur_Conan_Doyle/Memoirs_of_Sherlock_Holmes/Adventure_XI_The_Final_Problem_p4.html)

After comparing with original we found out that the missing word is `memorandum-book`, but submitting the sha1 of this string didn't worked so we tried with `memorandumbook`

```bash
➜ echo "memorandumbook" | sha1sum
3e06c0914406bcd91c6326d32a75be36dd44a2d4
```
FLAG - Securinets{3e06c0914406bcd91c6326d32a75be36dd44a2d4}
