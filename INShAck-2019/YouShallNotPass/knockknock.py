#!/usr/bin/env python3

import time
import socket
import select


sequence= [
    {"port": 10010, "proto": "UDP"},
    {"port": 10090, "proto": "UDP"},
    {"port": 10020, "proto": "TCP"},
    {"port": 10010, "proto": "UDP"},
    {"port": 10060, "proto": "TCP"},
    {"port": 10080, "proto": "UDP"},
    {"port": 10010, "proto": "UDP"},
    {"port": 10000, "proto": "TCP"},
    {"port": 10000, "proto": "UDP"},
    {"port": 10040, "proto": "TCP"},
    {"port": 10020, "proto": "UDP"}  ]

class Knocker(object):
    def __init__(self):
        self.timeout = 200 / 1000
        self.address_family, _, _, _, (self.ip_address, _) = socket.getaddrinfo(
                host="you-shall-not-pass.ctf.insecurity-insa.fr",
                port=None,
                flags=socket.AI_ADDRCONFIG
            )[0]

    def knock(self):

        for pair in sequence:
            use_udp = pair["proto"] == "UDP"
            port = pair["port"]

            s = socket.socket(self.address_family, socket.SOCK_DGRAM if use_udp else socket.SOCK_STREAM)
            s.setblocking(False)

            socket_address = (self.ip_address, port)
            if use_udp:
                s.sendto(b"a", socket_address)
            else:
                s.connect_ex(socket_address)
                select.select([s], [s], [s], self.timeout)

            s.close()
            time.sleep(self.timeout)



if __name__ == '__main__':
    Knocker().knock()
