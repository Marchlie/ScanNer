import argparse
import time

import aliveTest
import fingerprint
import portScan
import vulnerability
from tools import log


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("t", help="Target IP", type=str)
    parser.add_argument("-tp", help="Target port", type=int, default=None)
    parser.add_argument(
        "--debug", help="Debug mode", action="store_true", default=False
    )
    args = parser.parse_args()

    scanInfo = {
        "targetIP": args.t,
        "targetPort": args.tp,
        "isDebug": args.debug,
    }

    # Log scanInfo
    log.info("scanInfo: " + str(scanInfo))

    # Alive test
    scanInfo = {"alive": aliveTest(scanInfo)}

    # If alive, do portscan
    if scanInfo["alive"] == True:
        scanInfo["portlist"] = portScan(scanInfo)

    # If portlist is not empty, check fingerprint
    if scanInfo["portlist"] != None:
        scanInfo["fingerprint"] = fingerprint(scanInfo)

    # If fingerprint is not empty, check vulnerability
    if scanInfo["fingerprint"] != None:
        scanInfo["vulnerability"] = vulnerability(scanInfo)

    # Print result
    print(scanInfo)
    with open(
        "result" + time.strftime("%Y-%m-%d", time.localtime(time.time())) + ".txt",
        "a",
    ) as f:
        f.write(str(scanInfo) + "\n")


if __name__ == "__main__":
    main()
