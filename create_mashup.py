import librosa
import soundfile as sf

# Função para criar o mashup
def create_mashup(file1, file2, output_file):
    # Carregar os arquivos de áudio
    audio1, sr1 = librosa.load(file1, sr=None)
    audio2, sr2 = librosa.load(file2, sr=None)

    # Ajustar o tamanho dos áudios
    min_length = min(len(audio1), len(audio2))
    audio1 = audio1[:min_length]
    audio2 = audio2[:min_length]

    # Criar o mashup combinando os áudios
    mashup = 0.5 * audio1 + 0.5 * audio2

    # Salvar o mashup como um novo arquivo de áudio
    sf.write(output_file, mashup, sr1)  # Usa a taxa de amostragem do primeiro arquivo