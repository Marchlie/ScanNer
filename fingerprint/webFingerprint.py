import requests


def webFingerprint(scanInfo) -> dict:
    targetIP = scanInfo["targetIP"]
    targetPort = scanInfo["targetPort"]
    isDebug = scanInfo["isDebug"]
    portlist = scanInfo["portlist"]
    timeout = 3

    webText = []
    for port in scanInfo["portlist"]:
        url = "http://" + targetIP + ":" + str(port)
        r = requests.get(url)
        webText = webText.append(r.text)
    return webText
