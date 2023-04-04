# ****************************************************************************
#    ____    ___      ____    ____     ___    _   _    ____    ___    ____   *
#   / ___|  / _ \    | __ )  |  _ \   / _ \  | \ | |  / ___|  / _ \  / ___|  *
#  | |  _  | | | |   |  _ \  | |_) | | | | | |  \| | | |     | | | | \___ \  *
#  | |_| | | |_| |   | |_) | |  _ <  | |_| | | |\  | | |___  | |_| |  ___) | *
#   \____|  \___/    |____/  |_| \_\  \___/  |_| \_|  \____|  \___/  |____/  *
# Written by Mr. BaiKai                                                      *
# ****************************************************************************


def string_first(sf):
    if isinstance(sf, str):
        print(sf[0])
    else:
        raise TypeError


def string_last(sl):
    if isinstance(sl, str):
        print(sl[-1])
    else:
        raise TypeError


string_test = "This is a str."
num = 1
string_first(string_test)
string_last(string_test)
# string_first(num)
# string_last(num)