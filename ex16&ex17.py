# ****************************************************************************
#    ____    ___      ____    ____     ___    _   _    ____    ___    ____   *
#   / ___|  / _ \    | __ )  |  _ \   / _ \  | \ | |  / ___|  / _ \  / ___|  *
#  | |  _  | | | |   |  _ \  | |_) | | | | | |  \| | | |     | | | | \___ \  *
#  | |_| | | |_| |   | |_) | |  _ <  | |_| | | |\  | | |___  | |_| |  ___) | *
#   \____|  \___/    |____/  |_| \_\  \___/  |_| \_|  \____|  \___/  |____/  *
# Written by Mr. BaiKai                                                      *
# ****************************************************************************
from PIL import Image


def image_area(file_path):

    img = Image.open(file_path)
    image_height = img.height
    image_width = img.width
    print(image_height * image_width)


def image_classify(file_path):

    img = Image.open(file_path)
    image_height = img.height
    image_width = img.width
    if image_height > image_width:
        print("tall")
    elif image_width > image_height:
        print("wide")
    else:
        print("square")


image_area("img_path")
image_classify("img_path")
