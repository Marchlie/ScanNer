#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
Alive Test

Alive test is made for test if the target is alive.
It will send ICMP packet to target and test if the target is alive.
Return bool if the target is alive or not.
"""


from scapy.layers.inet import ICMP, IP, TCP, sr1
from tools import *


def aliveTest(scanInfo) -> bool:
    """
    Alive Test
    """
    # Set target IP
    targetIP = scanInfo["targetIP"]
    # Set target port
    targetPort = scanInfo["targetPort"]
    # Set debug mode
    isDebug = scanInfo["isDebug"]
    # Set timeout
    timeout = 3
    # Set alive
    alive = False
    # Set ICMP packet
    packet = IP(dst=targetIP) / ICMP()
    # Send ICMP packet
    response = sr1(packet, timeout=timeout, verbose=isDebug)
    # If response is not None
    if response is not None:
        # Set alive
        alive = True
    # If targetPort is not None
    if targetPort is not None:
        # Set packet
        packet = IP(dst=targetIP) / TCP(dport=targetPort)
        # Send packet
        response = sr1(packet, timeout=timeout, verbose=isDebug)
        # If response is not None
        if response is not None:
            # Set alive
            alive = True
    # Return alive
    return alive


if __name__ == "__main__":
    notMain()
