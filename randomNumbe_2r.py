#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# team: Wenqi, Tatiana, Elisabeth
# todays date:16.06.20

import random
import time
import sys
import matplotlib.pyplot as plt

def get_random_number(start, end):
    num = random.randint(start, end)
    return num


def write_log_file(outputfilename, data):
    f = open(output_file + ".log", "a")
    f.write("Our randomly generated number is " + str(data) + " (" + time.strftime("%H:%M:%S") + ")\n")
    f.close()


def get_color_by_dice_roll(spots):
    if spots == 1:
        color = 'blue'
    elif spots == 2:
        color = 'green'
    elif spots == 3:
        color = 'red'
    elif spots == 4:
        color = 'yellow'
    elif spots == 5:
        color = 'purple'
    else: color = 'orange'
    return color


if __name__ == "__main__":
    output_file = "randomNumber"
    roll = get_random_number(1, 6)
    color = get_color_by_dice_roll(roll)
    write_log_file(output_file, roll)
    dice_rolls=[]
    for i in range(6):
        roll = get_random_number(1, 6)
        dice_rolls.append(roll)
    print(dice_rolls)
    sys.stdout.flush()
    plt.barh(range(6),dice_rolls)
    plt.show()