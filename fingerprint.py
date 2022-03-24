#!/usr/bin/python3
# -*- coding: UTF-8 -*-
#
# Author: Marchlie
# Date: 2022-03-24
# Link: github.com/marchlie/scanner

"""
Fingerprint identification

Fingerprint identification is made for test if the target port has fingerprint or not.
It will send TCP packet to target and test if the target has fingerprint.
Return Fingerprint list if the target has fingerprint or None if not.
"""

import nmap
from tools import *
from scapy.layers.inet import IP, TCP, sr1
from requests import get
from fingerprint.webFingerprint import webFingerprint


def fingerprint(scanInfo) -> list:
    # Set target IP
    targetIP = scanInfo["targetIP"]
    # Set target port
    targetPort = scanInfo["targetPort"]
    # Set debug mode
    isDebug = scanInfo["isDebug"]
    # Set portlist
    portlist = scanInfo["portlist"]
    # Set timeout
    timeout = 3
    # Set fingerprint
    fingerprint = None
    # If targetPort is not None
    if targetPort is not None:
        webFingerprint(scanInfo)


if __name__ == "__main__":
    notMain()
