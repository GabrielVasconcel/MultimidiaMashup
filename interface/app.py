import os
import librosa
import soundfile as sf
import numpy as np
from flask import Flask, request, send_file, redirect, url_for, render_template

app = Flask(__name__)

# Função para criar o mashup
def create_mashup(file1, file2, output_file):
    # Carregar os arquivos de áudio
    audio1, sr1 = librosa.load(file1, sr=None)
    audio2, sr2 = librosa.load(file2, sr=None)

    # Ajustar o tempo da faixa mais curta para corresponder à faixa mais longa
    if len(audio1) > len(audio2):
        rate = len(audio1) / len(audio2)
        audio2 = librosa.effects.time_stretch(audio2, rate=rate)
    else:
        rate = len(audio2) / len(audio1)
        audio1 = librosa.effects.time_stretch(audio1, rate=rate)

    # Ajustar o BPM da faixa 2 para corresponder ao BPM da faixa 1
    tempo1, _ = librosa.beat.beat_track(y=audio1, sr=sr1)
    tempo2, _ = librosa.beat.beat_track(y=audio2, sr=sr2)
    ratio = tempo1 / tempo2
    audio2 = librosa.effects.time_stretch(audio2, rate=1 / ratio)

    # Ajustar o comprimento das faixas para serem iguais
    min_length = min(len(audio1), len(audio2))
    audio1 = audio1[:min_length]
    audio2 = audio2[:min_length]

    # Criar o mashup combinando os áudios
    mashup = 0.5 * audio1 + 0.5 * audio2

    # Salvar o mashup como um novo arquivo de áudio
    sf.write(output_file, mashup, sr1)  # Usa a taxa de amostragem do primeiro arquivo

    print(f"Mashup criado com sucesso em: {output_file}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file1' not in request.files or 'file2' not in request.files:
        return redirect(request.url)

    file1 = request.files['file1']
    file2 = request.files['file2']

    if file1.filename == '' or file2.filename == '':
        return redirect(request.url)

    input_folder = "uploads"
    output_folder = "outputs"

    if not os.path.exists(input_folder):
        os.makedirs(input_folder)

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    file_path1 = os.path.join(input_folder, file1.filename)
    file_path2 = os.path.join(input_folder, file2.filename)

    file1.save(file_path1)
    file2.save(file_path2)

    output_file = os.path.join(output_folder, f"mashup_{file1.filename[:-4]}_{file2.filename[:-4]}.wav")

    create_mashup(file_path1, file_path2, output_file)

    return redirect(url_for('download', filename=output_file))

@app.route('/download/<path:filename>')
def download(filename):
    return send_file(filename, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)