from PIL import Image

bits_total = 8
bits_for_secret = 4

CombinedImg = Image.open("combined_image.png")
SecretImg = Image.new("RGB", (CombinedImg.size[0], CombinedImg.size[1]), "black")
CombinedPixels = CombinedImg.load()
SecretPixels = SecretImg.load()


for i in range(CombinedImg.size[0]):
    for j in range(CombinedImg.size[1]):
        SecretPixels[i, j] = tuple((x & (2**bits_for_secret - 1)) << (bits_total - bits_for_secret) for x in CombinedPixels[i, j])

CombinedImg.show()  # Displays the combined image
SecretImg.show()    # Displays the extracted secret image