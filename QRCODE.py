import PySimpleGUI as sg
import qrcode

layout = [[sg.Text('Enter text:'), sg.InputText(key= 'INPUT')],
          [sg.Button('Create', key = 'CREATE')],
          [sg.Button('Exit', key = 'EXIT')]]

window = sg.Window('QR Code Generator', layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    if event == 'EXIT':
        break
    
    if event == 'CREATE':
        text = values['INPUT']

qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(text)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.show()


# # Generate QR code image with custom size and color
# qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
# qr.add_data(text)
# qr.make(fit=True)
# img = qr.make_image(fill_color="black", back_color="white").resize((300, 300))

try:
    img.show()
except:
    sg.popup_error("Error: Unable to generate QR code.")
finally:
    print('QR code generated successfully')

window.close()