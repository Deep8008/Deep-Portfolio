from PIL import Image

'''
This program gets a text and encode it in the image
'''

print("=== Image Text Encoder ===")

img_path = input("Enter image path: ")
img = Image.open(img_path)

my_text = input("Enter your secret message: ") + "|"
crypted_text = [ord(ch) for ch in my_text]

#formula#

jumpx = img.size[0] // 100
jumpy = img.size[1] // 100

k = 0   #counter#
for i in range(0, img.size[0], jumpx):
    for j in range(0, img.size[1], jumpy):
        if k < len(crypted_text):
            r, g, b = img.getpixel((i, j))
            img.putpixel((i, j), (crypted_text[k], g, b))
            k += 1

output_path = input("Enter output file path (ex: encoded.png): ")
img.save(output_path)

print("Message encoded and saved successfully!")
