from PIL import Image


def get_image(image_file):
    try:
        image = Image.open(image_file)
        print(image.size)
        print(image.mode)
        print(image.format)
        image.show()

        image_blackwhite = image.convert('L')
        image_blackwhite.show()
        image_blackwhite.save('miku_bn.jpg')

    except Exception as e:
        print('no se encontro la imagen: ', e)


if __name__ == '__main__':
    get_image('miku.jpg')
