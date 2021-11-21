Introduction
============


.. image:: https://readthedocs.org/projects/consumer-control-extended/badge/?version=latest
    :target: https://consumer-control-extended.readthedocs.io/
    :alt: Documentation Status


.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://adafru.it/discord
    :alt: Discord


.. image:: https://github.com/Neradoc/CircuitPython_consumer_control_extended/workflows/Build%20CI/badge.svg
    :target: https://github.com/Neradoc/CircuitPython_consumer_control_extended/actions
    :alt: Build Status


.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: Code Style: Black

A big list of all HID consumer controls


Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://circuitpython.org/libraries>`_
or individual libraries can be installed using
`circup <https://github.com/adafruit/circup>`_.

Installing from PyPI
=====================

On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/circuitpython-consumer-control-extended/>`_.
To install for current user:

.. code-block:: shell

    pip3 install circuitpython-consumer-control-extended

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install circuitpython-consumer-control-extended

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .env
    source .env/bin/activate
    pip3 install circuitpython-consumer-control-extended



Installing to a Connected CircuitPython Device with Circup
==========================================================

Make sure that you have ``circup`` installed in your Python environment.
Install it with the following command if necessary:

.. code-block:: shell

    pip3 install circup

With ``circup`` installed and your CircuitPython device connected use the
following command to install:

.. code-block:: shell

    circup install consumer_control_extended

Or the following command to update an existing version:

.. code-block:: shell

    circup update

Usage Example
=============

.. code-block:: python

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

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/Neradoc/CircuitPython_consumer_control_extended/blob/HEAD/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Documentation
=============

For information on building library documentation, please check out
`this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.
