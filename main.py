import qrcode

# Enlace del archivo PDF que obtuviste de Google Drive carpeta
url_1 = "https://drive.google.com/drive/folders/1NFzirJinjdW83Wl36llKHH-K-2l2FsGX?usp=sharing"
url_2 = "https://drive.google.com/file/d/1lyRaviLzbtHpVjeC_LcSOcKzSi9GFa5o/view?usp=sharing"

urls = [
    { 'name': 'opciones_sazon', 'link': url_1  },
    { 'name': 'menu_sazon', 'link': url_2  }
    ]

for url_item in urls:
    # Generar el código QR para el enlace
    img = qrcode.make(url_item['link'])

    # Guardar el código QR en un archivo usando el nombre del enlace
    filename = "qrImages/{}.png".format(url_item['name'])
    img.save(filename)
