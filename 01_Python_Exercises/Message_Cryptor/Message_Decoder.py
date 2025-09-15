from PIL import Image

'''
this program decodes the text hiding in image
'''

print("=== Image Text Decoder ===")
img_path = input("Enter encoded image path: ")
img = Image.open(img_path)

decoded = []
found = False

#formula#

jumpx = img.size[0] // 100
jumpy = img.size[1] // 100

k = 0   #counter#
for i in range(0, img.size[0], jumpx):
    for j in range(0, img.size[1], jumpy):
        r, g, b = img.getpixel((i, j))
        if r != 0:
            ch = chr(r)
            if ch == "|":
                found = True
                break
            decoded.append(ch)
    if found:
        break

print("Decoded message:", "".join(decoded))
