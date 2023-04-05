# ****************************************************************************
#    ____    ___      ____    ____     ___    _   _    ____    ___    ____   *
#   / ___|  / _ \    | __ )  |  _ \   / _ \  | \ | |  / ___|  / _ \  / ___|  *
#  | |  _  | | | |   |  _ \  | |_) | | | | | |  \| | | |     | | | | \___ \  *
#  | |_| | | |_| |   | |_) | |  _ <  | |_| | | |\  | | |___  | |_| |  ___) | *
#   \____|  \___/    |____/  |_| \_\  \___/  |_| \_|  \____|  \___/  |____/  *
# Written by Mr. BaiKai                                                      *
# ****************************************************************************
from PIL import Image


def image_area(image_path):
    """
        Image Path -> Number
        count the number of pixels in an image
        given: "J20-3.jpg" expected: 1920*1080

    """
    image = Image.open(image_path)
    image_height = image.height
    image_width = image.width
    return image_height * image_width


print(image_area("J20-3.jpg"))
