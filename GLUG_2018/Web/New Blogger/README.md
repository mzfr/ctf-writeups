# New Blogger

__PROBLEM__

Misha is a travel blogger.She made a website for her blog.Minan was very impressed with it but on detailed inspection found that there existed a vulnerability.
Can you find the flag exploiting the same?

Hint: Flag is in /etc/flag

[Link](104.248.49.223:7074)


__SOLUTION__

After reading the hint one thing that is clear is that this website is vulnerable to [Local file inclusion(LFI)](https://en.wikipedia.org/wiki/File_inclusion_vulnerability). So First thing to try is `http://104.248.49.223:7074/?page=../../../../../../../../../../etc/flag` and guess what we have, yes our beloved flag.

FLAG - `GLUG{7h3_54m3_0ld_f1l3_1nclu510n}`
