# boot.py
`boot.py` lives in the root of your keyboard when mounted as a storage device. 
There is a more detailed explanation in the [circuit python docs](https://docs.circuitpython.org/en/latest/README.html), 
however there are some common use cases for your keyboard listed here.

## Hiding device storage
You can hide your device from showing up as a USB storage by default (this can be overridden 
at startup if desired, per the example code further down this page).

```python
storage.disable_usb_drive()
```

## Using your keyboard before the OS loads
You can make your keyboard work in your computer's BIOS and bootloader (useful if you dual-boot).

```python
usb_hid.enable(boot_device=1)
```

## Disabling serial communication
By default, you can connect to your board's serial console, which can be useful for debugging, 
but may not be desired for everyday use.

```python
# Equivalent to usb_cdc.enable(console=False, data=False)
usb_cdc.disable()
```

## Example code
Below is a fully working example, which disables USB storage, CDC and enables BIOS mode.

```python
import supervisor
import board
import digitalio
import storage
import usb_cdc
import usb_hid

from kb import KMKKeyboard
from kmk.scanners import DiodeOrientation


# If this key is held during boot, don't run the code which hides the storage and disables serial
# This will use the first row/col pin. Feel free to change it if you want it to be another pin
col = digitalio.DigitalInOut(KMKKeyboard.col_pins[0])
row = digitalio.DigitalInOut(KMKKeyboard.row_pins[0])

if KMKKeyboard.diode_orientation == DiodeOrientation.COLUMNS:
    col.switch_to_output(value=True)
    row.switch_to_input(pull=digitalio.Pull.DOWN)
else:
    col.switch_to_input(pull=digitalio.Pull.DOWN)
    row.switch_to_output(value=True)

if not row.value:
    storage.disable_usb_drive()
    # Equivalent to usb_cdc.enable(console=False, data=False)
    usb_cdc.disable()
    usb_hid.enable(boot_device=1)

row.deinit()
col.deinit()
```
