import pyqrcode
import png
link = "https://www.linkedin.com/in/chinenyevm/"
qr_code = pyqrcode.create(link)
qr_code.png("linkedin.png", scale=5)
