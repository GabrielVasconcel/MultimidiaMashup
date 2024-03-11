from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1> Bem-vindo, vá para a rota /librosa ou /spleeter </h1>'

@app.route('/spleeter')
def spleet_music():
    return render_template('index.html')

@app.route('/librosa')
def mashup():
    return render_template('librosa.html')


if __name__ == '__main__':
    app.run(debug=True)
