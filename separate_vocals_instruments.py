from spleeter.separator import Separator

def separate_vocals_instruments(input_music1, output_music1, input_music2=None, output_music2=None): # Definir a função que vai separar os 2 inputs
    separator = Separator('spleeter:2stems')

    # Separação dos vocais e melodia da música 1
    separator.separate_to_file(input_music1, output_music1)

    # Separação dos vocais e melodia da música 2
    if input_music2 and output_music2:
        separator.separate_to_file(input_music2, output_music2)