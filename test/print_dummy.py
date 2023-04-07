from escpos.printer import Dummy, File

id_vendor = 0x0483
id_product = 0x5743

p = Dummy()
for i in range(10):
    p.text("Hello World\n")
    # p.image("logo.gif")
p.cut()
p.barcode('1324354657687', 'EAN13', 64, 2, '', '')
p.cashdraw(2)

f = open("demofile2.txt", "wb")
f.write(p.output)
f.close()
