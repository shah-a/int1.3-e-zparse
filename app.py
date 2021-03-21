from flask import Flask, render_template, request

app = Flask(__name__)
app.config['ENV'] = 'development'

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        tags = request.form.get('tags')
        tags = tags.split(',')
        tags = [tag.strip() for tag in tags]
        print(tags)
        return render_template('index.html')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
