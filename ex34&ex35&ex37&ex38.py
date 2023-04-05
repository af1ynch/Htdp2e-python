# ****************************************************************************
#    ____    ___      ____    ____     ___    _   _    ____    ___    ____   *
#   / ___|  / _ \    | __ )  |  _ \   / _ \  | \ | |  / ___|  / _ \  / ___|  *
#  | |  _  | | | |   |  _ \  | |_) | | | | | |  \| | | |     | | | | \___ \  *
#  | |_| | | |_| |   | |_) | |  _ <  | |_| | | |\  | | |___  | |_| |  ___) | *
#   \____|  \___/    |____/  |_| \_\  \___/  |_| \_|  \____|  \___/  |____/  *
# Written by Mr. BaiKai                                                      *
# ****************************************************************************



def string_first(string):
    """
        Function Signature:String -> String
        Purpose Statement: extract the first character from a non-empty string
        Function Examples:
            given: "helloworld"  expected: "h"
            given: "htdp" expect: "h"
    """
    return string[0]


def string_last(string):
    """
        String -> String
        extract the last character from a non-empty string
        given: "helloworld" expected: "d"
        given: "htdp" expected: "p"
    """
    return string[-1]


def string_rest(string):
    """
        String -> String
        produce a string like the given one with the first character removed
        given: "helloworld" expected: "elloworld"
        given: "htdp" expected: "tdp"
    """
    return string[1:]


def string_remove_last(string):
    """
        String -> String
        produce a string like the given one with the last character removed


    """
    string_length = len(string)
    return string[:string_length - 1]



test_str1 = "helloworld"
test_str2 = "htdp"
print(string_first("helloworld"))
print(string_first("htdp"))
print(string_last("helloworld"))
print(string_last("htdp"))
print(string_rest(test_str1))
print(string_rest(test_str2))
print(string_remove_last(test_str1))