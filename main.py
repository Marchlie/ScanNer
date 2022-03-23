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
    parser.add_argument("-tp", help="Target port", type=int)
    parser.add_argument("--debug", help="Debug mode", action="store_true")
    args = parser.parse_args()

    scanConfig = {
        "targetIP": args.t,
        "targetPort": args.tp,
        "isDebug": args.debug,
    }

    # Log ScanConfig
    log.info("ScanConfig: " + str(scanConfig))

    # Alive test
    scanConfig = {"alive": aliveTest(scanConfig)}

    # If alive, do portscan
    if scanConfig["alive"] == True:
        scanConfig["portlist"] = portScan(scanConfig)

    # If portlist is not empty, check fingerprint
    if scanConfig["portlist"] != None:
        scanConfig["fingerprint"] = fingerprint(scanConfig)

    # If fingerprint is not empty, check vulnerability

    if scanConfig["fingerprint"] != None:
        scanConfig["vulnerability"] = vulnerability()

    # Print result
    print(scanConfig)
    with open(
        "result" + time.strftime("%Y-%m-%d", time.localtime(time.time())) + ".txt",
        "a",
    ) as f:
        f.write(str(scanConfig) + "\n")


if __name__ == "__main__":
    main()
