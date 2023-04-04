# ****************************************************************************
#    ____    ___      ____    ____     ___    _   _    ____    ___    ____   *
#   / ___|  / _ \    | __ )  |  _ \   / _ \  | \ | |  / ___|  / _ \  / ___|  *
#  | |  _  | | | |   |  _ \  | |_) | | | | | |  \| | | |     | | | | \___ \  *
#  | |_| | | |_| |   | |_) | |  _ <  | |_| | | |\  | | |___  | |_| |  ___) | *
#   \____|  \___/    |____/  |_| \_\  \___/  |_| \_|  \____|  \___/  |____/  *
# Written by Mr. BaiKai                                                      *
# ****************************************************************************
from numbers import Number


def c_volume(a):

    if isinstance(a, Number):
        volume = a ** 3
        print("%.2f" % volume)
    else:
        raise "It's not a number. Please input a number."


def c_surface(b):

    if isinstance(b, Number):
        surface = 6 * (b ** 2)
        print("%.2f" % surface)
    else:
        raise "It's not a number.Please input a number."


t = 3.1
c_volume(t)
c_surface(t)