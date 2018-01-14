# Installation(on Debian-based Linux Distribution)

## Update your operating system before running

```
% sudo apt update
```

## Clone and enter this repository

```
% git clone http://github.com/ellisspringe/spoof-phisher
% cd spoof-phisher
```

## Run the installer script (check sources in /etc/apt/source.list if things aren't downloaded properly)

```
% sudo bash install
```

# Usage

## ARP poisoning.
```
% sudo python arp_poison.py -v <victim IP Address> -r <router IP Address>
```

## DNS spoofing.
```
% sudo python dns_packet_spoof.py
```

# References
 * [Reliable DNS spoofing with Python: Scapy + Nfqueue](http://danmcinerney.org/reliable-dns-spoofing-with-python-scapy-nfqueue/)
 * [ARP poisoning with Python](http://danmcinerney.org/arp-poisoning-with-python-2/)
