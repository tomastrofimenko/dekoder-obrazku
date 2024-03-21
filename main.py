from PIL import Image

def decoder(result):
    with open(result, "r", encoding="UTF-8") as fr:
        width, height = map(int, fr.readline().split())
        image = Image.new("RGB", (width, height))
        pixels = image.load()
        for y in range(height):
            line = fr.readline().strip()
            for x in range(0, len(line), 6):
                if x + 6 <= len(line):
                    r = int(line[x:x+2], 16)
                    g = int(line[x+2:x+4], 16)
                    b = int(line[x+4:x+6], 16)
                    pixels[x//6, y] = (r, g, b)
    return image
decoded_image = decoder("result.txt")

decoded_image.save("vysledok.jpg")
decoded_image.show()
