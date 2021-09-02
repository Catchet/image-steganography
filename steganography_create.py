from PIL import Image

bits_total = 8
bits_for_secret = 4

PublicImg = Image.open("public_image.png")
SecretImg = Image.open("secret_image.png")
CombinedImg = Image.new("RGB", (PublicImg.size[0], PublicImg.size[1]), "black")  # Create an empty image with the same dimensions as PublicImg
PublicPixels = PublicImg.load()
SecretPixels = SecretImg.load()

PublicImg.show()     # Displays the public original image
for i in range(PublicImg.size[0]):
    for j in range(PublicImg.size[1]):
        rgb = [0, 0, 0]
        for k in range(3):
            rgb[k] = (PublicPixels[i, j][k] & ((1 << bits_total) - 2**bits_for_secret)) + (SecretPixels[i, j][k] >> (bits_total - bits_for_secret))
        CombinedImg[i, j] = tuple(rgb)
CombinedImg.show()   # Displays the combined image



for i in range(CombinedImg.size[0]):
    for j in range(CombinedImg.size[1]):
        SecretPixels[i, j] = tuple((x & (2**bits_for_secret - 1)) << (bits_total - bits_for_secret) for x in CombinedImg[i, j])
SecretImg.show()     # Displays the extracted secret image

CombinedImg.save("combined_image.png")  # Save the combined image
