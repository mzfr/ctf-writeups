# Table tennis

__Problem__

The flag is in the Pcap, can you find it?

[out.pcapng](out.pcapng)

__Solution__

After opening the file in wireshark the first thing you'll notice will be the `DNS` and `TCP` protocol. I spended sometime looking at those protocol and even tried following the TCP protocol but didn't find anything.

Then I noticed that there's also `ICMP` protocol and when I tried viewing it's data I could see some HTML data in there. So I decided to use `tshark` to get that data but since I am not very good with tshark I couldn't figure out how to get that data from ICMP so I decided to use our beloved python along with scapy.

```python
from scapy.all import *

packet = rdpcap(file)
for pac in packet:
    if pac.haslayer(ICMP) and pac[ICMP].type == 0:
        data.append(pac[ICMP].layer[-8:].decode("utf-8"))

print("".join(data))
```

This gives us

```
'<html>\n\t<head>\n\t<title> I <3 Corgi </title>\n\t\t<script>\ndocument.write(atob("Q1RGe0p1c3RBUzBuZ0FiMHV0UDFuZ1Awbmd9"));\n\t\t</script>\n\n\t</head>\n\n\t<body>\n\n\t\t<h1> Woof!! </h1>\n\n\t</body>\n\n</ht`
```

We can see a base64 there decode that and you'll have the flag.
```
➜ echo "Q1RGe0p1c3RBUzBuZ0FiMHV0UDFuZ1Awbmd9" | base64 -d
CTF{JustAS0ngAb0utP1ngP0ng}
```

FLAG: `CTF{JustAS0ngAb0utP1ngP0ng}`
