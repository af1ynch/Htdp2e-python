# ****************************************************************************
#    ____    ___      ____    ____     ___    _   _    ____    ___    ____   *
#   / ___|  / _ \    | __ )  |  _ \   / _ \  | \ | |  / ___|  / _ \  / ___|  *
#  | |  _  | | | |   |  _ \  | |_) | | | | | |  \| | | |     | | | | \___ \  *
#  | |_| | | |_| |   | |_) | |  _ <  | |_| | | |\  | | |___  | |_| |  ___) | *
#   \____|  \___/    |____/  |_| \_\  \___/  |_| \_|  \____|  \___/  |____/  *
# Written by Mr. BaiKai                                                      *
# ****************************************************************************
import matplotlib.pyplot as plt


BASE_ATTENDEES = 120
BASE_PRICE = 5
CHANGE_ATTENDEES = 15
CHANGE_BASE_PRICE = 0.1
BASE_COST_PER_ATTENDEE = 180
INCREASE_COST_PER_ATTENDEE = 0.04


def attendees(ticket_price):
    return BASE_ATTENDEES - (ticket_price - BASE_PRICE) * (CHANGE_ATTENDEES / CHANGE_BASE_PRICE)


def revenue(ticket_price):
    return ticket_price * attendees(ticket_price)


def cost(ticket_price):
    return BASE_COST_PER_ATTENDEE + (INCREASE_COST_PER_ATTENDEE * attendees(ticket_price))


def profit(ticket_price):
    return revenue(ticket_price) - cost(ticket_price)


def frange(start, stop, step=0.1):

    while start < stop:
        yield round(start, 1)
        start += step

x = list(frange(0, 5.8, 0.1))
plt.plot(x, [profit(i) for i in x])
plt.show()