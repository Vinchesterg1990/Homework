from PIL import Image
# im = Image.open('Korsary-Vozvrashhenie-legendy.jpg')
# print(im.format, im.size,im.mode)
# out = im.resize((200,200))
# print(out.format, out.size,out.mode)
# im.show()
# out.show()
def logo(name):
    image = Image.open(name)
    w, h = image.size
    return image.resize((w//2, h//2))

im = logo('Korsary-Vozvrashhenie-legendy.jpg')
im_2 = logo('image (2).png')

im.paste(im_2,(100,100))
im.show()



