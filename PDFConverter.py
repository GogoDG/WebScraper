import os

from PIL import Image

path = "D:/Minecraft Stuff/RPGs/D&D/anyflipdownload/Spelljammer꞉ Boo's Astral Menagerie (BAM) [Standard Cover + Errata]"

images = [i for i in os.listdir(path) if i.endswith('png')]
iml = []
for image in images:
    img = Image.open(path + "/" + image)
    im = img.convert('RGB')
    iml.append(im)
ia = iml[0]
iml.pop(0)
ia.save(path + "/Spelljammer꞉ Boo's Astral Menagerie (BAM) [Standard Cover + Errata].pdf", save_all=True, append_images=iml)

