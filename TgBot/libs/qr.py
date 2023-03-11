from io import BytesIO
import qrcode
from qrcode.exceptions import DataOverflowError
import logging


def make_qr(data: str, error_correction: int = 1) -> BytesIO:
    qr_file = BytesIO()
    qr = qrcode.QRCode(error_correction=error_correction)
    data = data[:784]
    qr.add_data(data)
    qr_image = qr.make_image()
    qr_image.save(qr_file, "JPEG")
    return qr_file
