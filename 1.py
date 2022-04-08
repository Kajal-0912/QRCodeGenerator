import qrcode

img = qrcode.make("https://www.youtube.com/watch?v=-GmJLI122ZM")
img.save("DUH.jpg")

img1 = qrcode.make("0001KajalSingh")
img1.save("0001.jpg")

img1 = qrcode.make("0002Krishna")
img1.save("0002.jpg")

import cv2
d = cv2.QRCodeDetector()

retval, points, straight_qrcode = d.detectAndDecode(cv2.imread("0001.jpg"))

print(retval)


img3 = qrcode.make("0003IshanSharma")
img3.save("0003.jpg")

img4 = qrcode.make("0004Sneha")
img4.save("0004.jpg")
