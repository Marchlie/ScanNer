from scapy.layers.inet import IP, TCP
from scapy.sendrecv import sr1, send
from scapy.volatile import RandShort
from tools import *


def portscan(targetIp, targetPort, localIp, localPort, scanMode):
    if scanMode == "fullTCPScan":
        fullTCPScan(targetIp, targetPort, localIp, localPort)


def fullTCPScan(targetIp, targetPort, localIp, localPort):
    # TCP 连接扫描
    tcp_connect_scan = sr1(IP(dst=targetIp) / TCP(sport=localIp,
                                                  dport=targetIp, flags='S'), timeout=10)

   # 判断是否收到应答包
    if type(tcp_connect_scan) == type(None):
        print("[-] Port is closed.")
    # 判断收到的应答包是否具有TCP层
    elif tcp_connect_scan.haslayer(TCP):
        # 判断是否为SYN+ACK数据包
        if tcp_connect_scan.getlayer(TCP).flags == 0x12:
            send(IP(dst=targetIp) / TCP(sport=localPort,
                 dport=targetPort, flags='AR'))
            printGreen("[+] Port is open.")
        # 判断是否为RST数据包
        elif tcp_connect_scan.getlayer(TCP).flags == 0x14:
            printRed("[-] Port is closed.")


if __name__ == "__main__":
    notMain()
