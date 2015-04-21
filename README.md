pyusb-keyboard-alike
====================

Handler for keyboards and keyboard-alike devices like bar code scanners, RFID readers.

You will find some reusable base classes and few example classes handling data reading from USB bar code scanner and RFID reader that
emulate keyboards.


Requirements
------------
* pyusb 1.X (not 0.4)


How to use
----------
The **keyboard_alike** folder holds a re-usable Reader class. In most case you will be able to use it just by passing correct arguments.

There are device examples:

* newland.py - Newland 2D barcode scanner (NLS-HR32)

Exceptions
----------
Sometimes pyusb/Reader class will throw exceptions, more often at start when it may read some leftover data (will throw "Got X bytes instead of Y").
Some devices *support* resetting, which seems to prevent any weird reads (Lindy bar code scanner works with reset, while the RFID reader stops working if reset is called).

Lack of permissions will also cause exceptions. The code will have to run as root/sudo or you will have to use udev rules to add permissions for given device.

Sometimes *unknown* exceptions may show up. In many cases retrying to run the code works. In some other the device must be re-connected. Example:

```
keyboard_alike.reader.DeviceException: Could not set configuration: [Errno None] Unknown error
```


Handling new devices
--------------------
If you want to handle your device then at start some experimenting/debugging is required to get to know the device.

* Assuming you are using Linux - connect the device and print **dmesg** (or use **lsusb**) to get the VENDOR and DEVICE id 
* For the code the vendor and device IDs are *0xTHE_VALUE_YOU_GOT* (the 0x at start)
* Next stage is to check the raw output from the device - a list of digits that actually is a set of smaller lists-chunks that we will have to find
* Use debug=True and some data_size/chunk_size - it will print the list with raw data and quite likely it will raise an exception that it didn't got *data_size* of data
* Look on the list and see how many elements is in one chunk. In every chunk the value must be at the same index, like those are 6 element chunks:

```
0, 0, 31, 0, 0, 0,
0, 0, 27, 0, 0, 0
```


Credits
-------
* The original code was based on https://github.com/guyzmo/tmsr33-pyusb by Guyzmo Pratz
* This code was based on https://github.com/riklaunim/pyusb-keyboard-alike
