# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2021 Neradoc
#
# SPDX-License-Identifier: Unlicense

import time
import board
import digitalio
import usb_hid
from adafruit_hid.consumer_control import ConsumerControl
from consumer_control_extended import AL_TEXT_EDITOR, AL_CALCULATOR

cc = ConsumerControl(usb_hid.devices)

# define buttons. these can be any physical switches/buttons, but the values
# here work out-of-the-box with a FunHouse UP and DOWN buttons.
button_up = digitalio.DigitalInOut(board.BUTTON_UP)
button_up.switch_to_input(pull=digitalio.Pull.DOWN)

button_down = digitalio.DigitalInOut(board.BUTTON_DOWN)
button_down.switch_to_input(pull=digitalio.Pull.DOWN)

while True:
    if button_up.value:
        print("Button up pressed!")
        # open the system text editor
        cc.send(AL_TEXT_EDITOR)

    if button_down.value:
        print("Button down pressed!")
        # open the calculator
        cc.send(AL_CALCULATOR)

    time.sleep(0.2)
