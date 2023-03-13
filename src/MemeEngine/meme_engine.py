import os

from PIL import Image, ImageDraw, ImageFont


class MemeEngine:
    """ Meme Engine """

    def __init__(self, output_dir):
        """ Initialize the MemeEngine class """
        self.output_dir = output_dir
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def make_meme(self, img_path, text, author, width=500) -> str:
        """ Create a meme given an image and a quote """
        try:
            font_path = os.path.join(os.path.dirname(__file__), '..', 'resources', 'roboto-regular.ttf')
            output_path = os.path.join(self.output_dir, 'meme.jpg')
            image = Image.open(img_path)
            height = int(width * image.height / image.width)
            image = image.resize((width, height))
            draw = ImageDraw.Draw(image)
            font = ImageFont.truetype(font_path, 30)
            draw.text((10, (height - 100)), text, fill='white', font=font)
            draw.text((10, (height - 50)), author, fill='white', font=font)
            image.save(output_path)
            return output_path
        except FileNotFoundError as e:
            print(f"Image {img_path} not found")
            raise e