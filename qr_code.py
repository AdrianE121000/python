import qrcode

qr = qrcode.QRCode()
qr.add_data("https://tracker.axie.management")
img = qr.make_image()
img.save("qr.png")