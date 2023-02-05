import storage

storage.remount("/", readonly=False)

m = storage.getmount("/")
print(m.label)

storage.remount("/", readonly=True)

storage.enable_usb_drive()
