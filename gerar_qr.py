import qrcode

url = "http://192.168.86.7:5000"

qr = qrcode.make(url)
qr.save("qrcode_votacao.png")
print("QR Code salvo como qrcode_votacao.png")
