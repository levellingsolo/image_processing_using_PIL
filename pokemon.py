from PIL import Image, ImageFilter

img = Image.open(r'.\pokedex\004 pikachu.jpg')

# print(img)
#
# print(img.size)
# print(img.format)
# print(img.mode)
# print(dir(img))


# for adding filters
filtered_image1 = img.filter(ImageFilter.CONTOUR)

#for saving the image
filtered_image1.save('blurry.png', 'png')



## using .convert method

filtered_image2 = img.convert('1')
filtered_image2.save('grey.png', 'png')


img2 = Image.open(r'.\pokedex\IMG20230227165308.jpg')
print(img2)
# img2.show()

filtered_image3 = img2.convert('1')
# filtered_image3.show()


filtered_image4 = img2.filter(ImageFilter.SHARPEN)
#rotating the image and show
# filtered_image4.rotate(100).show()





#resizing the image
filtered_image4.thumbnail((640, 640))
# resized_img2.convert('1').show()






#cropping the image

# box = (200, 200, 400, 400)
# resized_img2.crop(box).show()


# cropped = filtered_image4.crop(box)
# cropped.show()





#merging two images
def merge(img1, img2):
    w = img1.size[0] + img2.size[0]
    h = max(img1.size[1], img2.size[1])
    img_merged = Image.new("1", (w, h))

    img_merged.paste(img1)
    img_merged.paste(img2, (img.size[0], 0))

    return img_merged

merge(img, filtered_image4).show()
#
# print(img)





# img5 = Image.open(r'alwen-yRkqGcvZuOc-unsplash.jpg')
# print('img 5', img5)
# resize_img5 = img5.resize((800, 300))
# resize_img5.save(r'uneven_thumbnail.jpg')


#thumbnail
img5 = Image.open(r'alwen-yRkqGcvZuOc-unsplash.jpg')
print('before thumbnail', img5)
# thumbnail does not return anything . it does changing in the original one.
img5.thumbnail((800, 300))
img5.show()
print(img5)


print('hello')
print('second commit')
