from PIL import Image
import os


def compress_images(image_folder):
    try:
        for file in os.listdir(image_folder):
            file_name, file_extension = os.path.splitext(file)
            print('comprimiendo archivo ' + file_name + file_extension)

            if file_extension == '.jpg':
                file_compress = Image.open(image_folder + file)
                file_compress.save(image_folder + file_name +
                                   "comprimido.jpg", optimize=True,
                                   quality=70)
    except Exception as e:
        print('no se pudo comprimir: ', e)
<<<<<<< HEAD
        print('esto debe ser para main')
=======
        print('nice')
        print('lose')
>>>>>>> rama-prueba


if __name__ == '__main__':
    compress_images('D:/anime/Waifus/Akame/')
