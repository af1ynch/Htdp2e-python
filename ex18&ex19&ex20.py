# ****************************************************************************
#    ____    ___      ____    ____     ___    _   _    ____    ___    ____   *
#   / ___|  / _ \    | __ )  |  _ \   / _ \  | \ | |  / ___|  / _ \  / ___|  *
#  | |  _  | | | |   |  _ \  | |_) | | | | | |  \| | | |     | | | | \___ \  *
#  | |_| | | |_| |   | |_) | |  _ <  | |_| | | |\  | | |___  | |_| |  ___) | *
#   \____|  \___/    |____/  |_| \_\  \___/  |_| \_|  \____|  \___/  |____/  *
# Written by Mr. BaiKai                                                      *
# ****************************************************************************


def string_join(str1, str2):

    if isinstance(str1, str) and isinstance(str2, str):
        print(str1 + "_" + str2)
    else:
        raise TypeError


def string_insert(str1, i):

    if i >=0 and i <= len(str1):
        print(str1[:i] + "_" + str1[i:])
    else:
        raise "string index out of range."


def string_delete(str1, i):

    if len(str1) > 0:
        if i >=0 and i <= len(str1):
            print(str1[:i-1] + str1[i:])
        else:
            raise "string index out of range."
    else:
        raise "We need a non-empty str."


# string_join("hello", "world")
# string_join(1, 2)
# string_insert("", 0)
string_delete("", 0)