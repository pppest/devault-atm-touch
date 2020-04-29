# this code is mostly a mixup based on code found in the links below
# zbar: https://www.pyimagesearch.com/2018/05/21/an-opencv-barcode-and-qr-code-
#   scanner-with-zbar/
# video: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/
#   py_gui/py_video_display/py_video_display.html

from pyzbar import pyzbar
import cv2
import time
import qrcode


def generate_qr_code(data):
    file = './images/qr_codes/qr-' + str(time.time()) + '.png'
    img = qrcode.make(data)
    img.save(file)
    return file

def read_qr_code():
    barcode_data = ""
    print("Scan wallet QR code")
    capture = cv2.VideoCapture(0)
    start = time.time()

    while(capture.isOpened()):
        ret, frame = capture.read()
        if ret is True:
            # check for qrcode and write if found and exit
            barcodes = pyzbar.decode(frame)
            # loop over the detected barcodes
            for barcode in barcodes:
                # extract the bounding box location of the barcode and draw the
                # bounding box surrounding the barcode on the image
                (x, y, w, h) = barcode.rect
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
                # the barcode data is a bytes object so if we want to draw
                # it on
                # our output image we need to convert it to a string first
                barcode_data = barcode.data.decode("utf-8")
                barcode_type = barcode.type
                # print the barcode type and data to the terminal
                print("Found {} barcode: {}".format(barcode_type, barcode_data))
                ## Make sure its a devault wallet
                if "devault:" not in barcode_data:
                    print("NOT a DeVault wallet!!!")
                    barcodes = []
            if barcodes != []:
                    break
        else:
            break
    capture.release()
    cv2.destroyAllWindows()
    return barcode_data
