from PIL import Image
im = Image.open("yoxd.png")

print(im.format, im.size, im.mode)

box = (0, 0, 500, 500)
region = im.crop(box)
region.save("recorte.png")


r, g, b, a = im.split()
region = Image.merge("RGBA", (b,g,r,a))
region.save("cambio.png")

r, g, b, a = im.split()
region = Image.merge("RGBA", (b,r,g,a))
region.save("cambio2.png")

r, g, b, a = im.split()
region = Image.merge("RGBA", (r,b,g,a))
region.save("cambio3.png")

r, g, b, a = im.split()
region = Image.merge("RGBA", (g,r,b,a))
region.save("cambio4.png")

r, g, b, a = im.split()
region = Image.merge("RGBA", (g,b,r,a))
region.save("cambio5.png")

"""
out = im.rotate(45)
out.save("giro.png")

r, g, b = im.split()
region = Image.merge("RGB", (b,g,r))
region.save("cambio.png")

r, g, b = im.split()
region = Image.merge("RGB", (b,r,g))
region.save("cambio2.png")

r, g, b = im.split()
region = Image.merge("RGB", (r,b,g))
region.save("cambio3.png")

r, g, b = im.split()
region = Image.merge("RGB", (g,r,b))
region.save("cambio4.png")

r, g, b = im.split()
region = Image.merge("RGB", (g,b,r))
region.save("cambio5.png")
"""