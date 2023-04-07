from escpos.printer import Usb

id_vendor = 0x0483
id_product = 0x5743

p = Usb(id_vendor, id_product)
p.text("ADSFASDFASDFASDFASDFASDF\n")
p.text("ADSFASDFASDFASDFASDFASDF\n")
p.text("ADSFASDFASDFASDFASDFASDF\n")
p.text("ADSFASDFASDFASDFASDFASDF\n")
# for i in range(10):
#    p.text("Hello World\n")
# p.image("logo.gif")
# p.cut()
#p.barcode('1324354657687', 'EAN13', 64, 2, '', '')
# p.cashdraw(2)
