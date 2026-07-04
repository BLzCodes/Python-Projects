import os
import platform
import qrcode

qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=40,
    border=16,
)

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def makeQR():
    link = input("Enter a link to convert: ")
    try:
        qr.add_data(link)
        qr.make(fit=True)
        print("Link converted successfully!\n")
        saveQR(qr)
    except:
        print("Not a valid link.")
        input("Press any key to continue")
        clear_console()
        makeQR()

def saveQR(qr):
    try:
        img = qr.make_image(fill_color="#000000", back_color="#FFC17B")
        name = input("Name the saved image: ")
        path = "saved\\"+name+".png"
        img.save(path)

        if platform.system() == 'Windows':
            os.startfile(path)
        elif platform.system() == 'Darwin':
            os.system(f"open {path}")
        else:
            os.system(f"xdg-open {path}")

        input("Image saved successfully in \"saved\" folder!")
        clear_console()
        makeQR()
    except:
        input("Invalid characters. Try again.")
        saveQR(qr)

makeQR()
