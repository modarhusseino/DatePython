import time
import os
import platform


def clear():
    if platform.system() == 'Linux' or platform.system() == 'Darwin':
        os.system('clear')
    else:
        os.system('cls')


while True:

    Time = time.localtime()
    year =Time[0]
    month =Time[1]
    day = Time[2]
    hour = Time[3]
    minute = Time[4]
    second = Time[5]

    time.sleep(1)
    clear()

    print("""
        date: {}/{}/{}
        hour: {}:{}:{}
        """.format(day, month, year, hour,minute, second))