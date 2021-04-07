import qrcode
import cv2


def create_qrcode(text):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )

    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white").convert("RGB")
    img.save("./static/response.png")


def decode_qrcode(filepath):
    img = cv2.imread(filepath)
    detect = cv2.QRCodeDetector()

    decoded_text, points, straight_qrcode = detect.detectAndDecode(img)

    return decoded_text
