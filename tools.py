def printGreen(a):
    # 打印绿色
    print('\033[32m%s\033[0m' % a)


def printRed(a):
    # 打印红色
    print('\033[32m%s\033[0m' % a)


def notMain():
    print("It is NOT main program!")


if __name__ == "__main__":
    notMain()
