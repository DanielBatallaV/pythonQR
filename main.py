import qrcode

# Enlace del archivo PDF que obtuviste de Google Drive carpeta
url_1 = "https://drive.google.com/file/d/1OXFm-_C8kP6_VdWOJtkDPwkbYPZW4ev4/view?usp=sharing"

urls = [
    { 'name': 'QRSazon', 'link': url_1  }
    ]

for url_item in urls:
    # Generar el código QR para el enlace
    img = qrcode.make(url_item['link'])

    # Guardar el código QR en un archivo usando el nombre del enlace
    filename = "qrImages/{}.png".format(url_item['name'])
    img.save(filename)
