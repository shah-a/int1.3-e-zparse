from flask import Flask, render_template, request, Response
from scripts.parse import load_pages, parse

app = Flask(__name__)
app.config['ENV'] = 'development'

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html')

    tags = request.form.get('tags')
    tags = tags.split(',')
    tags = [tag.strip() for tag in tags]

    pdf = request.files.get('pdf')
    pages = load_pages(pdf)
    result = parse(pages, tags)

    response = Response(result, mimetype="text/csv")
    response.headers.set("Content-Disposition", "attachment", filename='response.csv')

    return response

if __name__ == '__main__':
    app.run(debug=True)


"""
00406214663, 00406293975, 00407040487,
00407041779, 00408951196, 00409181239,
Lease Tag Fee-INT, Prepaid Toll Payment
"""
