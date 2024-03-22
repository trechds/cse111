import speech_recognition as sr

def transcript_audio_portuguese(file_path):
    mic = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        audio = mic.record(source)
        try:
            frase = mic.recognize_google(audio, language='pt-BR')
            print('Transcription: ' + frase)
        except sr.UnknownValueError:
            print('It was not possible to understand... Try again!')
            frase = ""
        return frase

# Substitua 'caminho_para_o_arquivo_de_audio' pelo caminho do seu arquivo de áudio
transcript_audio_portuguese('test.ogg')