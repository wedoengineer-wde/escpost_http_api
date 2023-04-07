from printer_controller import create_printer


def test_create_printer():

    printer_drive = "Dummy"
    printer_settings = {}
    printer = create_printer(printer_drive, printer_settings)

    assert type(printer).__name__ == "Dummy"

    printer_drive = "Usb"
    printer_settings = {
        "id_vendor": 0x0483,
        "id_product": 0x5743
    }

    #printer = create_printer(printer_drive , printer_settings)

    #assert type(printer).__name__ == "Usb"
