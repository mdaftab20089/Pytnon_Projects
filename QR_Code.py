import qrcode as qr
img=qr.make("https://www.youtube.com/watch?v=FOGRHBp6lvM&list=PPSV")
img.save("aftab_qr.png")