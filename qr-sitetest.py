import qrcode

# Le contenu du QR code (texte ou URL)
data = "https://etsvrignaud.github.io/ets-vrignaud/"

# Génération du QR code
qr = qrcode.make(data)

# Enregistrement dans un fichier image
qr.save("mon_qrcode.png")

print("QR code généré avec succès !")