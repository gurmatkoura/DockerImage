import qrcode

def create_qrcode(data: str):
    """Create a QR code"""

    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5)
    qr.add_data(data)
    qr.make(fit=True)
    return qr.make_image(fill='black', back_color='white')

