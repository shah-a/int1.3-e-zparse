from flask import Flask, render_template, request, redirect, url_for
import pdfplumber

app = Flask(__name__)
app.config['ENV'] = 'development'

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        tags = request.form.get('tags')
        tags = tags.split(',')
        tags = [tag.strip() for tag in tags]

        file = request.files.get('pdf')

        if not file:
            return redirect(url_for('home'))

        with pdfplumber.open(file) as pdf:
            pages = [page.extract_text() for page in pdf.pages]

        print(pages[0])

        return redirect(url_for('home'))
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
