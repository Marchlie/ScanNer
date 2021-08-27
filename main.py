import argparse
from infoCollection import portscan


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", help="Local IP", type=str,)
    parser.add_argument("-lp", help="Local port", type=int)
    parser.add_argument("t", help="Target IP", type=str)
    parser.add_argument("-tp", help="Target port", type=int)
    parser.add_argument("-sm", help="Scan mode", type=str)
    args = parser.parse_args()

    targetIP = args.t
    targetPort = args.tp
    localIP = args.l
    localPort = args.lp
    scanMode = args.sm

    portscan(targetIP, targetPort, localIP, localPort, scanMode)


if __name__ == "__main__":
    main()
