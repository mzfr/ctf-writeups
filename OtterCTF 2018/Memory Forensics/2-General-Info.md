# 2-General Info

__PROBLEM__

Let's start easy - whats the PC's name and IP address?

format: CTF{flag}

__SOLUTION__

Now in this one we need to find the PC's name and IP address of the Rick's PC.

First of all we'll get those information from `Window's registry` so we'll have to get the offset of the registry.

```bash
➜ volatility -f OtterCTF.vmem --profile=Win7SP1x64 hivelist
Volatility Foundation Volatility Framework 2.6
Virtual            Physical           Name
------------------ ------------------ ----
0xfffff8a00377d2d0 0x00000000624162d0 \??\C:\System Volume Information\Syscache.hve
0xfffff8a00000f010 0x000000002d4c1010 [no name]
0xfffff8a000024010 0x000000002d50c010 \REGISTRY\MACHINE\SYSTEM
0xfffff8a000053320 0x000000002d5bb320 \REGISTRY\MACHINE\HARDWARE
0xfffff8a000109410 0x0000000029cb4410 \SystemRoot\System32\Config\SECURITY
0xfffff8a00033d410 0x000000002a958410 \Device\HarddiskVolume1\Boot\BCD
0xfffff8a0005d5010 0x000000002a983010 \SystemRoot\System32\Config\SOFTWARE
0xfffff8a001495010 0x0000000024912010 \SystemRoot\System32\Config\DEFAULT
0xfffff8a0016d4010 0x00000000214e1010 \SystemRoot\System32\Config\SAM
0xfffff8a00175b010 0x00000000211eb010 \??\C:\Windows\ServiceProfiles\NetworkService\NTUSER.DAT
0xfffff8a00176e410 0x00000000206db410 \??\C:\Windows\ServiceProfiles\LocalService\NTUSER.DAT
0xfffff8a002090010 0x000000000b92b010 \??\C:\Users\Rick\ntuser.dat
0xfffff8a0020ad410 0x000000000db41410 \??\C:\Users\Rick\AppData\Local\Microsoft\Windows\UsrClass.dat
```

As we can see in the output above the offset for the registry is `0xfffff8a000024010`. So now we'll get the keys for it:

```bash
➜ vol.py -f OtterCTF.vmem --profile=Win7SP1x64 printkey -o 0xfffff8a000024010 -K "ControlSet001\Control\ComputerName\ComputerName"
Volatility Foundation Volatility Framework 2.6
Legend: (S) = Stable   (V) = Volatile

----------------------------
Registry: \REGISTRY\MACHINE\SYSTEM
Key name: ComputerName (S)
Last updated: 2018-06-02 19:23:00 UTC+0000

Subkeys:

Values:
REG_SZ                        : (S) mnmsrvc
REG_SZ        ComputerName    : (S) WIN-LO6FAF3DTFE
```

PC Name is `WIN-LO6FAF3DTFE`

Now for IP we can simply run a netscan on the memory.

```bash
0x7e7b0380         TCPv6    -:0                            4847:d418:80fa:ffff:4847:d418:80fa:ffff:0 CLOSED           2836     BitTorrent.exe
0x7e7b9010         TCPv4    192.168.202.131:50334          188.129.94.129:25128 CLOSED           2836     BitTorrent.exe
0x7e94b010         TCPv4    192.168.202.131:50356          77.126.30.221:13905  CLOSED           2836     BitTorrent.exe
0x7e9ad840         TCPv4    192.168.202.131:50380          84.52.144.29:56299   CLOSED           2836     BitTorrent.exe
0x7e9bacf0         TCPv4    192.168.202.131:50350          77.253.242.0:5000    CLOSED           2836     BitTorrent.exe
0x7eaac5e0         TCPv4    192.168.202.131:50387          93.184.220.29:80     CLOSED           3856     WebCompanion.e
0x7eab4cf0         TCPv4    -:0                            56.219.196.26:0      CLOSED           2836     BitTorrent.exe
0x7fb9cec0         UDPv4    192.168.202.131:1900           *:*                                   164      svchost.exe    2018-08-04 19:28:42 UTC+0000
0x7fb9d430         UDPv4    127.0.0.1:58341                *:*                                   164      svchost.exe    2018-08-04
```

This is not the complete output. You'll get lots of IP and stuff. But Our answer is in the last.

IP - `192.168.202.131`

I don't know why this is the IP, I just randomly tried this one and it accepted.

FLAG -  PC IP - `CTF{192.168.202.131}`
        PC name - `CTF{WIN-LO6FAF3DTFE}`
