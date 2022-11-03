from escpos.printer import Dummy, Usb, Serial
from escpos.escpos import Escpos


def create_printer(printer_driver: str, printer_settings: dict) -> Escpos:

    if printer_driver == "Usb":
        return Usb(*printer_settings)

    if printer_driver == "Serial":
        return Serial(*printer_settings)

    return Dummy()
