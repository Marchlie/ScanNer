#!/usr/bin/python
# -*- coding: UTF-8 -*-

from scapy.layers.inet import ICMP, IP, TCP
from scapy.sendrecv import sr1, send
from scapy.volatile import RandShort
from tools import *

def portscan(targetIp, targetPort, localIp, localPort, scanMode):
    if scanMode == "fullTCPScan":
        fullTCPScan(targetIp, targetPort, localIp, localPort)
    elif scanMode == "ping":
        ping(targetIp, localPort)
    else:
        printRed("Nothing to do")


def fullTCPScan(targetIp, targetPort, localIp, localPort):
    # TCP 连接扫描
    tcpConnectScan = sr1(IP(dst=targetIp) / TCP(sport=localIp,
                                                dport=targetIp, flags='S'), timeout=10)

   # 判断是否收到应答包
    if type(tcpConnectScan) == type(None):
        printRed("[-] Port is closed.")
    # 判断收到的应答包是否具有TCP层
    elif tcpConnectScan.haslayer(TCP):
        # 判断是否为SYN+ACK数据包
        if tcpConnectScan.getlayer(TCP).flags == 0x12:
            send(IP(dst=targetIp) / TCP(sport=localPort,
                 dport=targetPort, flags='AR'))
            printGreen("[+] Port is open.")
        # 判断是否为RST数据包
        elif tcpConnectScan.getlayer(TCP).flags == 0x14:
            printRed("[-] Port is closed.")


def ping(targetIp):
    """
    ping test

    requrest targetIP
    """
    icmp = IP(dst=targetIp)/ICMP()

    if type(icmp) == type(None):
        printRed("[-] targetIP might closed or be filtered")


if __name__ == "__main__":
    notMain()
