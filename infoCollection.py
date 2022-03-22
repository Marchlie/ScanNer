#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Information Collection
"""


from scapy.layers.inet import ICMP, IP, TCP
from scapy.sendrecv import sr1, send
from scapy.volatile import RandShort
from tools import *


def portscan(targetIP, targetPort, localIP, localPort, scanMode):
    if scanMode == "fullTCPScan":
        fullTCPScan(targetIP, targetPort, localIP, localPort)
    elif scanMode == "ping":
        ping(targetIP, localPort)
    else:
        printRed("Nothing to do")


def fullTCPScan(targetIP, targetPort, localIP, localPort):
    # TCP 连接扫描
    tcpConnectScan = sr1(
        IP(dst=targetIP) / TCP(sport=localIP, dport=targetIP, flags="S"), timeout=10
    )

    # 判断是否收到应答包
    if type(tcpConnectScan) == type(None):
        printRed("[-] Port is closed.")
    # 判断收到的应答包是否具有TCP层
    elif tcpConnectScan.haslayer(TCP):
        # 判断是否为SYN+ACK数据包
        if tcpConnectScan.getlayer(TCP).flags == 0x12:
            send(IP(dst=targetIP) / TCP(sport=localPort, dport=targetPort, flags="AR"))
            printGreen("[+] Port is open.")
        # 判断是否为RST数据包
        elif tcpConnectScan.getlayer(TCP).flags == 0x14:
            printRed("[-] Port is closed.")


def ping(targetIP, localPort):
    """
    Ping test

    request targetIP
    """
    icmp = IP(dst=targetIP) / ICMP()

    if type(icmp) == type(None):
        printRed("[-] targetIP might closed or be filtered")
    else:
        printGreen("[+] targetIP is open")
        print(icmp.answers)


if __name__ == "__main__":
    notMain()
