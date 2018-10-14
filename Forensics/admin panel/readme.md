# admin panel

__PROBLEM__

We captured some [traffic](data.pcap) logging into the admin panel, can you find the password?

__HINT__

Tools like wireshark are pretty good for analyzing pcap files.

__SOLUTION__

Okay so we are given a .pcap file. If you don't know what it is read about them [here](https://en.wikipedia.org/wiki/Pcap).
open the given pcap file in [wireshark](https://www.wireshark.org/) and then you'll be able to see something like

[!alt](wireshark-pcap.png)

This is the traffic that was captured. Now we have to find the password for `admin`, keep that in mind only for admin and not for some other user.

Now how to find the password into this haystack. well it is simple whenever you try to login you'll into any account you have to send data which is a `POST` method used by HTTP for sending those credentials. So search for `http` and you'll be left with very few entries. Something like

[!alt](wireshark-http.png)

In this look for the line
`68    37.234879   192.168.3.129   192.168.3.128   HTTP    542 POST /login HTTP/1.1 [Packet size limited during capture]`

Double click on it and in the last you'll be able to see the flag

FLAG - `picoCTF{n0ts3cur3_9feedfbc}`
