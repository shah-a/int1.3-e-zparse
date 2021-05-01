"""E-ZParse server."""

from dotenv import load_dotenv
from os import getenv
from flask import Flask, render_template, request, Response
from parse import load_pages, parse

load_dotenv()

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1 * (1024 ** 2)  # Sets 1 MB upload limit

@app.route('/', methods=['GET', 'POST'])
def home():
    """Homepage."""
    if request.method == 'GET':
        return render_template('index.html')

    tags = request.form.get('tags')
    tags = tags.split(',')
    tags = [tag.strip() for tag in tags]

    if tags[0].lower() == getenv('SECRET').lower():
        tags = getenv('INPUT').split(',')

    pdf_input = request.files.get('pdf')
    pdf_pages = load_pages(pdf_input)
    pdf_output = parse(pdf_pages, tags) if pdf_pages else None

    response = Response(pdf_output, mimetype="text/csv")
    response.headers.set("Content-Disposition", "attachment", filename='parsed.csv')

    return response

if __name__ == '__main__':
    app.run(debug=True)
