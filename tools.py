#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
Tools for main program
"""


class log:
    import time

    def info(self, msg):
        print(msg)
        with open(
            "log"
            + self.time.strftime("%Y-%m-%d", self.time.localtime(self.time.time()))
            + ".txt",
            "a",
        ) as f:
            f.write(
                "info"
                + self.time.strftime(
                    "%Y-%m-%d %H:%M:%S", self.time.localtime(self.time.time())
                )
                + " "
                + msg
                + "\n"
            )

    def warning(self, msg):
        print(msg)
        with open(
            "log"
            + self.time.strftime("%Y-%m-%d", self.time.localtime(self.time.time()))
            + ".txt",
            "a",
        ) as f:
            f.write(
                "warning"
                + self.time.strftime(
                    "%Y-%m-%d %H:%M:%S", self.time.localtime(self.time.time())
                )
                + " "
                + msg
                + "\n"
            )

    def debug(self, msg):
        print(msg)
        with open(
            "log"
            + self.time.strftime("%Y-%m-%d", self.time.localtime(self.time.time()))
            + ".txt",
            "a",
        ) as f:
            f.write(
                "debug"
                + self.time.strftime(
                    "%Y-%m-%d %H:%M:%S", self.time.localtime(self.time.time())
                )
                + " "
                + msg
                + "\n"
            )


def printGreen(a):
    # 打印绿色
    print("\033[32m%s\033[0m" % a)


def printRed(a):
    # 打印红色
    print("\033[32m%s\033[0m" % a)


def notMain():
    print("It is NOT main program!")


if __name__ == "__main__":
    notMain()
