import qrcode

# Enlace del archivo PDF que obtuviste de Google Drive PDF
# url = "https://drive.google.com/file/d/1tbdCNCBIetWjrmEzQQ1ySujFYQV-7eYS/view"
# Enlace del archivo PDF que obtuviste de Google Drive carpeta
url = "https://drive.google.com/drive/folders/1sS4j9IIhr7jWranIcGdKBTkW9WCYgB3T"
# Generar el código QR
img = qrcode.make(url)

# Guardar el código QR en un archivo
img.save("qrImages/Folder_menu_qr.png")
