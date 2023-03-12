import random
import os
import requests
from flask import Flask, render_template, abort, request
from functools import reduce


from QuoteEngine import Ingestor
from MemeEngine import MemeEngine

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']


    # quote_files variable
    quotes = list(reduce(lambda acc, items: acc + items, map(Ingestor.parse, quote_files), []))

    images_path = "./_data/photos/dog/"

    # images within the images images_path directory
    imgs = list(filter(lambda file_name: os.path.splitext(file_name)[1] == '.jpg',
                       map(lambda file_path: os.path.join(images_path, file_path), os.listdir(images_path))))

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    img = imgs[random.randint(0, len(imgs) - 1)]
    quote = quotes[random.randint(0, len(quotes) - 1)]
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    image_url = request.form['image_url']
    try:
        response = requests.get(image_url)
        tmp_path = os.path.join('./tmp/tmp.jpg')
        print(f'Status code {response.status_code}')
        if response.status_code == 200:
            img = response.content
            with open(tmp_path, 'wb') as f:
                f.write(img)
            path = meme.make_meme(tmp_path, request.form['body'], request.form['author'])
            return render_template('meme.html', path=path)
        else:
            return abort(response.status_code)
    except Exception as e:
        print("Error: ", e)

if __name__ == "__main__":
    app.run()
