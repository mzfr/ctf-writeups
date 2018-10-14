# What's My Name?

__PROBLEM__

Say my name, say [my name](myname.pcap).

__HINT__

If you visited a website at an IP address, how does it know the name of the domain?

__SOLUTION__

Again we are given a `.pcap` file and we have to find the flag. Here the hint talks about domain so basically we are looking for [DNS servers](https://www.cloudflare.com/learning/dns/what-is-dns/).

Search for `dns`, you'll be left with two entries, double click on the second one:
```
55  1418.342859 192.168.2.12    192.168.2.1 DNS 316 Standard query response 0xaaa0 ANY thisismyname.com A 192.168.2.13 CNAME myname.com MX 5 myname.com MX 10 mx2.myname.com MX 20 mx3.myname.com NS ns1.myname.com NS ns2.myname.com TXT SOA ns1.thisismyname.com
```

Then click on `Domain Name System (response)` there in the `answer` field you'll see the flag.

FLAG - `picoCTF{w4lt3r_wh1t3_2d6d3c6c75aa3be7f42debed8ad16e3b}`
