import qrcode

# Generate a fake scam QR code for testing
url = "http://free-lucky-winner.verify.xyz/bank"
img = qrcode.make(url)
img.save("test_qr.png")
print("Test QR code generated: test_qr.png")