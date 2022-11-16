echo 'SUBSYSTEMS=="usb", ATTRS{idVendor}=="0483" , GROUP="plugdev" , MODE="0666"' > /etc/udev/rules.d/50-myusb.rules


udevadm control --reload-rules
udevadm control --reload

udevadm trigger