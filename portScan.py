#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
Port Scan

Portscan is made for scan the target port.
It will scan the target port and return the portlist.
Return portlist if the target is alive or None if the target is dead.
"""

from tools import *
from scapy.layers.inet import IP, TCP
from scapy.sendrecv import sr1, send
from tools import *
import nmap


def portScan(scanInfo) -> list:
    """
    Port Scan
    """
    # Set target IP
    targetIP = scanInfo["targetIP"]
    # Set target port
    targetPort = scanInfo["targetPort"]
    # Set debug mode
    isDebug = scanInfo["isDebug"]
    # Set timeout
    timeout = 3
    # If targetPort is not None
    if targetPort is not None:
        # Set packet
        packet = IP(dst=targetIP) / TCP(dport=targetPort)
        # Send packet
        response = sr1(packet, timeout=timeout, verbose=isDebug)
        # If response is not None
        if response is not None:
            # Set portlist
            portlist = [targetPort]
        # If response is None
        else:
            # Set portlist
            portlist = []
    # If targetPort is None
    else:
        # Set portlist
        portlist = []
        # Set nmap scan
        nmapScan = nmap.PortScanner()
        # Scan targetIP
        nmapScan.scan(targetIP, "1-65535")
        # For each port
        for port in nmapScan[targetIP].all_tcp():
            # Set port
            port = port["port"]
            # Set packet
            packet = IP(dst=targetIP) / TCP(dport=port)
            # Send packet
            response = sr1(packet, timeout=timeout, verbose=isDebug)
            # If response is not None
            if response is not None:
                # Set portlist
                portlist.append(port)
    # Return portlist
    return portlist


if __name__ == "__main__":
    notMain()
