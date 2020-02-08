from PIL import Image
import os
import uuid


def crop_image(img, size, step):
    result = []
    x, y = 0, 0
    while y + size <= img.height:
        while x + size <= img.width:
            cropped_img = img.crop((x, y, x + size, y + size))
            result.append(cropped_img)
            x += step
        y += step
        x = 0
    return result


if not os.path.exists('./data'):
    os.mkdir('./data')

img_names = os.listdir('./raw_data')

for name in img_names:
    image = Image.open('./raw_data/' + name)

    arr = crop_image(image, 64, 64)
    image.close()

    for img in arr:
        img.save('data/' + str(uuid.uuid1()) + '.png')
        img.close()
