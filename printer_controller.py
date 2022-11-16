from escpos.printer import Dummy, Usb, Serial
from escpos.escpos import Escpos


def string_to_hex(string_var: str):
    an_integer = int(string_var, 16)
    #hex_value = hex(an_integer)
    # print(hex_value)
    return an_integer


def create_printer(printer_driver: str, printer_settings: dict) -> Escpos:

    if printer_driver == "Usb":
        printer_settings["idVendor"] = string_to_hex(
            printer_settings["idVendor"])
        printer_settings["idProduct"] = string_to_hex(
            printer_settings["idProduct"])
        return Usb(**printer_settings)
    if printer_driver == "Serial":
        return Serial(**printer_settings)

    return Dummy()
