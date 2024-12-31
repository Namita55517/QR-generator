import qrcode
img = qrcode.make('https://www.facebook.com/rojina.subedi.587')
img.save("luna.png")
img.show()
